# 洞察报告：browser-use/browser-harness

## 基本信息

| 项目 | 内容 |
|------|------|
| **洞察链接** | https://github.com/browser-use/browser-harness |
| **项目名称** | Browser Harness |
| **作者** | browser-use |
| **GitHub Stars** | 6.4k |
| **GitHub Forks** | 561 |
| **编程语言** | Python 100% |
| **许可证** | MIT |
| **提交次数** | 158 |

## 项目概述

Browser Harness 是一个极其简洁的**自愈式（self-healing）工具**，为 LLM 提供完成任何浏览器任务的完整自由度。它直接构建在 CDP（Chrome DevTools Protocol）之上，通过 WebSocket 连接到 Chrome，没有任何中间层框架。

## 核心特性

### 1. 自愈机制
当 LLM 在执行任务时发现缺少某个功能（如上传文件），它会：
- 在 `helpers.py` 中直接编写缺失的函数
- 无需重启，任务继续执行
- 整个过程完全自动化

### 2. 极简架构
- **总代码量**：约 592 行 Python 代码
- **核心文件**：
  - `install.md` - 首次安装配置
  - `SKILL.md` - 日常使用指南
  - `run.py` (~36 行) - 运行器
  - `helpers.py` (~195 行) - 工具函数集
  - `admin.py` + `daemon.py` (~361 行) - CDP WebSocket 桥接

### 3. 免登录远程浏览器
- 提供免费套餐：3 个并发浏览器、代理、验证码识别
- 支持云端部署和子代理场景

### 4. Domain Skills 技能系统
- 预置多种网站技能（GitHub、LinkedIn、Amazon 等）
- LLM 会自动生成新技能文件并共享给社区

## 工作原理

```
● agent: 想要上传文件
│
● helpers.py → upload_file() 不存在
│
● agent 编辑 harness 并编写函数    helpers.py  192 → 199 行
│                                     + upload_file()
✓ 文件上传成功
```

## 技术亮点

1. **无框架约束**：直接使用 CDP，无 Playwright/Selenium 等中间层
2. **实时编辑**：LLM 可在任务中途修改代码
3. **技能学习**：通过 `domain-skills/` 目录积累网站特定知识
4. **极薄架构**：~600 行代码 vs 其他框架动辄数万行

## 使用场景

- 自动化网页操作（填表、点击、文件上传）
- AI 驱动的端到端测试
- 复杂网页数据抓取
- 自动化工作流

## 总结

Browser Harness 代表了一种全新的 Agent 框架设计理念：**极简 + 自愈**。它摒弃了传统框架的复杂性，让 LLM 能够直接在运行时扩展自身能力。这种"边做边学"的模式使得 AI 代理可以应对任何未曾预设的浏览器任务，真正实现"你再也不用手动操作浏览器"的愿景。