---
title: EvanFlow - TDD驱动的迭代式软件开发反馈循环
link: https://github.com/evanklem/evanflow
story_id: 47916909
date: 2026-04-27
---

# EvanFlow — TDD驱动的迭代式软件开发反馈循环

## 项目概述

EvanFlow 是一个基于 Claude Code 的 TDD（测试驱动开发）驱动的迭代式软件开发框架。它通过16个 cohesive（内聚）的 Claude Code 技能和2个自定义子代理，将一个想法从头脑风暴逐步推进到实现，并在整个过程中设置了多个检查点，让开发者始终保持控制权。

**核心入口**：只需说一句 *"let's evanflow this"*，编排器就会启动整个流程。

```
brainstorm → plan → execute (sequential or parallel) → tdd → iterate → STOP
```

## 核心特性

### 1. 迭代式反馈循环

EvanFlow 的设计理念是**基于纪律的迭代累积**，而非单次生成。每个步骤都有一个检查点来控制下一步：

- **Brainstorm**：澄清意图，提出2-3种方案并进行嵌入式"烧烤"（压力测试）→ 你批准设计
- **Plan**：首先规划文件结构（深度模块化，删除测试）→ 你批准计划
- **Execute**：逐个任务执行并内联验证 → 阻塞时停止循环并向你反馈
- **TDD**：仅垂直切片——一个失败的测试 → 最小实现 → 重复。测试通过公共接口验证行为
- **Iterate**：重新阅读差异，用新眼光审视，运行质量检查，截取UI更改截图，运行"五大致命失败模式"检查清单。最多5次迭代
- **STOP**：报告，等待你的方向。代理从不自动提交、自动暂存或自动创建PR

### 2. 并行编码/监督编排

对于包含3个以上真正独立单元的计划，循环会分叉为**并行编码器/监督者编排**：每个单元一个编码器（使用垂直切片TDD和红色检查点），每个编码器一个监督者（只读审查子代理），加上一个集成监督者，在每个接触点运行命名集成测试。集成测试即 executable contract——如果双方都需要通过相同的通过测试，接口就无法漂移。

### 3. 内置硬规则

EvanFlow 包含多项来自**2025-2026年代理编码失败模式行业研究**的硬规则：

- **永不发明值**：文件路径、环境变量、ID、函数名、库API——如果不确定，代理停止并询问。（行动幻觉是最危险的代理失败模式。）
- **断言正确性警告**：研究表明62%的LLM生成的测试断言是错误的。`evanflow-tdd` 和监督者审查都会显式检查实现中的一个字符错误是否仍会让断言通过。
- **监控上下文漂移**：`evanflow-compact` 在出现症状时触发（重新询问已确定的问题，否定 earlier decisions）。行业数据显示约65%的企业AI编码失败可追溯到上下文漂移，而非原始token耗尽。
- **五大致命失败模式**：在迭代和监督审查中进行显式检查——幻觉行动、范围蔓延、级联错误、上下文丢失、工具误用。
- **无技能税**：临时问题不需要技能调用。技能是工具，不是收费站。

### 4. 技能套装

#### 默认循环（5个技能）

| 技能 | 目的 |
|------|------|
| `evanflow-brainstorming` | 澄清意图，提出2-3种方案并嵌入式"烧烤"。视觉请求的快速模式。 |
| `evanflow-writing-plans` | 首先文件结构，小任务，嵌入式"烧烤"。步骤2.5提供并行路径。 |
| `evanflow-executing-plans` | 逐任务执行并内联验证。步骤0重新提供并行路径。交给迭代，然后停止。 |
| `evanflow-tdd` | 垂直切片TDD。一个测试 → 一个实现 → 重复。通过公共接口验证行为。 |
| `evanflow-iterate` | 实现后的自审循环。重新阅读差异，修复问题，运行质���检查，截取UI。"五大致命失败模式"检查清单。 |

#### 特殊用途（8个技能）

| 技能 | 目的 |
|------|------|
| `evanflow-go` | **单一入口点。** 说"let's evanflow this"即可走完整个循环。 |
| `evanflow-glossary` | 将权威领域术语提取到 `CONTEXT.md`。标记歧义和同义词。 |
| `evanflow-improve-architecture` | 通过删除测试 + 深度模块化词汇表揭示重构机会。 |
| `evanflow-design-interface` | "设计两次"——生成3+个并行子代理，带有截然不同的约束，在深度/简单性/效率上比较。 |
| `evanflow-debug` | 根因纪律。先明确假设，修复前嵌入式"烧烤"，先写失败的测试。 |
| `evanflow-review` | 代码审查的两半（给予+接受）。不妥协于无法证明的反馈。 |
| `evanflow-prd` | 从现有上下文综合PRD。对于有意义的新功能。 |
| `evanflow-qa` | 对话式缺陷发现 → 问题草稿。提交前询问。 |

#### 跨cuts（1个技能）

| 技能 | 目的 |
|------|------|
| `evanflow-compact` | 长会话上下文管理。在清晰边界主动摘要的策略。漂移症状检查清单。 |

#### 元（1个技能）

| 技能 | 目的 |
|------|------|
| `evanflow` | 索引。共享词汇表 + 何时调用每个 `evanflow-*` 技能。 |

#### 自定义子代理（2个）

| 子代理 | 工具限制 | 目的 |
|--------|----------|------|
| `evanflow-coder` | Read, Edit, Write, Glob, Grep, Bash, TodoWrite | `evanflow-coder-overseer` 的实现子代理。工具+系统提示防止git操作、 범위外编辑、值幻觉。 |
| `evanflow-overseer` | Read, Grep, Glob (无Edit/Write/Bash) | 只读审查子代理。工具物理上强制"报告发现，永不修复"。 |

#### 捆绑钩子

`hooks/block-dangerous-git.sh` — PreToolUse 钩子，阻止破坏性git操作（`git push`, `git reset --hard`, `git clean -f`, `git branch -D`, `git checkout .`, `git restore .`）。

## 工作流程

```
你说: "let's evanflow this — 我想添加一个做X的小功能"
           │
           ▼
       evanflow-go (编排器)
           │
           ├─ 阶段0: 重申想法，范围检查
           ├─ 阶段1: evanflow-brainstorming (检查点: 设计批准)
           ├─ 阶段2: evanflow-writing-plans (检查点: 计划批准)
           │            └─ 步骤2.5: 并行化检查
           ├─ 阶段3: evanflow-executing-plans (顺序)
           │            OR
           │            evanflow-coder-overser (并行)
           │              ├─ 合同与命名测试 + 集成测试
           │              ├─ 红色检查点（所有编码器编写失败测试，编排器验证）
           │              ├─ 绿色阶段（每个编码器垂直切片TDD）
           │              ├─ 每编码器监督者（审查，永不修复）
           │              └─ 集成监督者（运行接触点测试）
           ├─ 阶段4: evanflow-iterate (5次上限，五大致命失败模式通过)
           └─ 阶段5: STOP. 报告完成的内容。等待你的方向。
```

## 安装方式

### 方式1 — Claude Code 插件市场（推荐）

```
/plugin marketplace add evanklem/evanflow
/plugin install evanflow@evanflow
```

### 方式2 — npx CLI

```
npx skills@latest add evanklem/evanflow -s '*' -y
```

### 方式3 — 手动复制

```bash
git clone https://github.com/evanklem/evanflow.git
cd evanflow
mkdir -p .claude/skills
cp -r skills/* .claude/skills/
mkdir -p .claude/agents
cp agents/*.md .claude/agents/
mkdir -p .claude/hooks
cp hooks/block-dangerous-git.sh .claude/hooks/
chmod +x .claude/hooks/block-dangerous-git.sh
```

## 依赖要求

- **Claude Code**（任何最近版本）
- **Bash**（Linux, macOS或Windows + WSL）
- **`jq`**（用于钩子脚本解析Claude的JSON工具输入）

可选但推荐：

- **`chromium`** 或 `google-chrome`** — 用于 `evanflow-iterate` 的UI更改视觉验证。

## 核心价值

1. **conductor, not autopilot**：真正的检查点在设计批准、计划批准和迭代后。代理停止于每个 git 操作并等待你的方向。
2. **无自动提交**：从不自动提交、自动暂存或自动创建PR。
3. **无强制仪式**：不必要时的 auto-commits。没有"必须调用技能"的税。
4. **验证优先**：质量检查（类型检查、lint、测试）在任何"完成"报告之前运行。

## 技术栈

- **语言**：Shell (100%)
- **许可证**：MIT

## 相关研究

EvanFlow 的设计受到以下行业研究的启发：

- Anthropic的 [2026年代理编码趋势报告](https://resources.anthropic.com/hubfs/2026%20Agentic%20Coding%20Trends%20Report.pdf)
- [编码代理的9个关键失败模式（DAPLab, Columbia）](https://daplab.cs.columbia.edu/general/2026/01/08/9-critical-failure-patterns-of-coding-agents.html)
- [代码生成的测试驱动开发](https://arxiv.org/pdf/2402.13521)（arXiv 2402.13521）——断言正确性发现

## 总结

EvanFlow 是一个精心设计的软件开发框架，通过16个 cohesive 技能和2个自定义子代理，将TDD纪律和迭代反馈循环深度嵌入 Claude Code 工作流程。它强调验证优先、上下文管理和人类控制，是现代AI辅助软件开发的优秀实践。

**Star**: 106 | **Fork**: 4

---

*洞察生成时间: 2026-04-27*