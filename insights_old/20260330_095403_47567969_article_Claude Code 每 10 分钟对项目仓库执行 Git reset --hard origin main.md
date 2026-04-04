# Claude Code 洞察报告

## 基本信息

| 项目 | 内容 |
|------|------|
| **洞察链接** | https://github.com/anthropics/claude-code/issues/40710 |
| **报告生成时间** | 2026-03-30 09:54:03 |
| **原始Issue编号** | #40710 |
| **Issue标题** | Claude Code runs git reset --hard origin/main against project repo every 10 minutes |
| **报告语言** | 中文 |

---

## 问题概述

Claude Code 每10分钟会自动对用户项目仓库执行 `git fetch origin` + `git reset --hard origin/main` 操作，这一行为会静默销毁所有已跟踪文件的未提交更改，仅未跟踪文件得以保留。Git worktree 不受此问题影响。

## 影响范围

- **受影响版本**: Claude Code 2.1.87 (Homebrew cask)
- **操作系统**: macOS 15.4 (Darwin 25.3.0, arm64)
- **问题性质**: 数据丢失 (data-loss)
- **触发条件**: 主工作树中存在未提交的已跟踪文件更改

## 技术分析

### 证据链

1. **Git reflog**: 观察到95+条完全相同的时间间隔记录（600秒），确认为定时器触发
2. **实时复现**: 修改已跟踪文件后，在下一个10分钟周期时文件被静默回滚
3. **fswatch监控**: 捕获到典型的 `git fetch` + `git reset --hard` 操作模式
4. **进程排查**: 确认只有Claude Code进程在相关仓库目录中操作
5. **无外部git进程**: 操作通过程序化方式执行（疑似libgit2），未调用外部git二进制

### 排除的其他原因

- Git hooks - 已排除
- Claude Code用户钩子 - 已排除
- 插件市场更新器 - 已排除
- macOS云同步 - 已排除
- Cron/LaunchAgents - 已排除
- 编辑器 - 已排除

## 临时解决方案

1. **使用Git worktrees** - 经验证不受影响
2. **频繁提交** - 已提交的更改在重置后不受影响

## 相关Issue

- Issue #8072: 代码修订反复被回滚
- Issue #7232: Claude未经授权执行git reset --hard导致数据破坏

## 结论

这是一个严重的数据丢失bug，由于其静默执行特性，难以被发现。建议用户在使用Claude Code时频繁提交更改，或使用git worktrees作为开发环境。
