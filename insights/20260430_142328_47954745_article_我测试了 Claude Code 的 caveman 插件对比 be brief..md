# 洞察报告：Caveman 插件 vs "be brief" 提示词基准测试

**洞察链接**: https://www.maxtaylor.me/articles/i-benchmarked-caveman-against-two-words

**发布日期**: 2026年4月29日

**作者**: Max Taylor

**测试主题**: 比较 Claude Code 压缩插件 Caveman 与简单的 "be brief" 提示词

---

## 基本结论

Caveman 插件在 token 压缩和输出质量上并未超越简单的 "be brief" 提示词。两者在 token 使用量和答案质量上几乎持平，但 Caveman 提供了额外的结构化输出价值。

## 测试设计

### 测试范围

- **24 个提示词**，覆盖 6 个类别：
  - Bug 诊断（5个）
  - 概念解释（5个）
  - 架构权衡（4个）
  - 多步骤设置（4个）
  - 安全/破坏性操作（3个）
  - 错误解释（3个）

### 测试对象

- **baseline**: Claude 默认设置，无任何指令
- **brief**: 每次提示前添加 "Be brief."
- **lite/full/ultra**: Caveman 插件的三种强度模式

### 评估方法

- 使用单独的 Claude 模型对每个回答进行评分
- 检查关键要点（key_points）的语义匹配
- 检查必需术语（must_use_terms）的字面匹配
- 检测应避免的错误声明（must_avoid）

## 核心发现

### 1. 质量无差异

| 模式 | 质量得分 |
|------|----------|
| baseline | 0.985 |
| brief | 0.985 |
| lite | 0.976 |
| full | 0.975 |
| ultra | 0.970 |

所有模式的得分差异在 1.5% 以内。每个模式都达到了 100% 的关键要点覆盖率。在 120 个回答中零触发任何应避免的错误声明。

### 2. Token 使用量

| 模式 | 平均 Token 数 |
|------|---------------|
| baseline | 636 |
| **brief** | **419** |
| lite | 401 |
| full | 404 |
| ultra | 449 |

"Be brief." 相比 baseline 减少了 34% 的 token。lite 和 full 模式的 token 使用量与 brief 接近。ultra 模式反而产生了最长的回答。

### 3. 分类差异

在 bug 诊断、概念解释、架构权衡和错误解释类别中，ultra 模式表现最佳或并列最佳。

但在多步骤设置和安全警告类别中，所有 Caveman 模式都表现不稳定。原因是 Caveman 内置的 "Auto-Clarity" 规则会在安全警告、不可逆操作和多步骤序列时显式停止压缩。

## Caveman 的实际价值

尽管压缩效果与 "be brief" 相当，但 Caveman 仍有以下优势：

1. **一致的输出格式**: 每次回答都遵循相同的模式，便于下游工具处理

2. **强度调节**: 可通过斜杠命令在 lite/full/ultra 之间切换

3. **会话持久性**: 通过 SessionStart 和 UserPromptSubmit 钩子持续注入规则集

4. **安全机制**: 自动识别何时停止压缩

## 建议

- **如只需简短输出**: 在提示词或 CLAUDE.md 中添加 "be brief." 即可
- **如需结构化输出**: 选择 Caveman 以获得一致的输出格式

## 启示

大多数提示工程建议从未与默认设置进行过实际测量对比。应该进行基准测试来验证这些建议的实际效果。

---

**参考资源**:
- 测试代码仓库: https://github.com/max-taylor/cc-compression-bench
- 视频版本: https://youtu.be/wijoYNiZq3M
- Caveman 插件: https://github.com/juliusbrussee/caveman