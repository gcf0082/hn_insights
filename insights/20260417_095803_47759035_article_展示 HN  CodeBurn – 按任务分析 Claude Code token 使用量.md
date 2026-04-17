**洞察链接**: https://github.com/AgentSeal/codeburn

**项目名称**: CodeBurn
**项目类型**: 开源 CLI 工具
**主要语言**: TypeScript
**GitHub 星级**: 2.3k
**许可证**: MIT

---

# CodeBurn 项目洞察报告

## 项目概述

CodeBurn 是一款用于追踪 AI 编程工具 token 消耗的开源工具。它通过交互式终端界面（TUI）展示 Claude Code、Codex、Cursor、OpenCode、Pi 和 GitHub Copilot 的使用成本和效率分析。

## 核心功能

### 1. 多提供商支持
支持六种 AI 编码工具：Claude Code、Claude Desktop、Codex、Cursor、OpenCode、Pi、GitHub Copilot。采用插件化架构，可轻松添加新提供商。

### 2. 交互式 TUI 仪表板
- 按任务类型、工具、模型、MCP 服务器和项目分类显示消耗
- 梯度图表、响应式面板、键盘导航
- 支持今日/7天/30天/本月/全部时段的视图切换
- 显示平均每会话成本和五个最昂贵会话

### 3. 任务分类（13类）
根据工具使用模式和用户消息关键词自动分类：编码、调试、功能开发、重构、测试、探索、规划、委托、Git操作、构建/部署、脑暴、对话、通用。

### 4. 一次成功率追踪
分析编辑/测试/修复重试循环，计算各类任务的一次成功率，帮助识别 AI 效率问题。

### 5. 优化建议功能
`codeburn optimize` 命令可扫描会话和配置，检测常见浪费模式并提供修复建议：
- 重复读取文件
- 低读取/编辑比
- 缺少 .claudeignore
- 未使用的 MCP 服务器
- 幽灵代理和技能

### 6. 数据导出
支持 CSV 和 JSON 格式导出今日、7天、30天数据。

### 7. 菜单栏小部件
支持 macOS SwiftBar 菜单栏显示今日消耗。

## 技术架构

### 数据读取方式
- **Claude Code**: 读取 `~/.claude/projects/` 中的 JSONL 会话文件
- **Codex**: 读取 `~/.codex/sessions/` 中的 JSONL 文件
- **Cursor**: 解析 SQLite 数据库 (`state.vscdb`)
- **OpenCode**: 解析 `~/.local/share/opencode/` 中的 SQLite 数据库
- **Pi**: 读取 `~/.pi/agent/sessions/` 中的 JSONL 文件
- **GitHub Copilot**: 读取 `~/.copilot/session-state/` 中的会话状态

### 定价数据
使用 LiteLLM 定价数据，自动缓存 24 小时。自动处理输入、输出、缓存读写和网络搜索成本。支持 162 种货币转换（通过 Frankfurter API）。

## 安装和使用

```bash
npm install -g codeburn
codeburn                    # 交互式仪表板
codeburn today              # 今日消耗
codeburn optimize            # 优化建议
codeburn status             # 紧凑状态显示
codeburn export             # CSV 导出
```

## 适用场景

- 开发团队监控 AI 编程工具成本
- 个人开发者优化 AI 使用效率
- 识别浪费模式和配置问题
- 成本分析和预算规划

## 总结

CodeBurn 是一个功能全面且免费的 AI 编程 token 追踪工具，特别适合需要精细化管理 AI 开发成本的团队和个人开发者。其无需 API 密钥、直接读取本地会话数据的设计使得部署和使用都非常简便。