# 洞察报告：agent-skills-eval

## 基本信息

| 项目 | 内容 |
|------|------|
| **洞察链接** | https://github.com/darkrishabh/agent-skills-eval |
| **项目名称** | agent-skills-eval |
| **项目描述** | Agent Skills 的测试运行器，用于评估 AI Agent 技能的实际效果 |
| **Stars** | 109 |
| **Forks** | 3 |
| **主要语言** | TypeScript (82.2%), JavaScript (17.8%) |
| **许可证** | MIT |
| **官网** | https://darkrishabh.github.io/agent-skills-eval/ |

---

## 项目概述

`agent-skills-eval` 是 Anthropic 推出的 Agent Skills 生态系统的测试框架，用于验证 `SKILL.md` 是否真正提升了模型的任务表现。它解决了 AI Agent 开发中的一个核心难题：如何**量化**技能的实际效果。

### 核心功能

1. **双模式对比评估**：对每个 eval 同时运行"加载技能"和"不使用技能"两种模式，直观展示技能带来的提升
2. **Judge 模型评分**：使用任意聊天模型作为评判者，基于预设的 assertions 进行通过/失败判定
3. **CLI + SDK 双接口**：一行命令快速上手，TypeScript SDK 支持自定义流水线
4. **OpenAI 兼容**：开箱即用支持 OpenAI、Together、Groq、Anthropic（通过 OpenAI 兼容层）、本地 Llama 服务器等
5. **工具调用断言**：支持对调用工具的 Agent 进行确定性检查，而不仅仅是文本生成
6. **静态 HTML 报告**：生成的报告可发布到任意位置，无需基础设施

---

## 技术架构

### 目录结构

```
agent-skills-workspace/
└── iteration-1/
    ├── meta.json              # 运行元数据
    ├── benchmark.json         # 汇总的通过/失败率
    ├── eval-basic/
    │   ├── with_skill/        # 输出、计时、评判分级
    │   └── without_skill/      # 基线对比
    └── report/
        └── index.html         # 可视化报告
```

### 工作流程

```
same prompt
      │
      ├── with_skill ──→ target model ──→ output
      │                                            │
      └──────────────────────┬───────────────────────┘
                             ▼
                      judge model
                      (评分两个输出)
                             ▼
                    pass / fail
```

### YAML 配置示例

```yaml
root: ./skills
workspace: ./agent-skills-workspace
baseline: true
target: gpt-4o-mini
judge: gpt-4o-mini
baseUrl: https://api.openai.com/v1
apiKeyEnv: OPENAI_API_KEY
concurrency: 4
strict: true
```

---

## SKILL 格式规范

符合 agentskills.io 规范：

```yaml
---
name: my-skill
description: 分析小 CSV 文件。
license: MIT
compatibility: 适用于支持文本的聊天模型。
---

当收到 CSV 文件时，识别最重要的趋势并引用相关行。
```

### evals/evals.json 格式

```json
{
  "skill_name": "my-skill",
  "evals": [
    {
      "id": "basic",
      "name": "基本行为",
      "prompt": "使用附件数据总结收入。",
      "files": ["evals/files/input.csv"],
      "expected_output": "响应识别出收入最高的月份。",
      "assertions": ["输出识别出收入最高的月份。"]
    }
  ]
}
```

---

## 快速开始

```bash
npx agent-skills-eval ./skills \
  --target gpt-4o-mini \
  --judge gpt-4o-mini \
  --baseline \
  --strict
```

---

## 与 agentskills.io 的兼容性

完全实现 agentskills.io 规范：
- `SKILL.md` YAML frontmatter 验证（name、description、license、compatibility 等）
- 严格的格式验证（名称长度、小写连字符格式、目录匹配等）
- 官方 artifact 布局：`iteration-N/<eval>/<mode>/outputs`
- 支持 `with_skill` 和 `without_skill` 基线对比

---

## 应用场景

1. **CI/CD 集成**：在发布流程中自动验证技能效果
2. **技能迭代**：量化每次修改带来的实际提升
3. **多模型对比**：比较不同模型对同一技能的效果差异
4. **自定义仪表盘**：SDK 支持对接自有数据分析系统

---

## 总结

`agent-skills-eval` 是 Agent Skills 生态系统的关键工具，它将技能评估从"凭感觉"转变为"有数据支撑"。通过双模式对比和 Judge 评分机制，开发者可以客观地验证技能是否真的有效，是 AI Agent 开发中不可或缺的测试基础设施。