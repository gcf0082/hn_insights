# Anthropic (Claude) 提供商洞察报告

## 基本信息

| 项目 | 内容 |
|------|------|
| **洞察链接** | https://docs.openclaw.ai/providers/anthropic |
| **来源平台** | OpenClaw 文档 |
| **提供商** | Anthropic (Claude) |
| **生成时间** | 2026-04-21 15:25:37 |

---

## 概述

Anthropic 构建了 **Claude** 模型系列，通过 API 和 Claude CLI 提供访问支持。在 OpenClaw 中，Anthropic API 密钥和 Claude CLI 重用均受支持。现有遗留的 Anthropic token 配置仍可在运行时使用。

> **注意**：Anthropic 工作人员表示 OpenClaw 风格的 Claude CLI 使用已被允许，因此 OpenClaw 将 Claude CLI 重用和 `claude -p` 使用视为此集成的 sanctioned 方式，除非 Anthropic 发布新政策。对于长期运行的网关主机，Anthropic API 密钥仍是最清晰和可预测的生产路径。

---

## 认证方式

### 方式一：Anthropic API 密钥

**适用场景**：标准 API 访问和按量计费

在 Anthropic Console 创建 API 密钥：

```bash
openclaw onboard
# 选择：Anthropic API key

# 或非交互式
openclaw onboard --anthropic-api-key "$ANTHROPIC_API_KEY"
```

**配置示例**：

```json5
{
  env: { ANTHROPIC_API_KEY: "sk-ant-..." },
  agents: { defaults: { model: { primary: "anthropic/claude-opus-4-6" } } },
}
```

### 方式二：Claude CLI 后端

OpenClaw 支持捆绑的 Anthropic `claude-cli` 后端：

- Anthropic 工作人员表示此用法已被允许
- 如果主机上已使用 Claude CLI，OpenClaw 可直接重用该登录
- 适用于想要使用现有 Claude CLI 登录的用户

---

## Thinking 默认配置 (Claude 4.6)

- Anthropic Claude 4.6 模型在 OpenClaw 中未设置明确 thinking 级别时，默认为 `adaptive`（自适应思考）
- 可通过 `/think:<level>` 按消息覆盖，或在模型参数中配置：
  ```
  agents.defaults.models["anthropic/<model>"].params.thinking
  ```

**相关文档**：

- [自适应思考](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking)
- [扩展思考](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)

---

## Fast 模式 (Anthropic API)

OpenClaw 的共享 `/fast` 开关支持直接公开的 Anthropic 流量，包括 API 密钥和 OAuth 认证的请求：

- `/fast on` 映射到 `service_tier: "auto"`
- `/fast off` 映射到 `service_tier: "standard_only"`

**重要限制**：

- OpenClaw 仅对直接 `api.anthropic.com` 请求注入 Anthropic 服务层级
- 如果通过代理或网关路由 `anthropic/*`，`/fast` 不会修改 `service_tier`
- 显式的 Anthropic `serviceTier` 或 `service_tier` 模型参数会覆盖 `/fast` 默认值

---

## 提示缓存 (Anthropic API)

OpenClaw 支持 Anthropic 的提示缓存功能。**仅限 API**；遗留的 Anthropic token 认证不识别缓存设置。

### 配置参数

| 值 | 缓存时长 | 说明 |
|---|---|---|
| `none` | 无缓存 | 禁用提示缓存 |
| `short` | 5 分钟 | API 密钥认证的默认值 |
| `long` | 1 小时 | 延长缓存 |

### 默认行为

使用 Anthropoc API 密钥认证时，OpenClaw 自动为所有 Anthropic 模型应用 `cacheRetention: "short"`（5分钟缓存）。可通过在配置中显式设置 `cacheRetention` 来覆盖。

### 按代理覆盖

使用模型级参数作为基准，然后通过 `agents.list[].params` 覆盖特定代理。

---

## 1M 上下文窗口 (Anthropic beta)

Anthropic 的 1M 上下文窗口需要 beta 资格。在 OpenCl中，通过 `params.context1m: true` 为支持的 Opus/Sonnet 模型启用：

```json5
{
  agents: {
    defaults: {
      models: {
        "anthropic/claude-opus-4-6": {
          params: { context1m: true },
        },
      },
    },
  },
}
```

OpenClaw 将其映射到 Anthropic 请求上的 `anthropic-beta: context-1m-2025-08-07`。

**注意**：Anthropic 目前在使用遗留 Anthropic token 认证（`sk-ant-oat-*`）时拒绝 `context-1m-*` beta 请求。

---

## 故障排除

### 401 错误 / token 突然失效

- Anthropic token 认证可能过期或被撤销
- 迁移到 Anthropic API 密钥

### 未找到提供商 "anthropic" 的 API 密钥

- 认证是**按代理**的。新代理不会继承主代理的密钥
- 重新为该代理运行 onboarding，或在网关主机上配置 API 密钥

### 未找到配置文件 `anthropic:default` 的凭据

- 运行 `openclaw models status` 查看哪个认证配置文件处于活动状态
- 重新运行 onboarding，或为该配置文件路径配置 API 密钥

### 没有可用的认证配置文件（全部冷却中/不可用）

- 检查 `openclaw models status --json` 中的 `auth.unusableProfiles`
- Anthropic 速率限制冷却可以是模型范围的

---

## 相关资源

- [Claude Code CLI 参考](https://code.claude.com/docs/en/cli-reference)
- [Claude Agent SDK 概述](https://platform.claude.com/docs/en/agent-sdk/overview)
- [将 Claude Code 与 Pro 或 Max 计划配合使用](https://support.claude.com/en/articles/11145838-using-claude-code-with-your-pro-or-max-plan)
- [将 Claude Code 与 Team 或 Enterprise 计划配合使用](https://support.anthropic.com/en/articles/11845131-using-claude-code-with-your-team-or-enterprise-plan/)
