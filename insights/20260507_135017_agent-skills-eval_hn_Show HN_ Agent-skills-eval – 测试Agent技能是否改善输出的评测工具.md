# Agent-skills-eval 洞察报告

## 基本信息

| 项目 | 内容 |
|------|------|
| **标题** | Show HN: Agent-skills-eval – Test whether Agent Skills improve outputs |
| **项目地址** | https://github.com/darkrishabh/agent-skills-eval |
| **文档地址** | https://darkrishabh.github.io/agent-skills-eval/ |
| **技术栈** | TypeScript / Node.js |
| **许可证** | MIT |
| **Stars** | 109 |
| **标签** | cli, yaml, typescript, ai-agents, llm-evaluation, agent-evals, agent-skills |

## 项目概述

Agent-skills-eval 是 [Agent Skills](https://agentskills.io) 生态系统的测试框架——Anthropic 提出的开放标准，用于为 AI 代理提供领域知识。其核心使命是解决一个关键问题：**如何科学地证明一个 `SKILL.md` 确实提升了模型的任务表现？**

该项目用**对照实验**的方式回答这个问题：对同一提示分别运行 `with_skill`（加载技能的版本）和 `without_skill`（无技能的基线版本），用评判模型对两边的输出进行评分，最终生成并排对比报告。

## 主要功能

- **对照评测流程**：每个评测自动运行两次（有技能 vs 无技能），量化技能带来的真实提升
- **评判模型评分**：使用任意聊天模型作为评判，基于预期输出和断言给出通过/失败的判定
- **TypeScript SDK + CLI**：一行命令即可在 CI 中使用，完整 SDK 支持自定义流水线和面板
- **OpenAI 兼容**：开箱支持 OpenAI、Together、Groq、Anthropic（通过兼容层）以及本地 Llama 服务器
- **工具调用断言**：支持对调用工具的智能体进行确定性检测，不仅限于文本生成
- **静态 HTML 报告**：生成可随处部署的静态站点，包含每项评测的详细对比
- **标准化输出**：JSON / JSONL 格式的评测工件，支持跨版本差分对比

## 工作流程

```
同一提示 → with_skill（加载 SKILL.md）→ 目标模型 → 输出
         → without_skill（基线）      → 目标模型 → 输出
                                              ↓
                                       评判模型评分
                                              ↓
                                       通过/失败判定
```

## 创新点

1. **填补 Agent Skills 生态的关键空白**：`agentskills.io` 规范定义了如何编写技能，但缺少验证技能有效性的工具。agent-skills-eval 是缺失的那一块拼图。

2. **A/B 测试式的评测思维**：不是简单判断输出好坏，而是通过对照实验量化技能带来的边际收益——这是对社区"是否过度炒作"质疑的有力回应。

3. **完全的规范兼容性**：实现了完整的 agentskills.io 规范——`SKILL.md` 前置元数据验证、`evals/evals.json` 模式校验、官方工件目录布局，可作为该规范的参考实现。

4. **可插拔 Provider 架构**：通过实现五字段单方法的 `Provider` 接口即可接入任意后端，包括 Ollama、vLLM、内部 API 等。

## 潜在价值

- **为技能市场提供质量背书**：如果 Agent Skills 形成一个生态市场，agent-skills-eval 可以成为技能质量认证的标准工具
- **加速团队采用决策**：团队在引入某项技能前，可以用数据回答"这个技能真的有用吗？"
- **技能迭代优化**：开发者可以迭代优化技能文件，通过评测数据验证每个版本的改进
- **CI 集成**：将技能评测纳入持续集成流水线，防止技能退化

## 改进建议

- 支持更多非 OpenAI 兼容的 provider（如原生 Anthropic API），减少对第三方兼容层的依赖
- 提供在线评测报告分享服务，方便团队间对比评测结果
- 增加评测数据的聚合和趋势分析能力，观察技能效果随时间的变化
- 考虑支持多轮对话评测场景，而非仅限于单轮提示
- 社区技能排行榜：基于评测通过率建立公开排行榜，推动技能质量竞争

## 总结

Agent-skills-eval 是 Agent Skills 生态系统中一个精准定位的工具——它不试图做所有事，而是聚焦于一个核心问题并用工程化的方式解决它。随着 Agent Skills 被更多团队采纳，这类验证工具的重要性只会越来越高。项目的 TypeScript 技术栈和对 OpenAI 兼容 API 的支持也降低了使用门槛。
