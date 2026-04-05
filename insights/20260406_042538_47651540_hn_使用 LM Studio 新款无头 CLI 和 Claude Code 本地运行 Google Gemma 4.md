---
title: 本地运行Google Gemma 4与LM Studio和Claude Code
hn_id: 47651540
date: 2026-04-06
---

**洞察链接**: https://news.ycombinator.com/item?id=47651540

**基本信息**:
- 标题: Running Google Gemma 4 Locally with LM Studio's New Headless CLI and Claude Code
- 发布者: vbtechguy
- 得分: 54 points
- 评论数: 16 comments
- 发布时间: 3小时前

---

## 中文总结

### 文章概述

这是一篇介绍如何在macOS上本地运行Google最新发布的Gemma 4（26B参数）大语言模型，并将其与Anthropic的Claude Code AI编程助手结合使用的教程。

### 核心技术要点

1. **Gemma 4模型**：Google发布的最新开源大语言模型，采用MoE（Mixture of Experts）架构，26B参数版本可在消费级硬件上运行

2. **LM Studio**：本地大模型运行工具，新增Headless CLI模式，可在终端运行而无需GUI界面

3. **Claude Code**：Anthropic的AI编程CLI工具，现可配置使用本地模型作为后端

4. **Ollama替代方案**：部分用户指出更简单的方案是使用`ollama launch claude --model gemma4:26b`

### 讨论要点

- **LM Studio与Claude Code兼容性问题**：有用户反映LM Studio配合Claude Code使用时会出现"卡住"的情况，建议使用Ollama API替代

- **MoE架构的VRAM使用**：澄清了MoE并不节省VRAM，仍需加载所有权重到内存，但可减少每轮前向传播的计算量

- **Claude Code Token效率**：有用户指出Claude Code的token消耗较大，需要大显存支持；云端模型（如Opus）有100万token上下文窗口，本地难以实现

- **工具选择**：推荐使用Caveman模式或其他本地AI编程工具来获得更好的本地体验
