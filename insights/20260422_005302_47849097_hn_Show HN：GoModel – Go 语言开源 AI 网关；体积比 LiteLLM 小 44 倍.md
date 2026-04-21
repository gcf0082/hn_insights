# GoModel：开源 AI 网关

**链接**: https://news.ycombinator.com/item?id=47849097
**标题**: Show HN: GoModel – an open-source AI gateway in Go; 44x lighter than LiteLLM
**发布者**: santiago-pl
**时间**: 2 小时前
**分数**: 59
**评论数**: 15

## 项目简介

GoModel 是一个开源的 AI 网关，由来自华沙的独立开发者 Jakub 自 2024 年 12 月起开发。该项目介于应用与 AI 模型提供商（如 OpenAI、Anthropic 等）之间，旨在解决以下问题：

- 按客户或团队追踪 AI 使用情况和成本
- 无需修改应用代码即可切换模型
- 更方便地调试请求流程
- 通过精确和语义缓存降低 AI 成本

## 主要优势

| 特性 | GoModel | LiteLLM |
|------|---------|---------|
| Docker 镜像大小 | ~17 MB | ~746 MB |
| 轻量化程度 | 1x | 44x+ |

- **请求工作流可视化**：请求过程清晰可见，易于调试
- **配置优先**：默认使用环境变量进行配置
- **完全开源**：无付费私有仓库

## 社区反馈

### 积极评价

- 使用 Go 语言的编译型语言方案获得好评
- 轻量级实现被认为是有价值的替代方案
- 语义缓存功能受到关注

### 功能建议

- 支持本地模型（如 vllm）
- AI 提供商订阅兼容性（如 ChatGPT、GH Copilot）
- 内置成本追踪功能（已有仪表板的 Usage 页面）

### 比较讨论

与 Bifrost（另一个 Go 语言路由器）的对比：
- GoModel 完全开源，无付费私有仓库
- 更轻量、更简单
- 调试和审计日志更方便

## 未来计划

作者表示将考虑添加 AI 提供商订阅兼容性功能。

## 链接

- 网站：https://gomodel.enterpilot.io
- GitHub：https://github.com/ENTERPILOT/GOModel/