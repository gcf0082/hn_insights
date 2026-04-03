# Agent Kernel 项目洞察报告

**洞察链接**: https://github.com/oguzbilgic/agent-kernel

**项目名称**: agent-kernel
**作者**: oguzbilgic
**星标数**: 144
**分支数**: 11
**许可证**: MIT

---

## 项目概述

Agent Kernel 是一个最小化内核，用于让任何 AI 编码代理具有状态化能力。只需克隆项目、指向代理、即可开始使用。

## 核心功能

- **跨会话记忆**: 代理能够记住之前会话的内容
- **笔记功能**: 代理可以记录笔记并在过去工作的基础上继续
- **无需框架**: 不需要数据库或复杂的框架
- **极简设计**: 仅需三个 Markdown 文件和一个 Git 仓库

## 快速开始

```bash
git clone https://github.com/oguzbilgic/agent-kernel.git my-agent
cd my-agent
opencode     # 或 claude, codex, cursor 等
```

代理会读取内核意识到自己是新设置的，然后询问你想让它扮演的角色。告诉它后，它会记住。

## 内存结构

```
AGENTS.md          ← 内核（通用，不要编辑）
IDENTITY.md        ← 代理的身份（代理维护）
KNOWLEDGE.md       → 知识文件的索引（代理维护）
knowledge/         ← 关于世界的知识（可变更）
notes/             ← 每日会话日志（只追加）
```

### 两种记忆类型

1. **`knowledge/`** — 状态记忆。关于当前实际情况的事实。当现实发生变化时，代理会更新这些内容。
2. **`notes/`** — 叙述记忆。每个会话发生了什么——决策、行动、待办事项。只追加模式，当天结束后不再修改。

## 工作原理

AI 代理已经会读取 `AGENTS.md`（或 `CLAUDE.md`、`.cursorrules` 等）作为项目指令。这个内核利用这种机制来教代理如何记住。

代理不需要数据库、向量存储或自定义框架。它只需要：
- 一个文件说明"你是状态化的，这里是方法"
- 一个用于存储记忆的 Git 仓库
- 纯 Markdown 文件

## 多代理支持

每个代理都是独立的仓库。创建另一个代理：

```bash
git clone https://github.com/oguzbilgic/agent-kernel.git another-agent
cd another-agent
opencode     # 或 claude, codex 等
```

相同的内核，不同的身份，不同的知识。你可以有 homelab 代理、投资代理、健康代理——全部运行相同的操作系统。

## 兼容性

支持任何 AI 编码代理：
- OpenCode
- Claude Code
- Codex
- Cursor
- Windsurf
- 等

## 总结

Agent Kernel 提供了一种极简但强大的方式来解决 AI 代理的长期记忆问题。通过利用现有的 Git 工作流和 Markdown 文件，它无需复杂的基础设施即可实现状态化代理。这种方法的优势在于：

1. **简单性**: 只需要 Git 和 Markdown
2. **灵活性**: 兼容多种 AI 代理工具
3. **可移植性**: 记忆存储在 Git 仓库中，便于备份和同步
4. **自然的工作流**: 符合开发者习惯的版本控制方式
