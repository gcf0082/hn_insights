# Claude Token Counter 工具更新：新增加模型对比功能

**洞察链接**: https://simonwillison.net/2026/Apr/20/claude-token-counts/

**来源**: Simon Willison's Weblog

**发布日期**: 2026年4月20日

---

## 核心发现

Simon Willison 对其 Claude Token Counter 工具进行了升级，新增了模型对比功能，允许用户同时对不同模型进行 token 计数以便进行比较。

### 关键信息

1. **Opus 4.7 是首个更改分词器的模型**
   - Opus 4.7 使用了更新的分词器来改善文本处理能力
   - 相同的输入会映射到更多 token，数量约为原来的 1.0-1.35 倍

2. **Opus 4.7 vs Opus 4.6 的 token 数量对比**
   - 使用 Opus 4.7 系统提示进行测试
   - Opus 4.7: 7,335 tokens
   - Opus 4.6: 5,039 tokens
   - 比率: **1.46x**

3. **成本影响**
   - Opus 4.7 与 Opus 4.6 定价相同：输入 $5/百万 tokens，输出 $25/百万 tokens
   - 由于 token 数量增加，预计成本将增加约 **40%**

4. **图像处理改进**
   - Opus 4.7 支持更高分辨率的图像
   - 最长边可达 2,576 像素（约 3.75 百万像素），是之前模型的三倍多
   - 高分辨率图像的 token 增幅更大（3.01x），但这主要是因为支持更高分辨率

5. **PDF 处理**
   - 15MB、30页的密集文本 PDF 测试
   - Opus 4.7: 60,934 tokens
   - Opus 4.6: 56,482 tokens
   - 比率: **1.08x**（显著低于原始文本的增幅）

---

## 可比较的模型

该工具支持以下四个当前主要模型：

- Claude Opus 4.7
- Claude Opus 4.6
- Claude Sonnet 4.6
- Claude Haiku 4.5

---

## 结论

Opus 4.7 的分词器更新带来了 token 数量的增加，这在文本处理上意味着约 40% 的成本上升。然而，这一改进也带来了更好的图像处理能力和更高的分辨率支持。对于需要处理高分辨率图像的用户来说，这一更新是有价值的。