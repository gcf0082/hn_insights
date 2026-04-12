---
title: claudraband 项目洞察报告
date: '2026-04-13'
source: https://github.com/halfwhey/claudraband
author: halfway
tags:
  - Claude Code
  - CLI工具
  - 自动化
  - ACP
---

# claudraband 项目洞察报告

## 基本信息

| 项目 | 信息 |
|------|------|
| 仓库名称 | claudraband |
| 作者 | halfwhey |
| GitHub 地址 | https://github.com/halfwhey/claudraband |
| 简介 | 程序化控制 Claude Code |
| 语言 | TypeScript (93.6%), JavaScript (6.2%) |
| 许可证 | MIT |
| Stars | 86 |
| Fork 数 | 2 |
| 最新版本 | 0.6.1 (2026-04-12) |
| 提交数 | 30 commits |

## 项目概述

`claudraband` 是一个实验性项目，用于程序化控制 Claude Code（Anthropic 官方 CLI 工具）。它将官方 Claude Code TUI 封装在受控终端中，支持保持会话存活、恢复会话、回答待处理提示、通过守护程序暴露会话，或通过 ACP 驱动会话。

这是一个面向高级用户的强力工具，而非面向 Claude SDK 的替代品。它专注于个人临时使用场景。

## 核心功能

### 1. 可恢复的非交互式工作流
- 类似于 `claude -p`，但支持会话持久化
- 支持会话恢复：`cband continue <session-id> 'what was the result of the research?'`

### 2. HTTP 守护程序
- 提供 HTTP daemon 用于远程或无头会话控制
- 默认端口：7842
- 支持创建、附加、继续会话

### 3. ACP 服务器
- 支持编辑器和其他前端集成
- 支持多种模型（opus、haiku 等）

### 4. TypeScript 库
- 提供完整的编程接口
- 可集成到自定义工具中

## 安装使用

```bash
# 一次性运行
npx @halfwhey/claudraband "review the staged diff"
bunx @halfwhey/claudraband "review the staged diff"

# 全局安装
npm install -g @halfwhey/claudraband
```

## 快速开始命令

```bash
# 本地持久会话
cband "audit the last commit and tell me what looks risky"
cband sessions
cband continue <session-id> "keep going"
cband continue <session-id> --select 2

# 守护程序模式
cband serve --host 127.0.0.1 --port 7842
cband --connect localhost:7842 "start a migration plan"

# ACP 模式
cband acp --model opus
```

## 项目结构

- `.claude/` - Claude 配置
- `assets/` - 资源文件
- `docs/` - 文档
- `examples/` - 示例代码
- `integration-test/` - 集成测试
- `packages/` - 包
- `skills/` - 技能定义

## 使用示例

1. **自我审问**：Claude 可以审问旧的 Claude 会话并证明其选择
2. **Toad via ACP**：Toad 可使用 claudraband ACP 作为替代前端
3. **Zed via ACP**：Zed 也支持 claudraband ACP

## 技术特点

- 使用 tmux 作为终端运行时（首选）
- 实验性 xterm.js 后端（用于无头场景）
- 会话存储在 `~/.claudraband/`
- 捆绑 Claude Code `@anthropic-ai/claude-code@2.1.96`

## 注意事项

1. 这不是 Claude SDK 的替代品
2. 不处理 OAuth 认证，需通过 Claude Code 本身认证
3. 每个交互都通过真实 Claude Code 会话运行
4. 项目仍在演进中，API 可能变化

## 文档链接

- [CLI 文档](https://github.com/halfwhey/claudraband/blob/master/docs/cli.md)
- [库文档](https://github.com/halfwhey/claudraband/blob/master/docs/library.md)
- [守护程序 API](https://github.com/halfwhey/claudraband/blob/master/docs/daemon-api.md)

## 适用场景

- 自动化代码审查
- 持续集成中的 Claude 交互
- 远程或无头环境使用 Claude Code
- 构建自定义 Claude 工作流
- 编辑器集成（如 Zed、Toad）

## 总结

claudraband 为 Claude Code 用户提供了强大的程序化控制能力，是追求高效工作流的���发者利器。其实验性质意味着使用需谨慎，但86星和持续更新的版本显示其在社区中获得了认可。