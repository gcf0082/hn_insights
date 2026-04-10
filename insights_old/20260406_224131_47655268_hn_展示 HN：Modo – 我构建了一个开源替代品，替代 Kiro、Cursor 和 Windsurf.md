# 洞察报告

**洞察链接**: https://news.ycombinator.com/item?id=47655268

## 基本信息

| 项目 | 内容 |
|------|------|
| **标题** | Show HN: Modo – I built an open-source alternative to Kiro, Cursor, and Windsurf |
| **得分** | 77 points |
| **作者** | mohshomis |
| **发布时间** | 14小时前 |
| **评论数** | 17条评论 |

---

## 项目概述

**Modo** 是一个开源的 AI 驱动代码编辑器，作为 Kiro、Cursor 和 Windsurf 的替代方案。该项目构建于 [Void](https://github.com/voideditor/void) 编辑器（VS Code 的分支）之上，采用 MIT 许可证开源。

作者开发 Modo 的动机是：希望在 AI 编码工具中添加一个小功能，但无法找到合适的提交流道，于是决定自己动手构建一个类似的工具。

## 核心功能

### 1. 规范驱动开发（Spec-Driven Development）

大多数 AI 工具采用"提示词 → 代码"的直接路径，Modo 则实现了"提示词 → 需求 → 设计 → 任务 → 代码"的完整工作流。

规范文件保存在 `.modo/specs/<name>/` 目录下，包含三个 Markdown 文件：
- `requirements.md` - 用户故事和验收标准
- `design.md` - 架构设计、组件和数据模型
- `tasks.md` - 实现步骤清单

### 2. 任务代码透镜（Task CodeLens）

在 `tasks.md` 文件中，每个待处理任务都有可点击的"▶ 运行任务"按钮，支持批量执行。

### 3. 引导文件（Steering Files）

Markdown 文档位于 `.modo/steering/` 目录，可将项目规则注入每次 AI 交互中，支持三种包含模式：`always`、`fileMatch` 和 `manual`。

### 4. 代理钩子（Agent Hooks）

JSON 配置文件位于 `.modo/hooks/`，支持在代理生命周期中自动化执行操作，包括10种事件类型和2种操作类型。

### 5. 自动驾驶/监督模式切换

状态栏提供 Autopilot（自动驾驶）和 Supervised（监督模式）切换，直接关联自动批准设置。

### 6. 其他功能

- **并行聊天会话**：多标签页支持各自独立的线程和上下文
- **氛围和规范模式**：Vibe 模式用于自由探索，Spec 模式用于结构化开发
- **子代理**：并行生成独立子任务
- **Powers**：可安装的知识包，捆绑文档、引导文件和 MCP 配置
- **专用资源管理器窗格**：显示规范、代理钩子、引导文件和 Powers
- **命令斜杠**：快速访问各种命令
- **上下文注入**：规范和引导文件自动注入 LLM 系统提示
- **自定义暗色主题**：Modo Dark 主题，青色点缀
- **Companion Character**：Modo 头像伴随回复

## 技术架构

- 基于 Void 编辑器（VS Code 分支）
- 主要使用 TypeScript (95.3%)
- 支持多种 LLM 提供商：Anthropic、OpenAI、 Gemini、Ollama、Mistral、Groq、OpenRouter

## 社区反馈

评论区的讨论主要集中在：

1. **命名争议**：Modo 这个名字与已停产的 DCC 软件 Modo 重复，可能引发混淆
2. **多分支工作流**：用户关心子代理是否能在多个分支上同时工作（推荐使用 git worktrees）
3. **可视化演示需求**：用户希望看到更多视觉演示而非纯文字说明
4. **与现有工具的比较**：与 CLAUDE.md 等配置文件方式的对比
5. **可观测性**：建议添加会话回放或会话探索功能

## 快速开始

```bash
git clone https://github.com/mohshomis/modo.git
cd modo
npm install
npm run buildreact
npm run watch
./scripts/code.sh
```

首次启动时需要连接模型提供商，Gemini 免费层是最快的入门方式。

## 总结

Modo 代表了 AI IDE 领域的一个重要尝试——通过开源方式实现与商业竞品（如 Cursor、Windsurf）相似的功能。其规范驱动的工作流和任务管理机制为 AI 辅助编程提供了更加结构化的方法。尽管项目命名存在一些争议，但其技术实现和功能设计值得关注。
