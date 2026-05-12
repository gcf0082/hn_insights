# Voker AI Agent 分析平台洞察报告

**洞察链接**: https://voker.ai

**基本信息**:
- **产品名称**: Voker
- **产品定位**: AI Agent 时代的分析平台
- **核心功能**: 为 AI Agent 提供全面的分析能力，帮助团队构建最优质的 Agent 产品
- **适用对象**: 产品经理、分析师、业务团队以及构建 AI Agent 的工程师

---

## 产品概述

Voker 是一个专为 AI Agent 设计的分析平台，旨在帮助团队深入了解 Agent 的表现和用户交互情况。该平台通过将 AI Agent 的交互转化为结构化的分析数据，使任何团队成员都能获取可操作的洞察，无需依赖工程团队的帮助。

---

## 核心功能

### 1. 自助式分析 (Self-Service Analytics)
- 产品经理、分析师和业务团队可以获取易于理解的洞察
- 无需提交工单或等待瓶颈解决
- 实现数据自服务，降低沟通成本

### 2. 性能智能 (Performance Intelligence)
- 跟踪 AI Agent 的输出内容
- 识别知识缺口
- 检测异常情况
- 衡量改进效果随时间的变化

### 3. 业务影响 (Business Impact)
- 将 Agent 指标与关键业务成果关联
- 将对话数据与已有用户数据相关联
- 量化 AI 投资回报率

---

## 核心指标追踪

Voker 提供三个核心指标来衡量 Agent 表现：

| 指标 | 描述 |
|------|------|
| **意图 (Intents)** | 识别用户想要什么。Voker 自动从自然对话中分类用户目标。 |
| **纠正 (Corrections)** | 检测用户是否未获得想要的内容。在用户流失前发现摩擦点。 |
| **解决方案 (Resolutions)** | 识别 Agent 是否解决了用户的问题。衡量每次交互的成功率。 |

---

## 技术集成

### 支持的 LLM 框架和模型
- OpenAI
- Anthropic
- Gemini
- Langchain
- CrewAI
- Vercel AI SDK

### 集成特点
- 轻量级 SDK：Python 和 TypeScript，仅需两行代码即可安装
- 数据所有权：用户完全拥有自己的数据
- 支持自托管部署：专为企业需求设计
- 生态系统友好：可与 Langfuse、Langsmith、PostHog、Mixpanel、Amplitude 等工具配合使用

### 集成代码示例
```python
# 安装 SDK
pip install voker

# 连接 Agent
from voker.ai.provider_openai import OpenAI
```

---

## 主要功能特性

1. **可查询的对话时间线**: 通过用户视角查看 Agent 对话，跨所有对话搜索主题、意图和问题。

2. **性能追踪**: 量化改进效果，了解何时需要回滚导致系统问题的更新。

3. **用户行为洞察**: 跟踪用户询问的内容、Agent 是否提供相应服务，当用户感到沮丧或退出时获得警报。

---

## 定价计划

| 计划 | 价格 | 事件数/月 | 数据保留 | 主要特性 |
|------|------|-----------|----------|----------|
| **Free** (Agent Ready) | $0 | 2,000 | 30天 | 社区支持，无限席位 |
| **Starter** (Agent Enabled) | $80/月 | 20,000 | 90天 | 邮件支持，30天免费试用 |
| **Agent First** (最受欢迎) | $400/月 | 2,000,000 | 1年 | Agent自动优化，邮件+Slack支持，30天免费试用 |
| **Enterprise** | 自定义 | 自定义 | 自定义 | 自托管部署，SSO专属优化工程师 |

---

## 目标用户群体

Voker 适用于以下团队：
- 高交互量（每月 1,000+ 聊天会话）
- 复杂的多轮对话（工具、RAG、MCP）
- 需要 Agent 洞察的跨职能团队

---

## 客户评价

- **True Classic**: "数据驱动我们所有决策，但我们没有追踪 AI 性能的方法。Voker 使监控和优化 AI 功能成为可能。" — Ben Yahalom, CEO

- **Dutch**: "Voker 让我们能够在生产环境中优化 Agent，确保投资回报率正向，同时不影响工程资源。" — Carlos Moreno, CTO

- **Coffee Clozers**: "使用 Voker，我们可以比竞争对手更快地迭代和改进 Agent。它简化了一切。" — Ariel Herrera, CTO

- **Lull**: "通过 Voker 的意图和解决方案追踪，我们了解到需要在产品和客户服务方面进行哪些投资，以及我们在哪些方面超出了目标！" — Peter Greig, VP of Data & Analytics

---

## 总结

Voker 是一个全面的 AI Agent 分析平台，通过提供意图识别、纠正检测和解决方案追踪等核心功能，帮助团队深入了解 Agent 的表现。其轻量级 SDK 集成、自助式分析能力和灵活定价使其成为构建高质量 AI Agent 产品的理想选择。

**官方网站**: https://voker.ai
**文档**: https://app.voker.ai/docs/overview