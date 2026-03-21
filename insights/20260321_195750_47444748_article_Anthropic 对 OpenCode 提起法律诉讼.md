# PR Insights Report

## 基本信息

| 项目 | 内容 |
|------|------|
| **洞察链接** | https://github.com/anomalyco/opencode/pull/18186 |
| **PR 标题** | anthropic legal requests |
| **状态** | Merged |
| **作者** | thdxr |
| **合并时间** | 2026-03-19 |
| **目标分支** | dev |
| **源分支** | anthropic-legal-rebased |

## 概述

该 PR 根据 Anthropic 的法律要求，移除了代码库中所有与 Anthropic 相关的引用内容。

## 主要变更

1. **删除 anthropic-20250930.txt 系统提示文件**
   - 移除了 Anthropic 品牌化的系统提示文件

2. **移除 opencode-anthropic-auth 内置插件**
   - 从内置插件列表中移除 `opencode-anthropic-auth@0.0.13`
   - 同时移除了 `OPENCODE_DISABLE_DEFAULT_PLUGINS` 标志检查

3. **移除 Provider 提示**
   - 从 Provider 登录选择 UI 中移除 `anthropic: "API key"` 提示标签

4. **更新 Provider 枚举**
   - 从 Provider 枚举中移除 Anthropic

## 社区反应

该 PR 引发了社区的强烈反应：
- 416 个 thumbs down 反应
- 181 个 confused 反应
- 社区开发了多个第三方插件作为解决方案

## 社区解决方案

1. **opencode-claude-auth** (griffinmartin)
   - GitHub: https://github.com/griffinmartin/opencode-claude-auth
   - npm: https://www.npmjs.com/package/opencode-claude-auth

2. **opencode-anthropic-oauth** (shahidshabbir-se)
   - GitHub: https://github.com/shahidshabbir-se/opencode-anthropic-oauth
   - npm: https://www.npmjs.com/package/opencode-anthropic-oauth

3. **opencode-claude-code-plugin** (unixfox)
   - GitHub: https://github.com/unixfox/opencode-claude-code-plugin