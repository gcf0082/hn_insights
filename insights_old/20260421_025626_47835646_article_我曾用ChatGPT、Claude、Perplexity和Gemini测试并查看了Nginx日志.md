# AI流量与引荐流量：Nginx日志揭示的真相

**洞察链接：** https://surfacedby.com/blog/nginx-logs-ai-traffic-vs-referral-traffic

**来源：** SurfacedBy Blog

**发布日期：** 2026年4月19日

**作者：** Ali Khallad

---

## 核心发现

当用户向AI助手询问某个网站时，AI助手是否会真正获取页面，还是根据之前的索引来回答？通过设置Nginx探针并向主流AI聊天机器人发起强制实时获取的查询，作者获得了明确的答案。

**两种不同的信号：**
- **AI提供方抓取**：助手直接访问源站，通常带有专用User-Agent，无引荐来源
- **真实点击访问**：人类阅读AI回答后，点击引用链接，以普通浏览器访问并携带AI作为引荐来源

将两者混为一个"AI流量"数字会掩盖数据中最有价值的区分。

---

## 实验方法

作者配置了自定义Nginx日志格式来捕获默认combined日志压缩掉的Headers：

```nginx
log_format ai_probe escape=json
  '{'
    '"time":"$time_iso8601",'
    '"ip":"$remote_addr",'
    '"uri":"$request_uri",'
    '"status":$status,'
    '"ua":"$http_user_agent",'
    '"referer":"$http_referer",'
    '"accept":"$http_accept"'
  '}';
```

每个AI助手收到指向唯一查询字符串的提示（如`/?ai=chatgpt`、`/?ai=claude`等），便于属性归因。

---

## 五大AI助手的抓取行为

### 明确表明身份的助手

| 助手 | User-Agent | Accept Header | 首次访问robots.txt |
|------|-------------|---------------|-------------------|
| ChatGPT | `ChatGPT-User/1.0` | Chrome-style | 否 |
| Claude | `Claude-User/1.0` | `*/*` | 是 |
| Perplexity | `Perplexity-User/1.0` | (空) | 否 |
| Meta AI | `meta-webindexer/1.1` | `*/*` | 否 |
| Manus | Chrome UA + `Manus-User/1.0` | Chrome-style | 否 |

### 未表明身份的助手

| 助手 | 日志表现 | 结果 |
|------|---------|------|
| Gemini | 零请求来自任何Google UA | 未进行实时抓取，从索引回答 |
| Copilot | 普通Chrome 135 Linux x86_64 | 抓取了但无法与人类访客区分 |
| Grok | 普通Mac Safari 26和Mac Chrome 143 | 抓取了但无法与人类访客区分 |

---

## 关键发现详解

### ChatGPT：多IP爆发式抓取

ChatGPT-User从同一爆发内的多个源IP访问源站，通常同时拉取多个候选页面供模型决定引用哪一个。在24小时内捕获了来自五个不同Azure IP段的请求：`23.98.x.x`、`20.215.x.x`、`40.67.x.x`、`51.8.x.x`、`51.107.x.x`。如果基于单个源IP进行速率限制，会低估实际流量。

### Claude：总是先检查robots.txt

Claude-User在每次页面抓取前都先拉取`/robots.txt`，来自Anthropic拥有的IP空间`216.73.216.0/24`范围。机器人预检查符合Anthropic文档记录的行为。

### Perplexity：直接抓取，无客套

Perplexity-User直接抓取页面，无Accept Header，无引荐来源。Perplexity可以在不访问源站的情况下从自身索引回答问题，但实验证明它*可以*进行实时检索。

### Gemini：完全不可见

实验期间零请求来自任何Google User-Agent。Gemini完全从自身索引回答，不会进行到达源站的实时抓取。Google没有发布Gemini专用的检索User-Agent，如果Gemini进行实时抓取，它将以`Googlebot`的形式到达，与普通搜索索引无法区分。

### Copilot和Grok：伪装成普通浏览器

Microsoft Copilot以普通Chrome 135抓取，带有完整的浏览器风格Accept Header和CSS、JS、图片请求的正常爆发。无独特Copilot User-Agent。

Grok以普通Mac Safari 26和Mac Chrome 143抓取，无独特UA，无后缀，无Header信号可用于从请求中将其归因于xAI。

### Meta AI：文档与实际不符

Meta AI返回的信息与实时页面上已不存在的资料一致，表明采用索引优先的检索路径。当Meta确实进行实时抓取时（通过Muse Spark Surface），请求以`meta-webindexer/1.1`到达。Meta文档中的`Meta-ExternalFetcher`是用户发起检索的机器人，但实际观察到的行为与文档不完全匹配。

### Manus：最清晰的标识

Manus以`Mozilla/5.0 ... Chrome/132.0 ... ; Manus-User/1.0`抓取。`Manus-User/1.0`后缀是检索信号。与其他代理不同，Manus渲染完整页面：HTML、每个CSS文件、每个JS文件、每个图片。

---

## 可测量的两项指标

### 1. AI提供方抓取

从日志中可以明确测量的是带有文档化或观察到的检索专用User-Agent的请求：
- `ChatGPT-User`
- `Claude-User`
- `Perplexity-User`
- `Manus-User`
- `Meta-ExternalFetcher`（文档化）
- `meta-webindexer`（观察到的）

### 2. 真实访问

普通浏览器User-Agent，以AI聊天机器人作为引荐来源：
- `chatgpt.com`
- `claude.ai`
- `perplexity.ai`
- `gemini.google.com`
- `copilot.microsoft.com`
- `grok.com`
- `meta.ai`
- `google.com` / `bing.com`

搜索索引机器人（`OAI-SearchBot`、`Claude-SearchBot`、`PerplexityBot`、`Googlebot`、`Bingbot`）也会出现在日志中，但它们不是回答特定用户问题的AI——它们是在构建索引，不应计入实时检索。

训练机器人（`GPTBot`、`ClaudeBot`、`CCBot`）是第三类独立信号，也不应计入检索。

---

## 实际影响

1. **流量测量不对称**：从日志测量AI流量将因供应商而异。Google的差距是结构性的，无法通过日志解决。

2. **三大助手无法追踪**：Gemini、Copilot和Grok要么在提供方抓取日志中不可见（Gemini），要么无法与普通人类访客区分（Copilot和Grok）。

3. **Googlebot无法归因**：`Googlebot`命中无法单独归因于Gemini与经典搜索。

4. **Google-Extended不阻止Googlebot**：阻止`Google-Extended`不会阻止`Googlebot`。它只控制`Googlebot`抓取的内容是否可用于Gemini训练和基础。

5. **多IP分布**：ChatGPT从多个IP段抓取，单IP速率限制会低估。

---

## 供应商Bot分类表

| Bot | 公司 | 类别 | 来源 |
|-----|------|------|------|
| ChatGPT-User | OpenAI | 检索 | platform.openai.com/docs/bots |
| OAI-SearchBot | OpenAI | 搜索索引 | platform.openai.com/docs/bots |
| GPTBot | OpenAI | 训练 | platform.openai.com/docs/bots |
| Claude-User | Anthropic | 检索 | Anthropic crawler docs |
| Claude-SearchBot | Anthropic | 搜索索引 | Anthropic crawler docs |
| ClaudeBot | Anthropic | 训练 | Anthropic crawler docs |
| Perplexity-User | Perplexity | 检索 | docs.perplexity.ai/guides/bots |
| PerplexityBot | Perplexity | 搜索索引 | docs.perplexity.ai/guides/bots |
| Meta-ExternalFetcher | Meta | 检索（可能绕过robots.txt） | Meta web crawlers |
| Meta-ExternalAgent | Meta | 训练和产品索引 | Meta web crawlers |
| meta-webindexer | Meta | 观察到的Meta AI检索 | Meta crawler docs |
| Manus-User | Manus | 检索（代理式；完整浏览器渲染） | 本次实验观察 |
| Googlebot | Google | 搜索索引（也是AI Overviews和AI Mode的基础） | Google crawlers |
| Google-Extended | Google | 使用控制，非爬虫；控制Gemini训练和基础 | Google crawlers |
| Bingbot | Microsoft | 搜索索引（也是Copilot的基础） | Copilot public websites |
| CCBot | Common Crawl | 训练（多实验室使用） | commoncrawl.org/ccbot |

---

## 总结

通过Nginx日志分析，我们发现：

1. **5个AI助手有明确的抓取标识**：ChatGPT、Claude、Perplexity、Meta AI、Manus都可以通过User-Agent识别

2. **3个主要助手无法追踪**：Gemini完全不进行实时抓取，Copilot和Grok伪装成普通浏览器

3. **AI流量测量需要结合两种信号**：Provider-side fetch（AI直接访问）和Real visit（用户通过AI点击访问）

4. **日志测量存在结构性局限**：Google的AI助手使用与搜索相同的爬虫，无法在日志中区分

这份洞察为网站运营者提供了关于AI流量真实情况的实证数据，帮助更好地理解和测量来自AI助手的流量。
