---
title: GlycemicGPT - 开源糖尿病管理平台
date: 2025-05-15
source: GitHub
url: https://github.com/GlycemicGPT/GlycemicGPT
---

# GlycemicGPT 洞察报告

## 项目基本信息

**项目名称**: GlycemicGPT  
**GitHub地址**: https://github.com/GlycemicGPT/GlycemicGPT  
**项目描述**: 开源糖尿病管理平台，以AI驱动的分析为核心  
**Slogan**: "因为没有人应该独自管理糖尿病"  
**最新版本**: v0.7.2 (2025年5月13日)  
**Stars**: 93  
**License**: GPL-3.0

## 项目概述

GlycemicGPT是一个开源的糖尿病管理平台，以人工智能分析为核心功能。它能够直接连接用户的连续血糖监测仪(CGM)和胰岛素泵，提供完整的独立使用体验——实时监控、每日AI简报、模式检测、对话式AI聊天以及护理人员警报功能。

对于已经使用Nightscout的用户，GlycemicGPT也可以从现有的Nightscout实例中获取数据并在其基础上添加AI分析，无需更改当前设置。

## 核心功能

1. **AI驱动分析**
   - 每日AI简报
   - 餐食分析
   - 模式识别
   - BYOAI架构——支持自选AI提供商(Claude、OpenAI、Ollama等)

2. **设备连接**
   - Dexcom G7 CGM云API连接(已验证)
   - Tandem t:slim X2胰岛素泵BLE直连+云API(已验证)
   - Tandem Mobi胰岛素泵协议兼容(未验证)

3. **实时监控**
   - 血糖实时监控与趋势图
   - Time in Range跟踪
   - 可配置警报与护理人员升级
   - 多渠道通知(Telegram、推送、应用内)

4. **移动应用**
   - Android手机应用(Kotlin + Jetpack Compose)
   - Wear OScompanion应用与表盘

5. **数据存储**
   - 最长10年个人糖尿病数据存储
   - 可打印报告(内分泌科就诊用)

## 技术架构

| 组件 | 技术 |
|------|------|
| 前端 | Next.js 15, React 19, Tailwind CSS, shadcn/ui |
| 后端 | FastAPI, Python 3.12 |
| 移动端 | Kotlin, Jetpack Compose, BLE |
| Wear OS | Kotlin, Wear Compose, Watch Face |
| AI Sidecar | TypeScript, Express, 多提供商代理 |
| 数据库 | PostgreSQL 16, SQLAlchemy 2.0 |
| 缓存 | Redis 7 |

## 部署方式

- Docker自托管(推荐)
- Kubernetes(Kustomize)
- 云VPS + Caddy自动HTTPS
- Cloudflare Tunnel(家庭服务器，无需端口转发)

## 重要安全声明

⚠️ **软件非医疗设备**：本软件**不**旨在取代内分泌科医生或医疗保健提供者。GlycemicGPT仅提供AI生成的建议，应作为专业医疗护理的补充工具使用。

⚠️ **AI局限性**：AI会犯错，可能产生幻觉、误解数据、提供过时信息或缺乏上下文。

⚠️ **Alpha软件**：该项目正在积极开发中，虽然功能正常且开发者日常使用，但尚未经过广泛测试。

## 关键原则

- **仅提供建议**——不控制医疗设备
- **BYOAI架构**——自选AI提供商
- **自托管**——数据保留在用户基础设施上
- **安全第一**——预验证层、紧急升级、医学免责声明

## 社区资源

- Discord社区: https://discord.gg/QbyhCQKDBs
- 官方网站: https://glycemicgpt.org
- 资金支持: Open Collective

## 结论

GlycemicGPT是一个创新性的开源糖尿病管理项目，将AI技术与糖尿病监测设备相结合，为糖尿病患者提供智能化的管理工具。虽然该项目处于Alpha阶段且明确声明不替代专业医疗护理，但它为糖尿病社区提供了一个有价值的开源选择，尤其适合技术能力强、愿意参与项目开发的用户。