# Claude Code Routines 洞察报告

## 基本信息

- **洞察链接**: https://code.claude.com/docs/en/routines
- **生成时间**: 2026-04-15 03:03:36
- **文章ID**: 47768133
- **主题**: Claude Code 自动化任务功能详解

---

## 一、什么是 Routines？

Routines（自动化任务）是 Claude Code 的一种自动化功能，允许用户创建保存的配置（包括提示词、一个或多个代码仓库、以及连接器），然后自动执行。这些任务在 Anthropic 管理的云基础设施上运行，因此即使关闭笔记本电脑，任务也能继续执行。

Routines 目前处于研究预览阶段，行为、限制和 API 表面可能会发生变化。

### 核心特性

- **自主运行**: Routines 作为完整的 Claude Code 云会话运行，无权限模式选择器，执行过程中无批准提示
- **多种触发方式**: 支持定时、API 调用、GitHub 事件三种触发方式
- **灵活组合**: 单个 Routine 可以组合多种触发器

---

## 二、触发器类型详解

### 1. 定时触发（Schedule）

定时触发按重复周期运行 Routine，例如每小时、每天、每周或工作日。

**配置要点：**
- 时间以本地时区输入，自动转换，因此无论云基础设施位于何处，Routine 都在指定的挂钟时间运行
- 由于错开（stagger），运行可能比预定时间晚几分钟
- 最小间隔为一小时

### 2. API 触发

API 触发为 Routine 提供专用的 HTTP 端点。通过向端点发送带有 Routine 承载令牌的 POST 请求来启动新会话。

**使用场景：**
- 集成到告警系统
- 部署流水线触发
- 内部工具调用

**调用示例：**
```bash
curl -X POST https://api.anthropic.com/v1/claude_code/routines/trig_01ABCDEFGHJKLMNOPQRSTUVW/fire \
  -H "Authorization: Bearer sk-ant-oat01-xxxxx" \
  -H "anthropic-beta: experimental-cc-routine-2026-04-01" \
  -H "anthropic-version: 2023-06-01" \
  -H "Content-Type: application/json" \
  -d '{"text": "Sentry alert SEN-4521 fired in prod."}'
```

### 3. GitHub 触发

GitHub 触发在连接仓库上发生匹配事件时自动启动新会话。

**支持的事件类型：**
- Pull Request（打开、关闭、分配、标签等）
- Push（提交推送到分支）
- Issues（问题创建、编辑、关闭等）
- Release（发布创建、发布等）
- Workflow run（GitHub Actions 工作流运行）
- 等等

**过滤选项：**
- 作者、标题、正文
- 基础分支、头部分支
- 标签、是否为草稿、是否已合并
- 是否来自 Fork

---

## 三、典型使用场景

### 1. 待办事项维护
每周工作日晚运行，针对问题跟踪器运行 Routine。读取自上次运行以来打开的问题，根据引用的代码区域应用标签、分配负责人，并将摘要发布到 Slack。

### 2. 告警分类
监控工具在错误阈值被触发时调用 Routine 的 API 端点，将告警正文作为 `text` 传递。Routine 拉取堆栈跟踪，与仓库中最近的提交关联，并打开带有建议修复的草稿 PR。

### 3. 自定义代码审查
GitHub 触发在 `pull_request.opened` 时运行。Routine 应用团队自己的审查清单，为安全、性能和样式问题留下内联评论，并添加摘要评论。

### 4. 部署验证
CD 流水线在每次生产部署后调用 Routine 的 API 端点。Routine 对新构建运行冒烟检查，扫描错误日志以查找回归，并在部署窗口关闭前发布通过或不通过的消息。

### 5. 文档漂移
定时触发每周运行。Routine 扫描自上次运行以来合并的 PR，标记引用已更改 API 的文档，并针对文档仓库打开更新 PR 以供编辑审核。

### 6. 库移植
GitHub 触发在 `pull_request.closed` 时运行，过滤到合并的 PR。Routine 将更改移植到另一种语言的并行 SDK 并打开匹配的 PR。

---

## 四、创建和管理

### 创建方式

1. **网页创建**: 访问 claude.ai/code/routines 点击 "New routine"
2. **CLI 创建**: 运行 `/schedule` 命令，可传递描述如 `/schedule daily PR review at 9am`
3. **桌面应用创建**: 打开 Schedule 页面，选择 "New remote task"

### 管理功能

- **查看运行**: 点击任何运行作为完整会话查看
- **立即运行**: 点击 "Run now" 立即启动运行
- **暂停/恢复**: 使用开关暂停或恢复计划
- **编辑**: 修改名称、提示词、仓库、环境、连接器或触发器
- **删除**: 删除 Routine，历史上创建的会话仍保留在会话列表中

---

## 五、使用限制

Routines 消耗订阅使用配额的方式与交互式会话相同。除了标准订阅限紫外，Routines 还有每日运行次数上限。可在 claude.ai/code/routines 或 claude.ai/settings/usage 查看当前消耗和剩余每日运行次数。

当 Routine 达到每日上限或订阅使用限制时：
- 启用额外使用的组织可以继续按需付费运行 Routine
- 未启用额外使用的情况下，额外运行被拒绝直到窗口重置

---

## 六、相关资源

- `/loop` 和会话内调度：开放 CLI 会话内的本地任务调度
- Desktop scheduled tasks：在本地机器上运行并可访问本地文件的本地计划任务
- Cloud environment：为云会话配置运行时环境
- MCP connectors：连接 Slack、Linear、Google Drive 等外部服务
- GitHub Actions：在 CI 管道中根据仓库事件运行 Claude