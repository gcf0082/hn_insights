# Kontext CLI 项目洞察报告

**洞察链接**: https://github.com/kontext-dev/kontext-cli

**项目名称**: kontext-security/kontext-cli

**项目类型**: 开源 CLI 工具

**核心功能**: 为 AI 编码代理提供企业级身份认证、凭证管理和治理能力

**许可证**: MIT

**编程语言**: Go 97.1%, Shell 2.9%

**星标数**: 79

**分支数**: 1

**提交数**: 47

---

## 项目概述

Kontext CLI 是一个开源的命令行工具，旨在为 AI 编码代理提供企业级的安全凭证管理能力。该工具无需改变开发者的工作方式，即可实现对企业级身份、凭证管理和治理的支持。

### 核心理念

**问题现状**: AI 编码代理需要访问 GitHub、Stripe、数据库等多种服务，目前团队通常将长期有效的 API 密钥复制到 `.env` 文件中，存在安全隐患。

**解决方案**: Kontext 用短期有效的、作用域受限的凭证替代长期 API 密钥，在会话开始时注入，会话结束时自动失效。每次工具调用都有日志记录，每个密钥都有追溯。

---

## 工作原理

### 1. 认证流程
- 运行 `kontext start --agent claude`
- 打开浏览器进行 OIDC 登录
- 将刷新令牌存储在系统密钥链中
- 可随时通过 `kontext logout` 清除

### 2. 会话管理
- 在 Kontext 后端注册会话
- 可在仪表板中查看

### 3. 凭证解析
- 读取 `.env.kontext` 文件
- 通过 RFC 8693 令牌交换将占位符替换为短期令牌

### 4. 代理启动
- 使用注入的凭证作为环境变量启动 Claude Code
- 设置治理钩子

### 5. 事件捕获
- PreToolUse、PostToolUse、UserPromptSubmit 事件流式传输到后端
- 包含用户、会话和组织归属

### 6. 清理
- 会话结束
- 凭证失效
- 临时文件移除

---

## 核心功能

### 1. 快速启动 Claude Code
```bash
kontext start --agent claude
```
无需配置文件、Docker 或设置脚本。

### 2. 临时凭证
- 短期令牌作用域仅限于会话
- 退出时自动失效
- 告别 `.env` 文件中的长期 API 密钥

### 3. 声明式凭证模板
- 在 `.env.kontext` 文件中声明项目需要的凭证
- 提交到仓库，团队成员获得相同凭证配置
- 密钥保存在 Kontext 中，不提交到源代码仓库

### 4. 治理遥测
- Claude 钩子事件流式传输到后端
- 包含用户、会话和组织归属

### 5. 安全默认
- OIDC 身份认证
- 系统密钥链存储
- RFC 8693 令牌交换
- AES-256-GCM 静态加密

### 6. 轻量级运行时
- 原生 Go 二进制文件
- 无需本地守护进程安装
- 无需 Node/Python 运行时

### 7. 更新通知
- 启动时后台检查 GitHub Releases API（24 小时缓存）
- 可通过 `KONTEXT_NO_UPDATE_CHECK=1` 禁用

---

## 声明凭证

`.env.kontext` 文件示例：

```
GITHUB_TOKEN={{kontext:github}}
STRIPE_KEY={{kontext:stripe}}
DATABASE_URL={{kontext:postgres/prod-readonly}}
```

将此文件提交到仓库，团队成员共享相同的模板，密钥留在 Kontext 中。

---

## 支持的代理

| 代理 | 标志 | 状态 |
|------|------|------|
| Claude Code | `--agent claude` | 活跃 |
| Cursor | 计划中 | 未发布 |
| Codex | 计划中 | 未发布 |

---

## 技术架构

```
kontext start --agent claude
  │
  ├── Auth: OIDC refresh token from keyring
  ├── ConnectRPC: CreateSession → session in dashboard
  ├── Sidecar: Unix socket server (kontext.sock)
  │     └── Heartbeat loop (30s)
  ├── Hooks: settings.json → Claude Code --settings
  ├── Agent: spawn claude with injected env
  │     │
  │     ├── [PreToolUse]        → kontext hook → sidecar → backend
  │     ├── [PostToolUse]       → kontext hook → sidecar → backend
  │     └── [UserPromptSubmit]  → kontext hook → sidecar → backend
  │
  └── On exit: EndSession → cleanup
```

### Go Sidecar
- 轻量级 Sidecar 进程与代理并行运行
- 通过 Unix socket 通信
- 钩子处理程序通过 Sidecar 发送规范化事件
- CLI 保持代理特定逻辑与后端合约分离

### 治理遥测
- 会话生命周期和钩子事件流向 Kontext 后端
- 为仪表板提供会话、跟踪和审计历史
- 捕获代理尝试做的事情和结果
- 不捕获 LLM 推理、令牌使用或对话历史

---

## 快速开始

### 安装
```bash
brew install kontext-security/tap/kontext
```

或直接下载二进制文件：
```bash
tmpdir="$(mktemp -d)" \
  && gh release download --repo kontext-security/kontext-cli --pattern 'kontext\_\*\_darwin\_arm64.tar.gz' --dir "$tmpdir" \
  && archive="$(find "$tmpdir" -maxdepth 1 -name 'kontext\_\*\_darwin\_arm64.tar.gz' -print -quit)" \
  && tar -xzf "$archive" -C "$tmpdir" \
  && sudo install -m 0755 "$tmpdir/kontext" /usr/local/bin/kontext
```

### 开发构建
```bash
go build -o bin/kontext ./cmd/kontext

# Generate protobuf (requires buf + plugins)
buf generate

# Test
go test ./...
go test -race ./...
go vet ./...
gofmt -w ./cmd ./internal

# Link for local use
ln -sf $(pwd)/bin/kontext ~/.local/bin/kontext
```

---

## 相关资源

- **官方网站**: https://kontext.security
- **文档**: https://docs.kontext.security/getting-started/welcome
- **Discord**: https://discord.gg/gw9UpFUhyY
- **协议定义**: [kontext-security/proto](https://github.com/kontext-security/proto/blob/main/proto/kontext/agent/v1/agent.proto)

---

## 项目标签

`cli` `golang` `security` `ai` `mcp` `secret-management` `grpc` `developer-tools` `oidc` `security-tools` `ai-agents` `kontext` `audit-logging` `credential-management`

---

## 总结

Kontext CLI 是一个创新的开源项目，解决了 AI 编码代理在企业环境中的安全凭证管理问题。通过短期令牌、OIDC 认证、完整的审计日志等功能，为团队提供了安全、可治理的 AI 代理使用体验。该项目使用 Go 语言编写，代码质量高，架构清晰，适合对 AI 安全工具有兴趣的开发者学习和贡献。