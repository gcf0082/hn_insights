# Libretto 项目洞察报告

**洞察链接**: https://github.com/saffron-health/libretto  
**项目名称**: Libretto  
**项目类型**: AI 浏览器自动化工具包  
**许可证**: MIT  
**编程语言**: TypeScript (92.8%), JavaScript (4.2%), Shell (1.8%)  
**星标数**: 146  
**分支数**: 8  
**提交数**: 1,155

## 项目简介

Libretto 是由 Saffron Health 团队开发的 AI 工具包，用于构建和维护浏览器自动化集成。该工具为编程代理提供实时浏览器和高效的 CLI，能够检查实时页面、捕获网络流量、录制用户操作并将其重放为自动化脚本，以及针对真实网站调试故障工作流。

Saffron Health 主要将其用于维护医疗软件（常见 EHR 系统）的浏览器集成，后开源供其他团队使用。

## 核心功能

### 1. 实时页面检查
- 以最小的上下文开销检查实时页面
- 捕获屏幕截图和 HTML 进行分析

### 2. 网络流量捕获
- 捕获网络请求以逆向工程网站 API
- 将浏览器自动化转换为直接网络请求（更快速、更可靠）

### 3. 用户操作录制
- 记录用户操作并重放为 Playwright 自动化脚本
- 支持交互式脚本构建

### 4. 故障调试
- 自主重现失败
- 在任意点暂停工作流
- 检查实时页面并修复问题

## 使用场景

### 单次脚本生成
代理会自动打开浏览器窗口，让用户登录网站，然后自动开始探索和执行任务。

### 交互式脚本构建
用户执行工作流后，可让代理将操作转换为 Playwright 脚本，支持输入参数化。

### 转换为网络请求
将浏览器自动化脚本转换为直接 API 调用，提高速度和可靠性。

### 修复损坏的集成
代理可以自行重现失败、暂停、检查并修复问题。

## 安装配置

```bash
npm install libretto
npx libretto setup      # 首次安装配置
npx libretto status    # 检查状态
```

支持配置 OpenAI、Anthropic、Google Gemini/Vertex 等模型。

## CLI 命令

| 命令 | 说明 |
|------|------|
| `libretto open <url>` | 启动浏览器打开 URL |
| `libretto snapshot` | 捕获截图和 HTML 并分析 |
| `libretto exec <code>` | 执行 Playwright 代码 |
| `libretto run <file>` | 运行工作流文件 |
| `libretto save <domain>` | 保存浏览器会话 |
| `libretto close` | 关闭浏览器 |

## 项目结构

```
packages/libretto/src/
├── cli/          # CLI 命令
├── runtime/      # 浏览器运行时
├── shared/      # 共享工具
└── skills/      # 技能定义
```

## 技术特点

- **多平台支持**: OpenAI / Anthropic / Gemini / Vertex
- **会话管理**: 每个会话独立存储（状态、日志、网络请求、操作）
- **配置灵活**: 支持自定义视口大小和 AI 模型
- **Profiles**: 保存认证状态（cookies, localStorage）供复用

## 适用人群

- 需要维护浏览器自动化的开发团队
- 需要逆向工程网站 API 的工程师
- 希望将 UI 自动化转换为 API 调用的开发者
- 医疗软件集成开发者

## 相关链接

- 官网: https://libretto.sh
- 文档: https://libretto.sh/docs
- Discord: https://discord.gg/NYrG56hVDt