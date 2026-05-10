# Hacker News 洞察报告

**洞察链接**: https://news.ycombinator.com/item?id=48002136

**标题**: DeepClaude – Claude Code agent loop with DeepSeek V4 Pro, 17x cheaper

**发布者**: alattaran

**发布时间**: 3小时前

**得分**: 165

**评论数**: 76

---

## 项目简介

DeepClaude是一个简单的Shell脚本，通过设置环境变量使Claude Code能够使用DeepSeek V4 Pro模型替代Anthropic的模型，从而实现显著的成本降低（约为原来的1/17）。

核心实现方式：
```bash
#!/bin/sh
export ANTHROPIC_BASE_URL=https://api.deepseek.com/anthropic
export ANTHROPIC_AUTH_TOKEN=sk-secret
export ANTHROPIC_MODEL=deepseek-v4-flash
export CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1
exec claude $@
```

---

## 社区讨论要点

### 1. 实现方式的简易性
- 实际上就是设置两个环境变量即可
- DeepSeek官方文档中已有说明如何与Claude Code集成
- 有人认为这个项目的意义不大，因为本身配置很简单

### 2. 成本效益
- 许多开发者对成本优化非常感兴趣
- 有用户提到使用Opus进行规划，DeepSeek进行实现的组合
- GLM 5.1也是一个被推荐的性价比高的选择
- Ollama Cloud也被提及为经济实惠的选项

### 3. Claude Code与其他工具的比较
- OpenCode被提及为一个开源替代方案
- 但有人认为OpenCode功能不如Claude Code丰富
- 还有人指出OpenCode默认会追踪用户数据
- 有人对pi.dev持批评态度

### 4. 模型选择策略
- 高级模型（如Opus）用于设计规划
- 较便宜的模型用于实际编码实现
- 本地模型（如Qwen 3.6 27B）配合高端硬件也是可行方案
- 有用户使用Asus Ascent GX10等AI PC运行本地模型

### 5. AI行业的竞争态势
- 讨论了中国AI模型对美国企业的威胁
- 开源模型可能不易被限制
- 有人认为硅谷无法承受竞争激烈的市场

### 6. 关于"vibe coding"的讨论
- 帖子本身被批评为"vibe coded"（随意编码）
- 价格信息也被指不准确
- 引发了对HN上AI相关帖子质量的讨论

---

## 总结

这个项目展示了AI编码工具领域的成本优化趋势。开发者可以通过使用替代模型提供商来大幅降低使用成本。社区讨论反映了对AI工具成本、模型选择以及开源与闭源方案之间权衡的持续关注。