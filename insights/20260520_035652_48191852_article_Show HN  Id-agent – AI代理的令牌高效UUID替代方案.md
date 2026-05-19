# id-agent 项目洞察报告

**洞察链接**: https://github.com/vostride/id-agent

**项目名称**: id-agent
**项目描述**: Token efficient IDs for AI agents - UUID alternative for the agentic era
**GitHub 星级**: 38 stars
**编程语言**: TypeScript 100%
**许可证**: MIT

---

## 项目概述

id-agent 是一个专为 AI 代理时代设计的 ID 生成库，旨在解决传统 UUID 在 LLM 场景下的痛点。UUID 存在两个主要问题： token 消耗高（约 23 个 token）以及容易被 LLM 产生幻觉。id-agent 生成基于单词的可读 ID，仅需约 14 个 token，同时提供相当的碰撞 resistance。

## 核心特性

### 1. Token 高效
- 每个单词在 o200k_base 分词器（GPT-4o、GPT-4.1 等）中恰好是 1 个 BPE token
- 8 词 ID 仅需约 14 token，比 UUID 节省 39%

### 2. 碰撞安全
- 可配置熵值：12 到 192 位
- 默认 8 词（96 位熵），在 300 万亿级别内碰撞概率极低

### 3. 输入验证
- 使用 Zod 进行模式验证
- 所有公共 API 都有类型检查

## API 概览

### idAgent(opts?)
生成随机可读 ID：
```typescript
idAgent() // 8 词，~96 位熵
idAgent({ words: 5 }) // 5 词，~60 位熵
idAgent({ prefix: 'user' }) // 带前缀
```

### idAgent.from(input, opts?)
基于输入字符串生成确定性 ID（使用 HMAC-SHA256）：
```typescript
await idAgent.from('user@example.com')
```

### parse(id)
解析 ID 为组件

### validate(id)
验证 ID 有效性

### createAliasMap(opts)
创建双向别名映射，用于 LLM 上下文中减少 token 消耗

### detectDuplicates(opts)
扫描重复 ID

## 熵与碰撞概率

| 单词数 | 位数 | 1K 条目碰撞概率 | 1M 条目碰撞概率 | 50% 碰撞阈值 |
|--------|------|-----------------|-----------------|--------------|
| 3      | 36   | 7.3×10⁻⁶        | ~1              | ~309K        |
| 5      | 60   | 4.3×10⁻¹³       | 4.3×10⁻⁷       | ~13 亿       |
| 8      | 96   | 6.3×10⁻²⁴       | 6.3×10⁻¹⁸      | ~331 万亿    |
| 10     | 120  | 3.8×10⁻³¹       | 3.8×10⁻²⁵      | ~1.4×10¹⁸   |

## 适用场景推荐

- **开发/测试**: `words: 3` (36 位，约 5 token)
- **团队工具**: `words: 4` (48 位，约 2000 万条目安全)
- **生产 SaaS**: `words: 5` (60 位，约 10 亿条目安全)
- **高容量/分布式**: `words: 8` (默认，96 位)
- **UUID 等效**: `words: 10` (120 位)

## 技术实现

- **随机 ID**: 使用 `crypto.getRandomValues()` (CSPRNG)
- **确定性 ID**: 使用 Web Crypto API 的 HMAC-SHA256
- **单词列表**: 4096 个英语单词，每个 3-6 个字符，已过滤攻击性词汇和同音词

## 总结

id-agent 为 AI 代理应用提供了高效的 ID 解决方案，特别适合需要与 LLM 交互的场景。其 token 优化特性和灵活的配置选项使其成为传统 UUID 的理想替代品。