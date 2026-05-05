# Claude Code 压缩插件基准测试：简单的 "be brief" 击败 Caveman

**链接**: https://news.ycombinator.com/item?id=47954745
**原文链接**: https://www.maxtaylor.me/articles/i-benchmarked-caveman-against-two-words
**标题**: I benchmarked Claude Code's caveman plugin against "be brief."
**分数**: 65 points
**发布者**: max-t-dev
**时间**: 1 天前
**评论数**: 42

## 核心内容

作者对 Claude Code 的热门压缩插件 Caveman 进行了基准测试，将其与简单的 "be brief." 提示词进行对比。结果令人惊讶：两个词的提示在 tokens 消耗和输出质量上与功能复杂的插件表现相当。

### 测试方法

- **测试数量**: 24 个提示词，覆盖六个类别
- **测试类别**: bug 诊断、概念解释、架构权衡、多步骤设置、安全/破坏性操作、错误解释
- **测试对象**: 五组对比（baseline、brief、lite、full、ultra）
- **评估方式**: Claude Sonnet 4-6 根据每个提示的评分标准进行评分

### 核心发现

1. **质量无差异**: 所有组别的质量得分都在 1.5% 以内，baseline 和 brief 都是 0.985
2. **Tokens 消耗相当**: "be brief." 将 tokens 减少 34%，与 Caveman lite 和 full 模式接近
3. **Ultra 模式表现意外**: 最严格的 ultra 模式反而产生了最长的输出

## 技术细节

### Caveman 插件特点

- 六种模式，支持斜杠命令和强度调节
- 提供古典中文变体版本
- 通过 `SessionStart` 和 `UserPromptSubmit` 钩子在每个提示中重新注入规则集

### "be brief." 的优势

- 无需安装任何插件
- 两个词 vs 复杂配置
- 在测试中匹配了所有三种 Caveman 模式的 tokens 消耗

### 社区观点

- **实用建议**: 如果只想让输出更简短，从 "be brief." 开始
- **选择 Caveman 的理由**: 需要跨会话的稳定输出结构时
- **更大的启示**: 大多数提示工程建议从未与默认设置进行过实际测量

## 结论

这个基准测试揭示了一个重要的教训：复杂的提示工程工具往往可以被简单的两词提示所替代。虽然 Caveman 在一致输出结构、强度调节和长会话持久性方面有其价值，但对于大多数用户来说，从简单的 "be brief." 开始可能是更实用的选择。测试框架已开源，其他压缩策略也可以在此基础上进行对比测试。