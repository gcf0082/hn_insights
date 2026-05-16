# 代码审查洞察报告

**链接**: https://github.com/adamjgmiller/adamsreview

**项目名称**: adamsreview
**作者**: adamjgmiller
**GitHub 统计**: 106 Stars | 3 Forks | 226 Commits
**编程语言**: Shell 72.2% | Python 27.8%
**许可证**: MIT

---

## 项目概述

adamsreview 是一个专为 Claude Code 打造的多阶段代码审查管道，通过并行子代理检测、验证通道、持久化 JSON 状态和自动修复循环来实现深度代码审查。在作者的 PR 实践中，该工具相比 Claude Code 内置的 `/review`、`/ultrareview`、CodeRabbit、Greptile 和 Codex 内置审查能发现更多真实 Bug，同时产生更少的误报。

---

## 核心功能

### 六大命令

1. **`/adamsreview:review`** — 多镜头代码审查，最多 7 个并行子代理镜头（正确性、安全性、UX 等）。通过去重通道和廉价→深度验证门控，可选添加 Opus 跨切面审查。`--ensemble` 模式额外集成 Codex CLI 和 PR 机器人评论抓取。

2. **`/adamsreview:codex-review`** — Codex CLI 同级审查，与下游所有命令完全兼容。通过 `--effort low|medium|high|xhigh` 调节成本，默认 `high`。

3. **`/adamsreview:add`** — 注入外部发现的成果（如 `/ultrareview`、Opus 一览、同事注释），与现有审查结果去重后验证合并。

4. **`/adamsreview:walkthrough`** — 交互式引导修复流程，逐个处理需要人工判断的问题，通过 `AskUserQuestion` UI 界面引导，自动修复提议批量确认后可一键执行。

5. **`/adamsreview:fix`** — 自动修复循环，并行分发修复子代理，用 Opus 重新审查，回滚任何回归问题，然后提交存活的修复（默认合并为一次提交）。

6. **`/adamsreview:promote`** — 人工覆盖，单个发现标记为可自动修复，绕过通道过滤和分数阈值。

### 推荐工作流

1. 审查：`/adamsreview:review` 或 `--ensemble` 模式
2. 添加：（可选）注入外部审查发现
3. 引导：（可选）交互式处理高置信度发现
4. 修复：`/adamsreview:fix` 应用所有自动修复

---

## 技术架构

### 目录结构

- `commands/` — 命令文件（review.md, codex-review.md, add.md, walkthrough.md, fix.md, promote.md）
- `fragments/` — 共享阶段片段和提示引用
- `bin/` — 辅助脚本（artifact-patch.py, artifact-render.py 等），插件运行时自动添加到 `$PATH`
- `docs/` — 状态/门控文档、管道文档、帮助脚本清单
- `hooks/` — SessionStart 注册和依赖检查
- `scripts/` — 开发运行脚本

### 依赖项

| 工具 | 版本 | 用途 |
|------|------|------|
| `uv` | 0.7+ | Python 脚本执行（PEP 723 inline-script） |
| `bash` | 3.2+ | Shell 辅助脚本（macOS 默认版本兼容） |
| `jq` | 1.6+ | JSON 处理 |
| `gh` | 2.x | PR 评论发布/抓取 |
| `git` | 2.x | 版本控制 |

---

## 技术亮点

### 状态管理

- 审查状态存储在 `~/.adams-reviews/<repo-slug>/<branch>/<review_id>/`
- 持久化 JSON 状态支持步骤间跨度数天或数周
- 避免了 `~/.claude/` 下的敏感文件权限提示问题

### Token 计数

- **子代理 Token**：从 per-review `tokens.jsonl` 日志汇总，精确统计
- **编排器 Token**：从会话转录本扫描，可选启用，需 macOS Full Disk Access

### 修复验证机制

- Phase 7.5 展示所有剩余自动修复提议（轻通道/手动/报告发现）
- Phase 9 验证每组修复结果，回归被自动回滚
- 支持粒度提交模式（`--granular-commits`）

---

## 版本状态

**当前版本**: v0.4.0（auto-fix-hint 功能）
- Phase 5.5 + Phase 7.5 + Step 4.5
- 所有六个命令已发布并日常使用
- v0.3.0 引入 `/adamsreview:codex-review`

---

## 安装方式

```bash
# Claude Code 中安装
/plugin marketplace add adamjgmiller/adamsreview
/plugin install adamsreview@adamsreview

# 本地克隆安装
/plugin marketplace add /path/to/adamsreview
/plugin install adamsreview@adamsreview
```

---

## 总结

adamsreview 代表了 AI 辅助代码审查的成熟实践，通过多镜头并行检测、智能验证门控和自动化修复循环，显著提升了代码审查的质量和效率。其持久化状态管理、回归检测和可选的 Codex 集成使其成为 Claude Code 用户的强大工具。