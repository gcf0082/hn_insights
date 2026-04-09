# 洞察报告

**链接**: https://github.com/salmanmohammadi/nanocode/discussions/1  
**项目**: nanocode - 用200美元训练你自己的Claude Code  
**作者**: salmanmohammadi  
**日期**: 2026年4月5日

---

## 项目简介

nanocode是一个开源库，展示如何从头训练你自己的Claude Code代理。该项目采用Constitutional AI方法（Anthropic训练Claude模型所使用的技术），包括编写自定义SOUL.md、定义代理接口、生成合成数据和使用偏好优化来对齐模型。

项目完全使用JAX编写，专为TPU训练优化。可在约9小时内用200美元训练1.3B参数的nanocode-d24模型，或用34美元在1.5小时内训练477M参数的nanocode-d20模型。

## 技术架构

### 1. 预训练与分词

- 在FineWeb-EDU和The Stack-V2数据集上训练，数据配比为1:5
- 代码tokenization效率显著提升（比nanochat提升50.9%）
- 模型参数与数据比率遵循8:1的缩放定律

### 2. 代理接口设计

定义了四个核心工具：
- **Read**: 读取文件
- **Edit**: 编辑文件
- **Grep**: 搜索模式
- **Bash**: 执行shell命令

### 3. Constitutional AI训练流程

采用两阶段训练：
1. **Constitutional SFT**: 生成对齐的合成数据，通过critique模型筛选
2. **DPO (Direct Preference Optimization)**: 直接偏好优化，无需奖励模型

## 性能对比

| 深度 | 参数 | CORE | 成本 | 时间 | MFU |
|------|------|------|------|------|-----|
| d12  | 135M | 0.090| $3   | 9min | 17.4% |
| d20  | 477M | 0.170| $30  | 1.4h | 45.2% |
| d24  | 1.3B | 0.227| $200 | 9.3h | 52.5% |

## SOUL特性

nanocode的SOUL定义了独特的个性：
- 仅使用小写字母（代码中的专有名词除外）
- 温暖友好
- 有点幽默感
- 不卑躬屈膝，不过度冗长
- 精确遵循给定指令

## 关键创新点

1. **合成数据生成管道**: 通过critique循环生成高质量的工具调用示例
2. **长上下文rollout**: 2000个复杂场景，模拟真实编码代理使用场景
3. **TPU优化**: 高度优化的JAX/XLA训练基础设施

## 总结

nanocode展示了用有限预算（200美元）训练AI编码代理的可行性，为理解Constitutional AI和代理训练提供了实践参考。项目代码约5.5K行，设计简洁可 hack，适合学习和定制。
