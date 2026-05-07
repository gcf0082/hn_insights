# 洞察报告：deepclaude

## 基本信息

- **洞察链接**: https://github.com/aattaran/deepclaude
- **项目名称**: deepclaude
- **作者**: aattaran
- **星标数**: 139
- **分支**: main
- **许可证**: MIT
- **主要语言**: JavaScript (43.2%), PowerShell (30.7%), Shell (26.1%)

## 项目概述

deepclaude 是一个开源工具，允许用户使用 Claude Code 的自主代理循环，但将底层 AI 模型从 Anthropic Claude 替换为 DeepSeek V4 Pro、OpenRouter 或任何 Anthropic 兼容的后端。项目声称可以在保持相同用户体验的同时，成本降低约 17 倍。

## 核心功能

### 1. 成本对比

| 使用级别 | Anthropic Max | deepclaude (DeepSeek) | 节省 |
|---------|---------------|----------------------|------|
| 轻度 (10天/月) | $200/月 (封顶) | ~$20/月 | 90% |
| 重度 (25天/月) | $200/月 (封顶) | ~$50/月 | 75% |
| 自动循环 | $200/月 (封顶) | ~$80/月 | 60% |

DeepSeek 的自动上下文缓存功能使代理循环极便宜——首次请求后，系统提示和文件上下文的缓存价格为 $0.004/M（对比未缓存的 $0.44/M）。

### 2. 支持的后端

| 后端 | 标志 | 输入/M | 输出/M | 服务器 | 备注 |
|------|------|--------|--------|--------|------|
| DeepSeek (默认) | `--backend ds` | $0.44 | $0.87 | 中国 | 自动上下文缓存 (重复请求便宜 120 倍) |
| OpenRouter | `--backend or` | $0.44 | $0.87 | 美国 | 最便宜，美国/欧盟延迟最低 |
| Fireworks AI | `--backend fw` | $1.74 | $3.48 | 美国 | 推理最快 |
| Anthropic | `--backend anthropic` | $3.00 | $15.00 | 美国 | 原始 Claude Opus (复杂问题) |

### 3. 工作原理

deepclaude 通过设置环境变量来重定向 Claude Code 的 API 调用：

- `ANTHROPIC_BASE_URL`: API 端点
- `ANTHROPIC_AUTH_TOKEN`: API 密钥
- `ANTHROPIC_DEFAULT_OPUS_MODEL`: Opus 级任务的模型名称
- `ANTHROPIC_DEFAULT_SONNET_MODEL`: Sonnet 级任务的模型名称
- `ANTHROPIC_DEFAULT_HAIKU_MODEL`: Haiku 级 (子代理) 的模型名称

### 4. 远程控制功能

支持通过 `--remote` 参数在浏览器中打开 Claude Code 会话，使用 DeepSeek 作为大脑：

```bash
deepclaude --remote                # 远程控制 + DeepSeek
deepclaude --remote -b or          # 远程控制 + OpenRouter
deepclaude --remote -b anthropic   # 远程控制 + Anthropic
```

### 5. 实时切换

支持在会话中实时切换 Anthropic 和 DeepSeek，无需重启。通过设置 slash 命令（`/deepseek` 或 `/anthropic`）实现。

## 支持的功能

- 文件读取、写入、编辑 (Read/Write/Edit 工具)
- Bash/PowerShell 执行
- Glob 和 Grep 搜索
- 多步自主工具循环
- 子代理生成
- Git 操作
- 项目初始化 (`/init`)
- 思考模式 (默认启用)

## 不支持或降级的功能

| 功能 | 原因 |
|------|------|
| 图像/视觉输入 | DeepSeek 的 Anthropic 端点不支持图像 |
| 并行工具使用 | 已禁用 — 工具一次执行一个 |
| MCP 服务器工具 | 不支持通过兼容层 |
| 提示缓存节省 | DeepSeek 有自己的缓存 (自动)，但忽略 Anthropic 的 `cache_control` |

## 智能差异

- **常规任务** (80% 的工作): DeepSeek V4 Pro 与 Claude Opus 相当
- **复杂推理** (20%): Claude Opus 更强 — 使用 `--backend anthropic` 切换

## 快速开始

1. 获取 DeepSeek API 密钥：在 platform.deepseek.com 注册，充值 $5
2. 设置环境变量
3. 安装脚本 (Windows: deepclaude.ps1, macOS/Linux: deepclaude.sh)
4. 使用 `deepclaude` 命令启动

## VS Code / Cursor 集成

支持添加终端配置文件以便从 IDE 启动 deepclaude。

## 适用场景

- 需要长期使用 Claude Code 进行代码开发的开发者
- 对成本敏感的用户
- 需要同时使用多个 AI 后端的用户
- 需要远程控制功能的用户

## 注意事项

- 远程控制功能需要 Claude Code 已登录且拥有 claude.ai 订阅
- 需要 Node.js 18+ 运行代理
- 图像处理功能不可用