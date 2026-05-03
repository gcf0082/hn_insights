# 洞察报告：Specsmaxxing

## 基本信息

- **洞察链接**: https://acai.sh/blog/specsmaxxing
- **发布日期**: 2026年
- **主题**: 通过编写规范(YAML)克服AI心理失调，以及开源工具包的介绍

---

## 核心内容总结

### 问题背景

作者描述了与AI agent协作时的常见困境：agent经常在实现过程中发现遗漏的边界情况、提出架构改进建议(如游标分页vs偏移分页)、指出性能问题(如N+1查询)。这些问题的根本原因在于：**上下文窗口有限，当上下文耗尽或切换会话时，agent会脱轨，需求也会丢失**。

### 解决方案：ACAI (Acceptance Criteria for AI)

作者引入了**ACID (Acceptance Criteria IDs)**的概念：为每个需求分配唯一标识符，并在代码和测试中引用这些标识符。这种做法实现了规范与代码的紧密耦合，使开发者能够：
- 在大型PR中快速导航
- 精确定位需求被满足或测试的位置
- 跟踪需求状态(todo、assigned、completed)
- 追踪验收覆盖率而非仅测试覆盖率

### Acai.sh 工具包

作者开源了一个工具包，包含：
1. **feature.yaml格式**：用于编写特性的规范，支持ACID引用
2. **CLI工具**：可在npm或GitHub releases获取
3. **Web应用**：基于Elixir、Phoenix、PostgreSQL的仪表板和JSON REST API

### 工作流程

1. **编写规范**：使用feature.yaml格式，列出可测试的具体需求
2. **交付**：运行`npx @acai.sh/cli skill`让agent学习规范驱动开发流程
3. **审查**：通过仪表板按需求审查(而非逐文件审查)
4. **迭代**：修改规范或使用仪表板附加注释

### 未来展望

- **从Specsmaxxing到Testmaxxing**：当代码生成速度快于阅读速度时，QA和验证成为瓶颈
- **从Testmaxxing到响应式软件工厂**：当规范定义良好且CI/QA高度可靠时，LLM可以自主响应红色测试或告警

### 与其他工具的对比

- **GitHub SpecKit**：更像"带额外步骤的氛围编程"，解决不同问题
- **OpenSpec**：描述系统当前行为(而非应有何行为)，且倾向AI生成规范
- **Kiro**：EARS语法转换，无端到端交付
- **Traycer.ai**：仍使用普通.md文件，Acai对规范格式更有主张

---

## 不适用场景

- 产品低风险或简单，无需编写规范
- 规范是主观的，需跨代码库迭代
- ACID依赖稳定编号，修订规范时需重新对齐代码
- 不鼓励将设计和表面需求放入规范
- 需要采用feature.yaml格式