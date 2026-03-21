# 洞察报告

## 基本信息

| 项目 | 内容 |
|------|------|
| **洞察链接** | https://twitter.com/fynnso/status/2034706304875602030 |
| **来源** | X (Twitter) |
| **发布时间** | 2026-03-20 |
| **原始报告链接** | https://xcancel.com/fynnso/status/2034706304875602030 |
| **洞察ID** | 20260321_195750_47452404_article |
| **报告生成时间** | 2026-03-21 19:57:50 |

## 摘要

开发者 @fynnso 发现 Cursor AI 的 Composer 2.0 实际上是基于 Kimi K2.5 模型（带强化学习），而非 Cursor 自主训练的基础模型。

## 核心发现

### 发现过程
- fynnso 通过在 Cursor 中配置 OpenAI base URL 并设置一个简单的请求dump服务器
- 成功捕获到 Composer 2.0 发送的请求中的模型ID：
  ```
  accounts/anysphere/models/kimi-k2p5-rl-0317-s515-fast
  ```

### 技术细节
- 模型ID明确显示为 `kimi-k2p5`，即 Kimi K2.5
- 带有 RL (Reinforcement Learning) 强化学习后训练
- Composer 1.5 会阻止这种请求捕获，但 Composer 2.0 存在漏洞
- 发现后不久 Cursor 已修复该问题

## 行业影响

### 争议焦点
1. **许可证合规性**：Kimi K2.5 采用 Modified MIT 许可证，要求在达到特定收入/用户门槛时" prominent display Kimi K2.5"
2. **商业模式质疑**：有观点认为 Cursor 正成为模型路由层，选择最便宜的模型完成任务并赚取差价
3. **透明性问题**：用户和投资者可能认为这是"从头训练"的新模型

### 社区反应
- Elon Musk 也参与了调侃
- Kimi 团队成员 Yulun Du 有相关回复
- 有人测试后发现 Composer 2 与 Opus 4.6 相比仍有差距

### 支持观点
- 从商业角度看，使用开源基础模型而非自研是合理选择
- 降低成本，加快产品迭代
- Kimi K2.5 作为开源模型，理论上可以合法使用

## 关键引用

> "so composer 2 is just Kimi K2.5 with RL at least rename the model ID"
> — @fynnso

> "Cursor is becoming a model routing layer, not an IDE. They pick the cheapest model that clears a quality bar per task, wrap it in their UX, and pocket the margin."
> — @animeshxdas

## 相关链接

- 原推文: https://twitter.com/fynnso/status/2034706304875602030
- Cursor Composer 2 发布: https://twitter.com/cursor_ai/status/2034941631871455262
- Reddit 讨论: https://www.reddit.com/r/LocalLLaMA/comments/1rytksg/

## 结论

此次发现揭示了 AI IDE 行业的一个重要趋势：基础模型的选择和更换可能比用户认知的更加灵活。Cursor Composer 2.0 基于 Kimi K2.5 本身并非问题，关键在于是否遵守相应的开源许可证要求以及是否对用户保持透明。
