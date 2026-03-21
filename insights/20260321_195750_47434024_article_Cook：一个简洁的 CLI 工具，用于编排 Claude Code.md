# Cook - CLI 工具洞察报告

## 基本信息

| 项目 | 内容 |
|------|------|
| **工具名称** | cook |
| **类型** | CLI 工具 |
| **用途** | 编排 Claude Code、Codex 和 OpenCode 的命令行工具 |
| **GitHub** | https://github.com/rjcorwin/cook |
| **npm** | https://www.npmjs.com/package/@let-it-cook/cli |
| **安装方式** | `npm install -g @let-it-cook/cli` |

---

## 核心功能

### 1. 工作单元 (Work)
- 一个 prompt = 一次 agent 调用 = 核心工作单元

### 2. 循环操作符
| 操作符 | 功能 |
|--------|------|
| `xN` | 重复工作 N 次 |
| `review` | 添加 review→gate 循环，质量把关 |
| `ralph` | 任务列表进度管理 |

### 3. 组合操作符
| 操作符 | 功能 |
|--------|------|
| `vN` / `race N` | 并行运行 N 个相同 cook，取最佳结果 |
| `vs` | 两个不同方案并行运行对比 |
| `pick` | 选择一个胜者 |
| `merge` | 合并所有结果 |
| `compare` | 输出对比文档 |

---

## 使用示例

```bash
# review 循环
cook "Implement dark mode" review

# 3 次重复
cook "Implement dark mode" x3

# 3 版本竞速，选最佳
cook "Implement dark mode" v3 "least code"

# 两种方案对比
cook "Auth with JWT" vs "Auth with sessions" pick "best security"
```

---

## 配置

- `cook init` 初始化项目配置
- `COOK.md` - 项目指令和 agent prompt 模板
- `.cook/config.json` - agent/model 默认配置
- `.cook/Dockerfile` - Docker 沙箱依赖
- `.cook/logs/` - 会话日志

### 沙箱模式
- **Agent 模式** (默认): 使用系统级沙箱
- **Docker 模式**: 容器内运行，限制网络访问
- OpenCode 仅支持 Docker 模式

### 速率限制恢复
- 默认自动等待并重试
- 可配置 `pollIntervalMinutes` 和 `maxWaitMinutes`

---

## 洞察总结

1. **编排能力**: cook 是 AI 编码代理的"指挥官"，能协调多个 AI agent 协同工作
2. **质量保障**: 内置 review 和 gate 机制，确保输出质量
3. **并行开发**: 支持多版本竞速、多方案对比，提高开发效率
4. **灵活配置**: 支持自定义 agent、模型、prompt，适应不同场景
5. **隔离执行**: 使用 git worktree 隔离并行任务，避免冲突
