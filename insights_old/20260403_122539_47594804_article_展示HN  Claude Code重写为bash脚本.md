# 洞察报告：claude-sh

## 基本信息

| 项目 | 内容 |
|------|------|
| **洞察链接** | https://github.com/jdcodes1/claude-sh |
| **项目名称** | claude-sh |
| **项目描述** | Claude Code rewritten as a bash script. ~1500 lines, zero npm packages. Just curl + jq. |
| **作者** | jdcodes1 (Joey Dafforn) |
| **编程语言** | Shell (100%) |
| **星标数** | 88 |
| **观察者** | 2 |
| **分支** | 15 |
| **许可证** | MIT |

---

## 项目概述

claude-sh 是一个用纯 Bash 脚本重写的 Claude Code 实现。整个项目仅约 1500 行代码，不依赖任何 npm 包，只需要 `curl` 和 `jq` 两个工具即可运行。相比之下，原始的 Claude Code 拥有约 38 万行 TypeScript 代码和 266 个 npm 依赖。

---

## 核心特性

### 功能特性
- **实时流式输出** - 通过 FIFO 管道实现，文本在 Claude 生成时即时显示
- **6个内置工具** - Bash、Read、Edit、Write、Glob、Grep
- **工具链调用** - 每轮最多支持 25 次工具调用
- **权限提示** - 运行非安全命令前会询问用户（y/n/a）
- **CLAUDE.md 加载** - 从目录树向上读取项目指令文件
- **Git 上下文感知** - 自动获取分支、状态和最近提交信息
- **会话保存/恢复** - 退出时自动保存，支持通过 `--resume <id>` 恢复
- **指数退避重试** - 遇到 429/529 限流时自动重试
- **成本跟踪** - 显示每轮和会话的总费用
- **动态加载动画** - 包含原始风格的加载动画动词
- **斜杠命令** - `/help`, `/cost`, `/model`, `/clear`, `/save`, `/resume`, `/commit`, `/diff`, `/quit`
- **管道模式** - 支持 `echo "explain this" | ./claude.sh`

### 安装依赖
- `curl` (必需)
- `jq` (必需)
- `rg` (可选，ripgrep 用于更好的搜索)
- `python3` (可选，用于 Edit 工具)

---

## 架构设计

```
claude.sh          # 主 REPL 循环，斜杠命令，process_turn()
lib/
  api.sh           # Anthropic API 客户端，通过 FIFO 实现 SSE 流式传输，重试机制
  json.sh          # 消息构建，会话持久化，CLAUDE.md 加载，Git 上下文
  tools.sh         # 6 个工具实现 + 权限系统
  tui.sh           # ANSI 颜色，加载动画，显示辅助函数
```

### 工作流程
1. 读取用户输入
2. 使用 `jq` 构建 JSON 请求（消息、工具、系统提示词）
3. 通过 `curl` 和 FIFO 管道流式传输响应
4. 逐行解析 SSE 事件，实时打印文本增量
5. 到达 tool_use 块时执行工具
6. 将工具结果作为消息反馈
7. 循环直到 Claude 停止调用工具

---

## 性能对比

| 指标 | claude.sh | Claude Code (TypeScript) |
|------|-----------|--------------------------|
| 代码行数 | ~1,500 | ~380,000 |
| 依赖项 | curl, jq | 266 个 npm 包 |
| 二进制大小 | 0 (脚本) | ~200MB node_modules |
| 启动时间 | 即时 | ~500ms |

---

## 使用方法

### 基本用法
```bash
git clone https://github.com/jdcodes1/claude.sh.git
cd claude.sh
chmod +x claude.sh
export ANTHROPIC_API_KEY="sk-ant-..."
./claude.sh
```

### 环境变量

| 变量 | 默认值 | 说明 |
|------|--------|------|
| `ANTHROPIC_API_KEY` | (必填) | 你的 Anthropic API 密钥 |
| `CLAUDE_MODEL` | claude-sonnet-4-20250514 | 使用的模型 |
| `CLAUDE_MAX_TOKENS` | 8192 | 最大输出 token 数 |
| `ANTHROPIC_API_URL` | https://api.anthropic.com | API 基础 URL |
| `CLAUDE_SH_PERMISSIONS` | ask | 权限模式：ask, allow, deny |

### 恢复会话

```bash
# 列出保存的会话
./claude.sh
> /resume

# 按编号恢复
> /resume 1

# 从命令行恢复
./claude.sh --resume 20240101-120000-12345
```

---

## 总结

claude-sh 是一个极具创新性的项目，它证明了即使使用简单的 Shell 脚本工具，也能实现复杂的 AI 交互功能。该项目以其极简的依赖、快速的启动时间和轻量的代码量著称，是了解和学习 AI CLI 工具实现原理的优秀案例。对于追求极致轻量化和快速响应的开发者来说，claude-sh 是一个值得尝试的替代方案。