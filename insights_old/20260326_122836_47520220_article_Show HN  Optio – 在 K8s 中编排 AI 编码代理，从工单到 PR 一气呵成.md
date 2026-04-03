# Optio 项目洞察报告

**洞察链接**: https://github.com/jonwiggins/optio

## 基本信息

| 项目 | 值 |
|------|-----|
| 项目名称 | Optio |
| 作者 | jonwiggins |
| 许可证 | MIT |
| Stars | 71 |
| 语言 | TypeScript (98.3%) |
| 提交数 | 149 |

## 项目简介

Optio 是一个用于 AI 编码代理的工作流编排工具，实现从任务到合并 PR 的完整自动化流程。用户提交任务（通过 Web UI、GitHub Issue 或 Linear 工单），Optio 会自动处理后续所有步骤：配置隔离环境、运行 AI 代理、打开 PR、监控 CI、触发代码审查、自动修复失败，直至合并 PR。

## 核心功能

1. **自主反馈循环** - CI 失败时自动恢复代理运行、合并冲突时自动重新基、审查反馈自动推送修复
2. **Pod 级仓库架构** - 每个仓库一个长期存在的 Kubernetes Pod，使用 git worktree 实现隔离
3. **代码审查代理** - 自动启动审查代理作为子任务，支持独立的提示词和模型配置
4. **多渠道任务接入** - 支持 Web UI、GitHub Issues 和 Linear 工单
5. **实时仪表盘** - 实时日志流、流水线进度、成本分析和集群健康状态

## 技术架构

- **API 层**: Fastify 5 + Drizzle ORM + BullMQ
- **Web 层**: Next.js 15 + Tailwind CSS 4 + Zustand
- **数据库**: PostgreSQL 16
- **队列**: Redis 7 + BullMQ
- **运行时**: Kubernetes
- **AI 代理**: Claude Code、OpenAI Codex

## 工作流程

1. **接入** - 任务来自 Web UI、GitHub Issues 或 Linear 工单
2. **配置** - 查找或创建 Kubernetes Pod，为仓库创建 git worktree
3. **执行** - AI 代理运行并编写代码
4. **PR 生命周期** - 每 30 秒轮询 PR 的 CI 状态和审查状态
5. **反馈循环** - CI 失败、合并冲突和审查反馈自动恢复代理
6. **完成** - PR 被压缩合并，关联问题被关闭，成本被记录

## 快速启动

```bash
git clone https://github.com/jonwiggins/optio.git && cd optio
pnpm install
./scripts/setup-local.sh
docker build -t optio-agent:latest -f Dockerfile.agent .
pnpm dev
# API → http://localhost:4000
# Web → http://localhost:3100
```

## 项目结构

```
apps/
  api/          Fastify API 服务器、BullMQ 工作线程、WebSocket 端点
  web/          Next.js 仪表盘，实时流式传输、成本分析

packages/
  shared/             类型、任务状态机、提示词模板
  container-runtime/  Kubernetes Pod 生命周期
  agent-adapters/     Claude Code + Codex 适配器
  ticket-providers/   GitHub Issues、Linear 提供商

images/               容器 Dockerfiles
helm/optio/           生产 Kubernetes 部署 Helm Chart
scripts/              设置和入口脚本
```

## 总结

Optio 是一个创新的 AI 编码代理工作流编排系统，通过自动化的反馈循环机制，实现了从任务描述到 PR 合并的完全自动化。其核心优势在于能够自动处理 CI 失败、代码审查反馈和合并冲突，大大减少了人工干预的需要。该项目采用现代化的技术栈（TypeScript、Next.js、Fastify、PostgreSQL、Kubernetes），适合需要自动化软件开发流程的团队使用。
