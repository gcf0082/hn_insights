---
title: ChatGPT 浏览器状态检测技术分析
date: 2026-03-29
source: Buchodi Threat Intel
url: https://www.buchodi.com/chatgpt-wont-let-you-type-until-cloudflare-reads-your-react-state-i-decrypted-the-program-that-does-it/
---

# ChatGPT 直至 Cloudflare 读取 React 状态才允许输入 - 深度技术分析

## 基本信息

- **发布日期**: 2026年3月29日
- **来源**: Buchodi's Threat Intel
- **作者**: Jamie Larson
- **原文链接**: https://www.buchodi.com/chatgpt-wont-let-you-type-until-cloudflare-reads-your-react-state-i-decrypted-the-program-that-does-it/

## 内容摘要

本文揭示了 ChatGPT 每条消息发送时都会触发 Cloudflare Turnstile 验证程序在浏览器后台静默运行。作者通过解密网络流量中获取的 377 个程序样本，发现其检测范围远超标准浏览器指纹识别。

### 核心发现

Turnstile 程序检查 **55 个属性**，涵盖三个层面：

1. **浏览器层面**: GPU、屏幕、字体等8项WebGL属性、8项屏幕属性、5项硬件属性、4项字体测量、8项DOM探测、5项存储检查
2. **Cloudflare 网络层面**: 城市、IP、区域等边缘服务器注入的头部信息
3. **ChatGPT React 应用层面**: `__reactRouterContext`、`loaderData`、`clientBootstrap` - 这些属性只有在 ChatGPT React 应用完全渲染和水合后才会存在

### 加密机制

Turnstile 字节码以加密形式到达，使用 `turnstile.dx` 字段（28,000 个 base64 字符，每次请求都会变化）。解密流程：

```
1. 从 prepare 请求中读取 p token
2. 从 prepare 响应中读取 turnstile.dx
3. XOR(base64decode(dx), p) → 外部字节码（89条指令）
4. 在19KB blob后找到5参数指令 → 最后一个参数是密钥
5. XOR(base64decode(blob), str(key)) → 内部程序（417-580条VM指令）
```

关键发现：XOR 密钥是服务器生成的浮点数，直接嵌入在字节码中。作者在 50 次请求中验证了这一点，成功率 100%。

### 其他验证机制

1. **Signal Orchestrator**（271条指令）: 安装事件监听器监控 36 个 `window.__oai_so_*` 属性，包括按键时序、鼠标速度、滚动模式、闲置时间等行为生物特征

2. **工作量证明（PoW）**: 25 字段指纹 + SHA-256 hashcash，72% 在 5ms 内解决，并非真正防御

### 关键结论

- 伪造浏览器指纹但未实际渲染 ChatGPT SPA 的机器人将会失败
- 真正的检测在应用层而非浏览器层
- XOR 密钥是服务器生成的明文嵌入，隐私边界取决于策略而非加密
- 混淆的目的是防止静态分析、阻止网站运营商读取原始指纹值、防止令牌重放

## 统计数据

| 指标 | 数值 |
|------|------|
| 解密程序数 | 377/377 (100%) |
| 观察到的唯一用户 | 32 |
| 每程序属性数 | 55（所有样本一致） |
| 每程序指令数 | 417-580（平均480） |
| 唯一XOR密钥（50样本） | 41 |
| SO行为属性 | 36 |
| PoW指纹字段 | 25 |
| PoW解决时间 | 72% < 5ms |

## 方法论说明

- 未在未授权情况下访问任何系统
- 未披露任何个人用户数据
- 所有流量来自同意参与者
- Sentinel SDK 经过美化后手动去混淆
- 所有解密使用 Python 离线完成
