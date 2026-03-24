# ProofShot 洞察报告

## 基本信息

- **洞察链接**: https://proofshot.argil.io/
- **项目名称**: ProofShot
- **许可证**: MIT License (开源)
- **获取方式**: npm install -g proofshot

## 项目概述

ProofShot 是一个为 AI 编码代理提供可视化验证的开源工具。当 AI 代理完成代码编写后，ProofShot 可以通过视频录制、错误日志和证据工件来证明其工作成果。

## 核心功能

### 1. 视频录制
完整的浏览器会话录制，支持自动去除空闲时间。开发者可以精确看到代理执行的操作，而不是等待的空闲时间。

### 2. 错误检测
捕获浏览器控制台错误，并使用模式匹配扫描服务器日志，支持 JavaScript、Python、Go、Rust 等多种编程语言。

### 3. 交互式时间线
独立的 HTML 查看器，包含同步视频、截图和交互式操作时间线，并带有元素标签。

### 4. PR 就绪的证据
生成 SUMMARY.md 和格式化输出，可直接粘贴到 Pull Request 中。支持与基线的视觉差异对比。

## 工作流程

ProofShot 通过三个命令实现完整验证：

1. **启动**: 启动开发服务器，打开无头浏览器并开始录制视频
   ```
   proofshot start --run "npm run dev"
   ```

2. **测试**: AI 代理执行导航、点击、填写表单和截图等操作，每个操作都会被记录
   ```
   proofshot exec navigate "http://localhost:3000"
   proofshot exec screenshot "homepage"
   ```

3. **停止**: 收集错误、停止录制、去除空闲时间并生成证据工件
   ```
   proofshot stop
   ```

## 兼容性与集成

ProofShot 与 AI 编码代理无关，可在以下工具中使用：

- Claude Code
- Cursor
- Codex
- Gemini CLI
- Windsurf
- 任何 MCP 兼容的代理

只需安装一次，之后每个代理都会自动获得可视化验证功能。

## 查看器功能

每个会话都可以完整回顾：
- 与操作时间线同步的视频播放
- 截图
- 元素标签
- 所有内容打包在一个独立的 HTML 文件中

## 总结

ProofShot 为 AI 编码代理提供了可靠的验证机制，通过视频录制、错误捕获和交互式时间线，让开发者能够验证 AI 生成的代码是否符合预期。其开源性质和与多种代理的兼容性使其成为 AI 开发工作流中的重要工具。