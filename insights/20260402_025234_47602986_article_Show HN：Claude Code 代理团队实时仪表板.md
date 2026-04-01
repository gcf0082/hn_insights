# 项目洞察报告：agents-observe

## 基本信息

| 项目 | 内容 |
|------|------|
| **项目名称** | agents-observe |
| **GitHub地址** | https://github.com/simple10/agents-observe |
| **项目描述** | Claude Code会话和多代理的实时可观测性仪表板 |
| **星标数** | 62 |
| **Fork数** | 2 |
| **最新版本** | v0.7.4 (2026年4月1日) |
| **提交数** | 306 |
| **许可证** | MIT |
| **主要语言** | TypeScript (90.3%) |

---

## 项目概述

agents-observe 是一个实时可观测性仪表板，专门为 Claude Code 代理设计。该项目提供了强大的过滤、搜索和多代理会话可视化功能，能够实时捕获和展示代理的完整活动轨迹。

## 核心功能

### 1. 实时事件监控
- 监控工具调用流（PreToolUse → PostToolUse 含结果）
- 展示完整代理层级结构（子代理与父代理的关系）
- 支持按代理、工具类型或全事件搜索过滤

### 2. 可视化展示
- 展开任何事件查看完整载荷、命令和结果
- 点击时间线图标跳转到流中的特定事件
- 浏览具有人类可读名称的历史会话

### 3. 多代理支持
- 协调器并行生成代码审查器、测试运行器和文档代理
- 实时观察每个代理的工作状态
- 及时发现并行执行中的问题

## 技术架构

```
Claude Code Hooks → observe_cli.mjs → API Server (SQLite) → React Dashboard
    (dumb pipe)      (HTTP POST)       (parse + store)      (WebSocket live)
```

### 组件说明

- **Hooks**: 在每个 Claude Code 事件（工具调用、提示、停止、子代理生命周期）时触发，读取原始事件并通过 HTTP POST 发送到服务器
- **Server**: 接收原始事件，提取结构化字段，存储代理元数据（名称、描述、类型、父子关系），事件通过 WebSocket 转发给订阅客户端
- **Client**: 初始加载时通过 REST API 获取事件，然后通过 WebSocket 接收实时更新

### 技术栈

| 组件 | 技术 |
|------|------|
| 后端 | Node.js + Hono + SQLite + WebSocket |
| 前端 | React 19 + shadcn |
| 容器 | Docker |
| 测试 | Vitest |

## 安装方式

### 插件安装（推荐）

1. 添加市场：`claude plugin marketplace add simple10/agents-observe`
2. 安装插件：`claude plugin install agents-observe`
3. 重启 Claude Code

安装完成后，服务器会自动作为 Docker 容器启动，Hooks 开始捕获事件。访问 http://localhost:4981 查看仪表板。

### 独立安装

1. 克隆仓库并安装依赖
2. 通过 `just setup-hooks <project>` 生成 hooks 配置
3. 将配置复制到项目的 `.claude/settings.json`

## 使用场景

### 1. 多代理工作透明化
当 Claude Code 自主运行时，会生成子代理、调用工具、读取文件、执行命令，缺乏可见性。通过 agents-observe 可以实时观察每个代理的活动。

### 2. 工具调用分析
助手的文本输出只是摘要，实际的工具调用（Bash 命令、文件读取、编辑、grep 模式）才是真实行为。agents-observe 同时展示两者。

### 3. 时间旅行调试
当子代理做出错误编辑或运行破坏性命令时，需要追溯事件的精确序列。事件流提供了完整的活动时间线和载荷。

### 4. 模式发现
通过跨会话捕获事件，可以观察代理的长期行为模式、偏好的工具以及容易卡住的地方。

## 插件技能

| 技能 | 描述 |
|------|------|
| `/observe` | 打开仪表板URL并检查服务器是否运行 |
| `/observe status` | 检查服务器健康状况并显示仪表板URL |

## 路线图

- [ ] 添加 Codex 支持
- [ ] 添加 OpenClaw 支持
- [ ] 添加 pi-code 代理支持

## 相关项目

- [Agent Super Spy](https://github.com/simple10/agent-super-spy) - 完整的代理可观测性栈，可在本地或远程运行
- [Multi-Agent Observability System](https://github.com/disler/claude-code-hooks-multi-agent-observability) - 启发了本项目
- [Claude DevTools](https://github.com/matt1398/claude-devtools) - 会话文件可视化，需在本地运行

## 故障排除

| 问题 | 解决方案 |
|------|----------|
| Docker 未运行 | 确保 Docker Desktop 或 Docker 守护进程正在运行 |
| 端口 4981 被占用 | 停止占用进程或移除陈旧容器 |
| 插件未捕获事件 | 运行 `/observe status` 检查服务器状态 |
| 事件未显示在仪表板 | 检查服务器运行、hooks 配置、网络连接 |
| WebSocket 断开 | 客户端每3秒自动重连 |

## 总结

agents-observe 为 Claude Code 提供了强大的实时可观测性能力，解决了多代理工作不透明的问题。通过捕获完整的 hook 事件流并实时展示在仪表板上，开发者可以深入了解代理的实际行为，及时发现和解决问题。该项目采用现代技术栈（React 19、Docker、SQLite），安装简便，是 Claude Code 用户的重要工具。

---

*报告生成时间：2026-04-02 02:52:34 UTC+8*