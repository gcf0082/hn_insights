# Hacker News 洞察报告: Mistral Small 4

**来源**: [https://news.ycombinator.com/item?id=47404575](https://news.ycombinator.com/item?id=47404575)  
**日期**: 2026-03-20  
**主题**: Mistral Small 4 模型发布

## 模型概述

Mistral Small 4 是一个约 1190 亿参数的 MoE (混合专家) 模型，使用 128 个专家但每个 token 只激活 4 个，因此前向传播相当于约 60 亿参数。

## 关键洞察

### 1. 基准测试可信度问题
- 用户对 AI 模型的基准测试结果持怀疑态度
- Qwen 3.5 122B 在基准测试中表现优秀，但实际使用体验不佳
- Mistral 在基准测试中略逊于 Qwen，但实际表现可能更好

### 2. 性能与成本优势
- 输出价格仅为 $0.60/1M tokens，性价比极高
- 相比 Qwen 3.5，推理时间和 token 消耗更少，成本更低
- 在相同工作负载下表现更好，且价格更便宜

### 3. 技术架构特点
- MoE 架构：128 experts，4 active per token
- 约 120B 参数，可安装在单张 H100 (4-bit quant) 或 128GB Apple Silicon/AMD AI CPU 上
- 与传统的dense transformer缩放方式完全不同

### 4. 市场定位
- 被评价为"Big Deal"，可能吸引大量基于 Qwen 和其他中国模型构建的开发者
- 开源且可自托管、可微调
- 适合需要在成本和性能之间取得平衡的应用场景

### 5. 实际测试反馈
- 在 agentic workflow 测试中表现尚可，适合基础任务
- 不适合复杂任务如查询生成和检索
- 比 GPT-OSS-120b 好用

## 总结

Mistral Small 4 是一个具有高性价比的开源 MoE 模型，特别适合需要在本地运行大模型且注重成本的开发者。其价格优势和可自托管特性使其成为中小型工作负载的理想选择。
