# 洞察报告：agent-kernel

## 基本信息

| 项目 | 内容 |
|------|------|
| **洞察链接** | https://github.com/oguzbilgic/agent-kernel |
| **项目名称** | agent-kernel |
| **项目描述** | Minimal kernel to make any AI coding agent stateful. Clone, point your agent, go. |
| **星数** | 94 |
| **Fork数** | 7 |
| **License** | MIT |
| **主题标签** | opencode, agents, agentic-ai, claude-code, codex-cli, openclaw |

## 项目概述

Agent Kernel 是一个极简的AI代理内核，可以让任何AI编码代理变得有状态化。项目设计理念是"Clone, point your agent, go"——只需克隆仓库、启动代理即可使用。

## 核心特性

### 记忆结构

项目采用纯Markdown文件的简单结构：

- **AGENTS.md** — 内核文件（通用，不需编辑）
- **IDENTITY.md** — 代理身份定义（由代理维护）
- **KNOWLEDGE.md** — 知识文件索引（由代理维护）
- **knowledge/** — 关于世界的Facts（可变的）
- **notes/** — 每日会话日志（只追加）

### 两种记忆类型

1. **knowledge/** — 状态记忆。当前事物的事实，代理在现实变化时更新。
2. **notes/** — 叙述记忆。每个会话发生了什么——决策、行动、待办事项。只追加，日结束后不再修改。

### 工作原理

AI代理已经会读取`AGENTS.md`（或`CLAUDE.md`、`.cursorrules`等）作为项目指令。这个内核利用这一机制来教代理"如何记住"。

代理不需要数据库、向量存储或自定义框架，只需要：
- 一个文件说明"你是有状态的，这是方法"
- 一个git仓库存储记忆
- 纯Markdown文件

## 快速开始

```bash
git clone https://github.com/oguzbilgic/agent-kernel.git my-agent
cd my-agent
opencode  # 或 claude, codex, cursor 等
```

启动后，代理读取内核，意识到是新环境，会询问你想让它成为什么角色。告诉它后，它会记住。

## 多代理支持

每个代理都是独立的仓库。创建新代理：

```bash
git clone https://github.com/oguzbilgic/agent-kernel.git another-agent
cd another-agent
opencode  # 或 claude, codex 等
```

相同的内核，不同的身份和知识。可以有 homelab 代理、投资代理、健康代理——都在运行同一个"操作系统"。

## 兼容性

支持任何AI编码代理：OpenCode、Claude Code、Codex、Cursor、Windsurf等。

## 总结

Agent Kernel 提供了一种极简但强大的方式，让AI代理具备持久记忆能力。通过利用现有的代理指令机制（AGENTS.md），无需引入复杂的数据库或框架，仅靠Git仓库和Markdown文件即可实现有状态的AI代理。这种设计轻量、灵活且易于使用。