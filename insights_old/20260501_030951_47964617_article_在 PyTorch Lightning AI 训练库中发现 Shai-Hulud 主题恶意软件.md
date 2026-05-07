# PyTorch Lightning AI训练库中发现Shai-Hulud主题恶意软件

**洞察链接**: https://semgrep.dev/blog/2026/malicious-dependency-in-pytorch-lightning-used-for-ai-training/

**报告日期**: 2026年5月1日

**安全事件概述**: PyPI包"lightning"（广泛使用的深度学习框架）在2.6.2和2.6.3版本中遭受供应链攻击，植入Mini Shai-Hulud主题的恶意代码，旨在窃取凭证并在导入时执行恶意软件。

---

## 一、事件概述

PyPI包"lightning"是一个广泛使用的深度学习框架，于2026年4月30日发布的2.6.2和2.6.3版本遭受供应链攻击影响。任何使用该包进行图像分类、LLM微调、扩散模型开发或时间序列预测的团队都可能受到影响。

攻击者通过`pip install lightning`即可激活恶意代码。受影响的版本包含隐藏的`_runtime`目录，其中包含混淆的JavaScript有效载荷，在模块导入时自动执行。

该恶意软件旨在窃取凭证、认证令牌、环境变量和云密钥，同时尝试污染GitHub仓库。攻击具有Shai-Hulud主题特色，包括创建名为EveryBoiWeBuildIsaWormBoi的公共仓库。

安全研究人员认为这是同一威胁行为者继Mini Shai-Hulud攻击之后的再次行动。恶意提交消息遵循相同的Dune主题命名约定，本次活动使用前缀EveryBoiWeBuildIsAWormyBoi以区分原始Mini Shai-Hulud攻击。

## 二、受影响版本

- lightning version 2.6.2
- lightning version 2.6.3

## 三、攻击机制分析

### 3.1 跨生态系统传播：PyPI到npm

与直接针对npm的Mini Shai-Hulud不同，这次攻击的入口点是PyPI。恶意代码有效载荷仍然是JavaScript，蠕虫传播通过npm进行。一旦运行，如果恶意软件发现npm发布凭据，它会将setup.mjs dropper和router_runtime.js注入该令牌可以发布到的每个包，设置scripts.preinstall以执行dropper，修改补丁版本并重新发布。任何安装了这些包的下游开发者都会在其机器上运行完整恶意软件，其令牌被窃取且包被蠕虫化。

### 3.2 数据泄露机制

泄露组件与上次活动中的Mini Shai-Hulud机制设计相同，使用四个并行通道，即使个别路径被阻止，被窃取的数据也能传出：

1. **HTTPS POST到C2服务器**: 被窃取的数据立即通过443端口POST到攻击者控制的服务器。域名和路径以加密字符串形式存储在有效载荷中，使静态分析更加困难。

2. **GitHub提交搜索死drop**: 恶意软件轮询GitHub提交搜索API以查找以EveryBoiWeBuildIsAWormyBoi开头的提交消息，其中携带双Base64编码的令牌，格式为EveryBoiWeBuildIsAWormyBoi:<base64(base64(token))>。解码后，令牌用于验证Octokit客户端进行进一步操作。

3. **攻击者控制的公共GitHub仓库**: 创建一个具有随机选择的Dune词名称和描述"A Mini Shai-Hulud has Appeared"的新公共仓库，可在GitHub上直接搜索。被窃取的凭据作为results/results-<timestamp>-<n>.json提交（通过API Base64编码，内部为纯JSON），超过30MB的文件被分割成编号块。提交消息使用chore: update dependencies作为掩护。

4. **推送到受害者自己的仓库**: 如果恶意软件获得ghs_ GitHub服务器令牌，它将被窃取的数据直接推送到受害者的GITHUB_REPOSITORY的所有分支。

### 3.3 窃取目标

恶意软件针对本地文件、CI/CD流水线、云提供商和各平台凭据：

- **文件系统**: 扫描80多个凭据文件路径以获取ghp_、gho_和npm_令牌（每个文件最多5MB）。
- **Shell/环境**: 运行gh auth token并转储process.env中的所有环境变量。
- **GitHub Actions**: 在Linux运行器上，通过嵌入式Python转储Runner.Worker进程内存，提取所有标记为isSecret:true的密钥，以及GITHUB_REPOSITORY和GITHUB_WORKFLOW。
- **GitHub组织**: 检查令牌范围（repo、workflow）并遍历GitHub Actions组织密钥。
- **AWS**: 尝试环境变量、~/.aws/credentials配置文件、IMDSv2（169.254.169.254）和ECS（169.254.170.2）以调用sts:GetCallerIdentity；此外还枚举和获取所有Secrets Manager值和SSM参数。
- **Azure**: 使用DefaultAzureCredential枚举订阅并访问Key Vault密钥。
- **GCP**: 通过GoogleAuth认证并枚举和获取所有Secret Manager密钥。

目标覆盖本地开发环境、CI运行器和所有三个主要云提供商。在受影响窗口期间导入恶意包的任何机器都应被视为完全受感染。

## 四、通过开发者工具持久化

恶意软件一旦进入仓库，就会植入针对两个最常见开发者工具的持久化钩子：Claude Code和VS Code。这可能是真实攻击中滥用Claude Code钩子系统的首批记录案例之一。

### 4.1 Claude Code持久化

.claude/settings.json: 恶意软件在仓库的Claude Code设置中写入SessionStart钩子，matcher设置为"*"，指向node .vscode/setup.mjs。每次开发者在受感染的仓库中打开Claude Code时都会触发，无需工具使用或用户操作。

### 4.2 VS Code持久化

.vscode/tasks.json: 并行钩子通过runOn: folderOpen任务针对VS Code用户，每次打开项目文件夹时运行node .claude/setup.mjs。

### 4.3 setup.mjs Dropper

两个钩子都调用setup.mjs，这是一个自包含的Bun运行时引导程序。如果Bun未安装，它会从GitHub releases静默下载bun-v1.3.13，处理Linux x64/arm64/musl、macOS x64/arm64和Windows x64/arm64。然后执行.claude/router_runtime.js（完整的14.8MB有效载荷）并从/tmp清理。

### 4.4 恶意GitHub Actions工作流

如果恶意软件持有具有写入访问权限的GitHub令牌，它会将名为Formatter的工作流推送到受害者的仓库。每次推送时，它通过${{ toJSON(secrets) }}转储所有仓库密钥，并将其上传为可下载的Actions artifact，名为format-results。这些操作被固定到特定提交SHA以显得合法。

在CI期间收到受感染lightning包并持有写入权限令牌的任何仓库都应接受这些文件的审计。

## 五、妥协指标

### 5.1 提交消息

- 以EveryBoiWeBuildIsAWormyBoi开头的提交消息（死drop令牌载体，可通过GitHub提交搜索搜索）

### 5.2 GitHub仓库

- 描述为"A Mini Shai-Hulud has Appeared"的GitHub仓库（攻击者泄露仓库，可在GitHub上直接搜索）

### 5.3 受影响包

- lightning@2.6.2
- lightning@2.6.3

### 5.4 文件和系统工件

- _runtime/start.py: Python加载器，在导入时初始化有效载荷
- _runtime/router_runtime.js: 混淆的JavaScript有效载荷（14.8MB，Bun运行时）
- _runtime/: 添加到恶意包版本的目录
- .claude/router_runtime.js: 注入到受害者仓库的恶意软件副本
- .claude/settings.json: 注入到受害者仓库的Claude Code钩子配置
- .claude/setup.mjs: 注入到受害者仓库的dropper
- .vscode/tasks.json: 注入到受害者仓库的VS Code自动运行任务
- .vscode/setup.mjs: 注入到受害者仓库的dropper

## 六、安全建议

1. **立即检查**: 检查项目是否安装了受影响的版本（2.6.2或2.6.3）
2. **触发扫描**: 如果项目最近未扫描，请触发新扫描
3. **依赖过滤**: 检查依赖过滤器是否有匹配项。如果显示"No matching dependencies"，则表示项目未积极使用恶意依赖
4. **审计仓库**: 如果检测到匹配，还需要审计仓库中注入的文件（.claude/和.vscode/目录中的意外内容）
5. **凭据轮换**: 轮换可能存在于受影响环境中的任何GitHub令牌、云凭据或API密钥

任何在受影响窗口期间导入恶意包的机器都应被视为完全受感染。建议进行全面的安全审计和凭据轮换。

## 七、结论

这是一起严重供应���攻击事件，攻击者成功在上游包中植入恶意代码，影响了广泛使用的PyTorch Lightning框架。攻击者采用了多层次的数据窃取策略和跨平台传播能力，结合了对开发者工具的滥用，形成了复杂的攻击链。

建议所有使用lightning包的用户立即检查并更新到安全版本，同时对可能受影响的环境进行全面的安全审计。