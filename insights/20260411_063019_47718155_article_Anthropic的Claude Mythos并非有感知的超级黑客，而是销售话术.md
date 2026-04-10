# 洞察报告：Anthropic 的 Claude Mythos 并非有意识的超级黑客，只是一个销售噱头

**基本信息**

- **发布日期**：2026-04-11
- **来源**：Tom's Hardware
- **原文链接**：https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropics-claude-mythos-isnt-a-sentient-super-hacker-its-a-sales-pitch-claims-of-thousands-of-severe-zero-days-rely-on-just-198-manual-reviews
- **作者**：Jon Martindale

---

## 核心观点

Anthropic 公司最近发布的 Claude Mythos AI 模型引发了广泛关注，该公司声称该模型发现了“数千个”严重零日漏洞。然而，深入分析显示这一说法存在明显夸大成分，实际上所谓的“数千个”漏洞仅基于 198 次人工审查。

## 主要发现

### 1. 漏洞发现数量存在夸大

Anthropic 声称发现了“数千个高严重性漏洞”，涵盖所有主流操作系统和网页浏览器。但根据其Own分析显示：

- 在 198 份人工审查的漏洞报告中，专家仅在 90% 的案例中同意 Claude 的严重性评估
- 许多漏洞存在于较老的软件中，或根本无法利用
- 部分漏洞已被近期修复

### 2. 实际可利用性有限

以 FFMPeg 漏洞为例，这个存在了 16 年的漏洞经过 Anthropic 自身分析后被认定为“并非关键严重性漏洞”，且“很难将其转化为可用的漏洞”。

对于 Linux 内核漏洞，虽然 Mythos 发现了多个潜在漏洞，但由于 Linux 的纵深防御安全系统，无法实际利用这些漏洞。

### 3. 测试结果并不惊人

在超过 7000 个开源软件栈的 OSS-Fuzz 风格测试中，Mythos 发现了约 600 个可导致崩溃的漏洞和 10 个严重漏洞。这虽然比之前的 Claude 模型更好，但并非数千个具有破坏性的漏洞。

## 销售策略分析

### 恐惧营销模式

Anthropic 长期以来利用“AI 危险论”作为其销售策略的一部分：

- 2025 年声称挫败了“首个 AI 策划的网络攻击”
- CEO Dario Amodei 曾表示 AI 可能取代 20% 的白领工作
- 反复强调 AI 需要严格控制和监控

### 商业动机明显

- Anthropic 是首个获得美国政府安全许可的大型语言模型 AI
- 虽然有消费级产品，但更倾向于向大型企业和政府机构销售服务
- 将 Mythos 描述为“危险工具”有助于凸显其“安全合作伙伴”的价值

## 关于“有意识 AI ”的澄清

Anthropic 在报告中反复暗示不确定新 AI 是否有意识，但实际上：

- AI 并不具有意识
- 更像是 John Searle“中文房间”思想实验的产物
- AI 不真正记住任何生物意义上的事物，只能根据先前输入调整响应权重

## 结论

Claude Mythos 虽然在发现软件漏洞方面表现不错，但远不如 Anthropic 宣称的那么令人担忧。将发现的所有漏洞描述为“数千个严重零日漏洞”是一种营销手段，而非客观的技术评估。如果 Anthropic 和其他软件开发者能够使用 AI 发现并修补漏洞，这是好消息，而非令人恐惧的消息。

---

*本报告由 AI 自动生成，仅供参考。*