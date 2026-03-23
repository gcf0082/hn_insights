# Agent Kernel - AI 代理状态化方案洞察

**来源**: [Hacker News](https://news.ycombinator.com/item?id=47486287)  
**项目**: [oguzbilgic/agent-kernel](https://github.com/oguzbilgic/agent-kernel)  
**得分**: 35 | **评论数**: 15 | **发布时间**: 2025-12-21

---

## 项目概述

Agent Kernel 是一个极简的 AI 代理内核，旨在让任何 AI 编码代理具备状态化能力。该项目仅通过三个 Markdown 文件和一个 Git 仓库即可实现，无需数据库或复杂框架。

## 核心特性

### 内存结构

```
AGENTS.md          ← 内核（通用，不编辑）
IDENTITY.md        ← 代理身份（代理维护）
KNOWLEDGE.md       ← 知识文件索引（代理维护）
knowledge/         ← 世界事实（可变）
notes/             ← 每日会话日志（追加写入）
```

### 两种记忆类型

1. **knowledge/** - 状态记忆：关于当前现实的事实，代理在现实变化时更新
2. **notes/** - 叙事记忆：每个会话发生的事件、决策、待办事项等，仅追加写入

## 工作原理

AI 代理已经会读取 `AGENTS.md`（或 `CLAUDE.md`、`.cursorrules` 等）作为项目指令。Agent Kernel 利用这一机制来教代理"如何记住"：

- 一个文件说明"你是状态化的，以下是方法"
- 一个 Git 仓库用于存储记忆
- 纯 Markdown 文件

## 兼容性

支持任何 AI 编码代理：OpenCode、Claude Code、Codex、Cursor、Windsurf 等。

## 快速开始

```bash
git clone https://github.com/oguzbilgic/agent-kernel.git my-agent
cd my-agent
opencode  # 或 claude, codex, cursor 等
```

代理读取内核后，会意识到自己是新启动的，然后询问用户希望它扮演什么角色。代理会记住这个身份。

## 应用场景

用户可以为不同目的创建多个独立的代理仓库：
- 家庭实验室代理
- 投资代理
- 健康代理

## 评价

该项目获得了 94 颗星和 7 次 fork，表明社区对简化 AI 代理状态化管理有着强烈需求。其核心理念是利用现有的代理指令机制，无需额外基础设施工具即可实现记忆持久化。