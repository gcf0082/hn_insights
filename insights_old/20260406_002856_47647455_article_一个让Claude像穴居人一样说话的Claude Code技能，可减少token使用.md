# 洞察报告：Caveman

## 基本信息

- **洞察链接**: https://github.com/JuliusBrussee/caveman
- **项目名称**: caveman
- **项目描述**: 一个 Claude Code skill/plugin 和 Codex 插件，让 AI 用"原始人"风格说话，可节省约 75% 的 token
- **_stars**: 794
- **Forks**: 14
- **License**: MIT

## 项目概述

Caveman 是一个基于病毒式观察产生的项目——发现用"原始人"风格的说话方式可以显著减少 LLM 的 token 使用量，同时保持完全的技术准确性。项目作者将这一想法做成了一个可一键安装的技能插件。

## 核心功能

1. **Token 节省**: 可节省约 75% 的 token 使用量
2. **速度提升**: 响应速度提升约 3 倍
3. **技术准确性**: 保持 100% 的技术准确性
4. **安装便捷**: 支持 npx、Claude Code plugin、Codex 多种安装方式

## 优化策略

| 类型 | 原始人风格处理 |
|------|---------------|
| 填充词 | 移除 "I'd be happy to help" 等冗余表达 |
| 冠词 | 移除 a, an, the |
| 客套话 | 移除 "Sure, I'd be happy to" |
| 犹豫词 | 移除 "It might be worth considering" |
| 技术术语 | 保留精确术语（如 polymorphism） |
| 错误信息 | 精确引用 |

## 安装方式

```bash
# 使用 npx
npx skills add JuliusBrussee/caveman

# 或使用 Claude Code plugin
claude plugin marketplace add JuliusBrussee/caveman
claude plugin install caveman@caveman
```

## 使用方法

触发方式：
- `/caveman` 或 Codex `$caveman`
- "talk like caveman"、"caveman mode"、"less tokens please"

停止方式：
- "stop caveman" 或 "normal mode"

## 对比示例

**普通 Claude（69 tokens）**:
> "The reason your React component is re-rendering is likely because you're creating a new object reference on each render cycle. When you pass an inline object as a prop, React's shallow comparison sees it as a different object every time, which triggers a re-render. I'd recommend using useMemo to memoize the object."

**原始人风格（19 tokens）**:
> "New object ref each render. Inline object prop = new ref = re-render. Wrap in `useMemo`."

## 结论

Caveman 项目展示了一种有趣的提示工程技巧——通过简化语言风格，在不影响技术准确性的前提下显著降低 token 消耗。这对于需要控制成本和提高响应速度的应用场景具有实际价值。