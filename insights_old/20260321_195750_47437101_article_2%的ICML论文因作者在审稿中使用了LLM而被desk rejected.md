# Insights Report: On Violations of LLM Review Policies

## 基本信息

- **标题**: On Violations of LLM Review Policies
- **来源**: ICML Blog
- **发布日期**: 2026年3月18日
- **原始链接**: https://blog.icml.cc/2026/03/18/on-violations-of-llm-review-policies/
- **作者**: ICML 2026 Program Chairs (Alekh Agarwal, Miroslav Dudik, Sharon Li, Martin Jaggi), Scientific Integrity Chair (Nihar B. Shah), Communications Chairs (Katherine Gorman, Gautam Kamath)

## 核心洞察

### 1. 违规规模
- **497篇论文被拒稿**（约占全部投稿的2%）
- **795条评审（约占全部评审的1%）**由506名评审撰写，被检测到使用了LLM
- **51名评审**被移除出评审池（因为超过一半的评审都是LLM生成的）

### 2. ICML 2026 LLM使用政策
- **政策A（保守型）**: 禁止使用任何LLM
- **政策B（开放型）**: 允许使用LLM帮助理解论文和相关工作，以及润色评审

### 3. 检测方法：水印技术
- 使用基于Rao, Kumar, Lakkaraju和Shah的研究方法
- 创建了**17万个短语**的字典
- 为每篇论文随机选取2个短语，通过PDF嵌入隐藏指令
- LLM在生成评审时会包含这些指定短语
- 成功率：大多数前沿模型超过80%

### 4. 处理措施
- 被检测到的违规评审被**全部删除**
- 违规评审对应的投稿被**拒稿**
- 如果一名评审超过一半评审都是LLM生成的，则该评审被**移除出评审池**

### 5. 关键观点
- 约1%的评审违反了明确同意遵守的政策
- 51名评审（约占506名违规评审的10%）被完全移除
- 这提醒社区：随着领域快速变化，必须最积极保护的是彼此之间的信任

## 相关链接

- [ICML 2026 LLM Policy](https://icml.cc/Conferences/2026/LLM-Policy)
- [Community Preferences and Feedback](https://icml.cc/Conferences/2026/Intro-LLM-Policy)
- [Rao et al. Research Paper](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0331871)
- [ICML 2026 What's New in Peer Review](https://blog.icml.cc/2026/01/08/whats-new-in-icml-2026-peer-review/)
