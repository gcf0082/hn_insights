---
洞察链接: https://www.anthropic.com/glasswing
标题: Project Glasswing：为AI时代保障关键软件安全
发布来源: Anthropic
发布时间: 2026年4月
故事ID: 47679121
---

# Project Glasswing：为AI时代保障关键软件安全

## 项目简介

Anthropic宣布推出**Project Glasswing**，这是一项新的网络安全倡议，旨在保护全球最关键的软件系统。该项目汇集了Amazon Web Services、Apple、Broadcom、Cisco、CrowdStrike、Google、JPMorganChase、Linux Foundation、Microsoft、NVIDIA和Palo Alto Networks等科技巨头。

## 核心问题：AI模型的网络安全威胁

Claude Mythos Preview是Anthropic训练的一个前沿模型，它展现了一个严峻的事实：**AI模型已经达到了可以在发现和利用软件漏洞方面超越除最熟练的人类安全专家之外的所有人的水平**。

该模型已经发现了数千个高危漏洞，涵盖**每一个主流操作系统和主流网络浏览器**。随着AI技术的快速发展，这些能力将会迅速扩散，可能超出负责任部署这些能力的控制范围。

## 关键发现

Claude Mythos Preview自主发现的漏洞示例：

1. **OpenBSD 27年漏洞**：在以安全加固著称的安全操作系统OpenBSD中发现了一个允许攻击者远程崩溃任何运行该系统的机器的漏洞
2. **FFmpeg 16年漏洞**：在一条被自动化测试工具点击过500万次但从未发现问题的代码行中发现了漏洞
3. **Linux内核漏洞**：自主发现并链接了Linux内核中的多个漏洞，实现了从普通用户权限到完全控制机器的权限提升

## 合作伙伴响应

- **Cisco**：AI能力已经跨越了保护关键基础设施免受网络威胁所需的基本阈值，必须立即采用新方法
- **AWS**：每天分析超过400万亿个网络流量以发现威胁，AI是其大规模防御能力的核心
- **Microsoft**：在CTI-REALM基准测试中，Claude Mythos Preview相比之前的模型显示出实质性改进
- **CrowdStrike**：漏洞被发现和被攻击者利用之间的时间窗口已经崩溃——过去需要数月的事情现在只需几分钟
- **Linux Foundation**：为关键开源代码库的维护者提供新一代AI模型，主动识别和修复漏洞
- **Palo Alto Networks**：需要将这些模型交到开源维护者和各地防御者手中，在攻击者之前发现和修复这些漏洞

## Anthropic承诺

- **1亿美元**的Claude Mythos Preview模型使用额度，用于Project Glasswing和额外参与者
- **400万美元**直接捐赠给开源安全组织（250万美元给Alpha-Omega和OpenSSF，150万美元给Apache Software Foundation）
- 在90天内公开报告发现的漏洞和可披露的改进
- 与领先的安全组织合作，制定AI时代安全实践的实际建议

## 基准测试表现

| 基准测试 | Mythos Preview | Opus 4.6 |
|---------|---------------|----------|
| CyberGym（网络安全漏洞复现） | 83.1% | 66.6% |
| SWE-bench Verified | 93.9% | 80.8% |
| SWE-bench Pro | 77.8% | 53.4% |
| GPQA Diamond | 94.6% | 91.3% |

## 安全未来

Project Glasswing是起点。没有任何一个组织可以单独解决这些网络安全问题：前沿AI开发者、其他软件公司、安全研究人员、开源维护者和世界各国政府都有不可替代的作用。防御世界网络基础设施的工作可能需要数年时间；前沿AI能力可能在短短几个月内就会大幅提升。为了网络防御者能够取得优势，我们需要立即采取行动。
