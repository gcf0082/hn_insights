# CodeBurn – 按任务分析 Claude Code token 使用量

**洞察链接**: https://news.ycombinator.com/item?id=47759035

**基本信息**:
- **标题**: Show HN: CodeBurn – Analyze Claude Code token usage by task
- **来源**: GitHub (agentseal/codeburn)
- **发布时间**: 10 小时前
- **得分**: 76 points
- **评论数**: 17 comments
- **作者**: agentseal

## 项目概述

CodeBurn 是一个用于分析 Claude Code token 使用量的工具。作者在发现自己每周在 Claude Code 上花费约 1400 美元却几乎没有visibility了解具体哪些任务消耗了 token 后，开发了这款工具。

## 核心功能

1. **数据来源**: 读取 Claude Code 本地存储的 JSONL 会话转录文件 (~/.claude/projects/)
2. **任务分类**: 根据工具使用模式将每个对话轮次分类到 13 个类别（不涉及 LLM 调用）
3. **关键发现**: 
   - 约 56% 的支出用于没有工具使用的对话轮次
   - 实际编码操作（编辑/写入）仅占约 21%

## 技术特点

- **界面**: 使用 Ink（React for terminals）构建的交互式终端 UI
- **功能**: 渐变柱状图、响应式面板、键盘导航
- **集成**: macOS 的 SwiftBar 菜单栏集成

## 社区反馈

1. **分类准确性**: 有用户指出活动分类略有问题，例如将规划活动误分类
2. **Cursor 支持**: 目前不支持 Cursor Agent，计划添加支持
3. **成本对比**: 有用户提到 $200/月的套餐从未遇到过速率限制
4. **未来方向**: 建议添加评估用户工作效率并建议改进方向的功能

## 相关项目

- Claudoscope: 类似的 token 分析工具
- ClaudeRank.com: 完全开源的类似产品