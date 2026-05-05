# 洞察报告：Shai-Hulud 主题恶意软件发现于 PyTorch Lightning AI 训练库

**洞察链接**：https://news.ycombinator.com/item?id=47964617

**标题**：Shai-Hulud Themed Malware Found in the PyTorch Lightning AI Training Library

**来源**：Hacker News (Semgrep 安全研究)

**发布日期**：2026年4月30日

**HN得分**：176 points

**评论数**：47 comments

---

## 事件概述

2026年4月30日，PyPI 包 `lightning`（广泛使用的深度学习框架）在发布的 2.6.2 和 2.6.3 版本中遭到供应链攻击。恶意代码隐藏在名为 `_runtime` 的隐藏目录中，当模块被导入时会自动执行。攻击者使用《沙丘》主题命名（Shai-Hulud），被称为 "EveryBoiWeBuildIsAWormyBoi" 攻击活动。

## 攻击手法分析

### 恶意代码执行机制
恶意代码被嵌入在 `_runtime` 目录中，通过模块导入触发自动执行。运行 `pip install lightning` 即可激活恶意代码。

### 数据窃取目标
攻击者窃取的敏感信息包括：
- GitHub 访问令牌（ghp_, gho_）
- npm 令牌
- AWS 凭证（环境变量、~/.aws/credentials、IMDSv2、ECS）
- Azure 密钥（DefaultAzureCredential、Key Vault）
- GCP 密钥（Secret Manager）
- 环境变量和 CI/CD 密钥

### 数据泄露渠道
该攻击使用四个平行渠道进行数据外泄：
1. **HTTPS POST 到 C2 服务器**：直接向攻击者控制的服务器发送窃取数据
2. **GitHub 提交搜索 dead-drop**：利用 GitHub 提交消息作为数据中转站（格式：EveryBoiWeBuildIsAWormyBoi:<base64(base64(token))>）
3. **攻击者控制的公开 GitHub 仓库**：创建名为 "A Mini Shai-Hulud has Appeared" 的仓库
4. **直接推送到受害者仓库**：将窃取数据推送到受害者的 GITHUB_REPOSITORY

### 持久化机制
恶意代码通过以下开发者工具实现持久化：
- **Claude Code**：`.claude/settings.json` 中的 SessionStart hook
- **VS Code**：`.vscode/tasks.json` 中的 folderOpen 任务
- **恶意 GitHub Actions**：注入 "Formatter" workflow 窃取所有 secrets

## 影响范围

- **受影响版本**：lightning 2.6.2 和 2.6.3
- **发布平台**：PyPI（GitHub 仓库未受影响）
- **攻击时间**：2026年4月30日

## 社区应对建议

1. **立即降级**：降级到 2.6.1 版本
2. **等待修复**：等待 2.6.4 版本发布后再升级
3. **排查 IOC**：检查是否存在以下文件：
   - `.claude/settings.json` 和 `.claude/router_runtime.js`
   - `.vscode/tasks.json` 和 `.vscode/setup.mjs`
   - `_runtime/start.py` 和 `_runtime/router_runtime.js`
4. **轮换凭证**：轮换所有可能在受影响环境中的 GitHub token、云服务密钥
5. **使用 pip 新功能**：pip 26.1 支持 `--uploaded-prior-to` 参数排除特定日期后的版本

## 总结

这是一起典型的软件供应链攻击，攻击者通过直接发布到 PyPI（而非提交到 GitHub）绕过了代码审查。PyTorch Lightning 官方确认恶意代码未进入 GitHub 仓库。此事件再次提醒我们：
- 开源依赖的安全性至关重要
- 依赖锁定（pinning）是防御供应链攻击的关键措施
- 自动化工具链可能成为攻击目标
- 定期审计和及时响应是防御供应链攻击的关键