# Marky 项目洞察报告

**洞察链接**: https://github.com/GRVYDEV/marky

**生成时间**: 2026-04-17 09:58:03

**基本信息系统**

- **项目名称**: GRVYDEV/marky
- **项目描述**: A lightweight easy to use markdown viewer（一个轻量级、易用的 Markdown 查看器）
- **星标数**: 52
- **分支数**: 1 (main)
- **提交数**: 28
- **编程语言占比**: TypeScript 68.6%, Rust 23.5%, CSS 6.1%, Shell 1.6%

## 项目概述

Marky 是一款专为 macOS 设计的原生 Markdown 查看器，由 Tauri v2、React 和 markdown-it 构建。该项目的核心设计理念是提供一个快速、简洁的工具，让用户能够从终端直接打开 `.md` 文件并获得美观的即时渲染效果。

## 核心功能特点

### 1. CLI 优先设计
Marky 完全围绕命令行体验设计，支持以下操作方式：
- `marky FILENAME` - 打开单个文件
- `marky FOLDER` - 打开文件夹作为持久工作区（类似 Obsidian 风格）

### 2. 实时重载
文件在磁盘上发生变化时（例如通过编辑器、Claude 等工具修改），视图会即时更新，非常适合查看 Claude 生成的计划、文档或正在编写的笔记。

### 3. 文件夹工作区
支持将文件夹添加为持久工作区，类似于 Obsidian 的侧边栏形式，关闭应用后会自动恢复上次会话。

### 4. 命令面板
Cmd+K 快捷键可以调用模糊搜索功能，基于 nucleo 引擎实现跨所有打开文件夹的文件搜索。

### 5. 丰富的 Markdown 渲染支持
- **语法高亮**: 使用 Shiki 和 VS Code 主题实现精准美观的代码块渲染
- **数学公式**: KaTeX 支持 `$inline$` 和 `$$display$$` 数学公式
- **Mermaid 图表**: 支持用 fence 语法创建 Mermaid 图表并渲染为 SVG
- **GFM 特性**: 支持表格、任务列表、删除线、自动链接、脚注等 GitHub 风格 Markdown 特性

### 6. 主题支持
- 跟随系统偏好自动切换浅色/深色主题
- 也支持手动切换主题

### 7. 安全渲染
所有 HTML 内容都经过 DOMPurify 清理，安全查看不可信的 Markdown 内容。

### 8. 轻量高效
采用原生 webview 技术（非 Electron），生产环境的 `.dmg` 文件仅 15MB 左右。

## 技术架构分析

### 技术栈组合

| 层次 | 技术选型 |
|------|----------|
| 桌面外壳 | Tauri v2 |
| 前端框架 | React + TypeScript + Vite |
| Markdown 解析 | markdown-it |
| 语法高亮 | Shiki |
| 数学公式 | KaTeX |
| 图表渲染 | Mermaid |
| 模糊搜索 | nucleo |
| UI 组件 | shadcn/ui |
| 样式方案 | Tailwind CSS |
| 文件监控 | notify (Rust crate) |

### 项目结构

```
src-tauri/       Rust 后端 — CLI、文件 I/O、文件监控、文件夹注册、模糊搜索
src/             React 前端 — Markdown 处理流水线、UI 组件、主题
src/components/  应用组件（Viewer、Sidebar、CommandPalette 等）
src/components/ui/  shadcn/ui 基础组件
src/lib/         核心逻辑（markdown-it 配置、Shiki、Tauri IPC 封装）
src/styles/      Tailwind 基础样式 + Markdown 正文样式
scripts/         安装辅助脚本
```

## 安装和使用

### Homebrew 安装（临时方案）
```bash
brew tap GRVYDEV/tap
brew install --cask GRVYDEV/tap/marky
xattr -cr /Applications/Marky.app  # 临时处理未签名问题
```

### 源码构建
```bash
git clone https://github.com/GRVYDEV/marky.git
cd marky
pnpm install
pnpm tauri build
./scripts/install-cli.sh
```

### 快捷键一览

| 快捷键 | 功能 |
|--------|------|
| Cmd+K | 命令面板（模糊文件搜索） |
| Cmd+O | 打开文件 |
| Cmd+Shift+O | 添加文件夹 |
| Cmd+F | 页面内搜索 |

## 发展路线图

项目未来计划包含以下特性：

1. **多平台支持** - 目前仅支持 macOS ARM，将扩展到 x86 macOS 和 Linux
2. **内置 AI 聊天** - 在 Markdown 文档内直接与 Claude Code 或 Codex 对话
3. **Git 差异审查** - 无需离开应用即可查看和审查本地 git 差异

## 项目优缺点分析

### 优势

1. **轻量高效** - 相比 Electron 应用，体积仅 15MB，减少系统资源占用
2. **实时监控** - 文件变化即时反映，提升工作流效率
3. **功能全面** - 支持数学公式、图表、代码高亮等高级 Markdown 特性
4. **安全性** - DOMPurify 清理确保安全渲染不可信内容
5. **现代化架构** - 采用 Tauri v2 + React 的新一代跨平台桌面应用技术栈

### 潜在挑战

1. **平台限制** - 目前仅支持 macOS，Linux 和 Windows 用户无法使用
2. **签名问题** - 应用当前未经过 Apple 开发者签名，需要手动执行 xattr 处理
3. **功能限制** - 作为单纯的 Markdown 查看器，缺乏编辑功能
4. **社区规模** - 仅有 52 星标，社区参与度和文档可能不够完善

## 适用场景建议

Marky 特别适合以下用户群体：

1. **开发者** - 需要快速查看代码文档、README 文件的技术人员
2. **Markdown 写作者** - 在写作过程中需要实时预览效果的作者
3. **AI 工具用户** - 使用 Claude 等 AI 工具生成文档，需要即时查看结果的开发者
4. **文档维护者** - 需要管理和浏览多个文档文件夹的团队成员

## 总结

Marky 是一款设计精良的 macOS 原生 Markdown 查看器，通过 Tauri v2 和 React 的现代化技术组合实现了轻量且功能丰富的文档查看体验其实时重载功能和多格式支持使其成为技术文档浏览的理想选择，尤其是在配合 AI 工具使用时。不过，目前仅支持 macOS 平台的限制意味着其他操作系统用户需要等待后续版本更新。