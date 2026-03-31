# Anthropic 承认 Claude Code 用户配额消耗速度超预期

## 基本信息

- **来源链接**: https://www.theregister.com/2026/03/31/anthropic_claude_code_limits/
- **发布日期**: 2026年3月31日
- **作者**: Tim Anderson
- **标签**: Anthropic, Claude, Developer

## 摘要

Anthropic 承认其 AI 编程助手 Claude Code 的用户正在以"远超预期"的速度消耗使用配额，导致自动化工作流程中断。用户投诉强烈，Anthropic 已将此问题列为团队最高优先级。

## 主要问题

### 1. 配额消耗过快
- Claude Pro 订阅用户（年费 $200）反映，配额在每周一就耗尽，直到周六才重置
- 有用户表示30天中只有12天能使用 Claude Code
- Max 5 计划用户（$100/月）在1小时内就耗尽配额，而之前可以使用8小时

### 2. 可能的原因

**配额调整**：Anthropic 上周宣布在高峰时段减少配额，影响约7%的用户

**促销活动结束**：3月28日是 Claude 促销活动（高峰时段外配额翻倍）的最后一天

**缓存 Bug**：用户逆向工程后发现 Claude Code 存在两个缓存 Bug，会导致成本增加10-20倍。有用户证实降级到 2.1.34 版本后明显改善

**缓存生命周期短**：Prompt 缓存只有5分钟生命周期，短暂休息后继续使用会导致更高成本

### 3. 对自动化工作流程的影响
- 运行 Claude Code 的自动化工作流需要显式捕获速率限制错误
- 循环中的单个会话可能在几分钟内耗尽每日预算
- 错误看起来像通用失败，会静默触发重试

## 用户反馈

用户对配额不透明表示不满：
- Pro 计划仅承诺"至少比免费服务多5倍的使用量"
- Standard Team 计划承诺"比 Pro 计划多1.25倍"
- 确切的使用限额未公开，用户只能通过仪表盘查看已消耗配额

## 行业背景

类似问题并非孤例。本月初，Google Antigravity 用户也在抗议类似问题。这反映出 AI 开发工具的定价和使用模式存在用户与提供商之间的隐性博弈。

## 参考链接

- [Anthropic 公告](https://old.reddit.com/r/Anthropic/comments/1s7zfap/investigating_usage_limits_hitting_faster_than/)
- [用户投诉](https://old.reddit.com/r/Anthropic/comments/1s8ex9a/nothing_changed/odgoc24/)
- [缓存 Bug 报告](https://www.reddit.com/r/ClaudeCode/comments/1s7mitf/psa_claude_code_has_two_cache_bugs_that_can/)
- [Anthropic 配额调整公告](https://www.theregister.com/2026/03/26/anthropic_tweaks_usage_limits/)
- [Prompt 缓存文档](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)
