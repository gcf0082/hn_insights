# Hacker News 洞察报告

**链接**: https://news.ycombinator.com/item?id=47920787

**基本信息**:
- **标题**: Show HN: OSS Agent I built topped the TerminalBench on Gemini-3-flash-preview
- **作者**: GodelNumbering
- **时间**: 2026-04-27 (约3小时前)
- **分数**: 144 points
- **评论数**: 53 comments

---

## 项目介绍

**Dirac** 是一个开源的AI编程Agent，在 TerminalBench 2.0 基准测试中取得了 **65.2%** 的分数，显著超过了：
- Google 官方结果：47.8%
- Junie CLI（闭源）：64.3%

该项目基于 Cline（VSCode的AI编程扩展）进行深度修改，拥有约70,000行代码变更和40,000行删除。

---

## 核心技术特点

### 1. Hash-Anchored 编辑
使用优化的 Myers Diff 算法进行文件编辑，减少编辑错误。

### 2. AST 上下文获取
- 利用语言的抽象语法树（AST）来决定需要获取什么内容到上下文中
- 完全避免了大型代码文件的整体读取
- 使用 tree-sitter WASMs，目前支持 **14种语言**
- 增量维护符号数据库（SQLite），基于时间戳更新

### 3. 批量操作
- 同时执行大量读取和编辑操作
- 允许模型动态执行 bash/python/perl 脚本来分析问题

### 4. 上下文策展
- 修剪旧的工具调用响应
- 截断工具输出
- 自动压缩上下文
- 机会主义上下文更新（预测模型下一步可能需要的内容并预先放入上下文）

### 5. 多模型支持
- 支持所有 Cline 支持的模型，包括 Qwen 和各种开源/闭源模型
- 默认使用 Gemini-3-flash-preview

---

## 社区讨论要点

### Harness 的重要性
讨论中最核心的结论是：**harness（工具框架）对性能的影响远超模型选择**。
- 从 47.8% 到 65.2% 的巨大差距主要来自于 harness 的改进
- 更换 harness 比更换底层模型带来的基准分数变化更大

### 上下文管理
- 修剪旧工具调用响应、截断输出、自动压缩的效果很好
- 减少上下文的好处大于"记住一切"的好处
- 保留简短摘要是有价值的

### 子Agent设计
- 不向主Agent暴露任何工具，除了 `run_agent` 工具
- 子Agent可以访问经典的 search/execute/fetch 工具
- 子Agent返回简洁摘要可以保持父Agent上下文清洁

### AST vs Grep
- Grep 对于代码概念命名良好的代码库很有效
- 但对于使用通用命名的代码库（如 "Tree"、"Node"），grep 几乎无法使用
- AST 可以避免拉取捆绑包中的代码

### 实际使用反馈
- 有用户报告在大型代码库重构任务中比 OpenCode 更高效
- 支持 Plan+Act 模式
- 使用 openrouter API key 即可使用

---

## 相关链接

- GitHub: https://github.com/dirac-run/dirac
- NPM: `npm install -g dirac-cli`
- TerminalBench: https://debugml.github.io/cheating-agents/

---

*报告生成时间: 2026-04-27 23:43:26*