# 洞察报告：使用 LM Studio 本地运行 Google Gemma 4

## 基本信息

- **洞察链接**：https://ai.georgeliu.com/p/running-google-gemma-4-locally-with
- **来源**：George Liu (Substack)
- **发布日期**：2026年4月4日
- **主题**：本地运行 Google Gemma 4 模型与 LM Studio CLI 及 Claude Code 集成

---

## 为什么要在本地运行模型？

云端 AI API 虽然好用，但存在以下问题：
- **速率限制**：API 调用次数受限
- **使用成本**：累计费用较高
- **隐私担忧**：数据离开本地机器
- **网络延迟**：依赖网络连接

本地模型的优势：
- **零 API 费用**：无需付费
- **数据隐私**：所有数据留在本地
- **稳定可用**：无需网络连接

## Google Gemma 4 模型系列

Google 发布了四个 Gemma 4 模型变体：

| 模型 | 参数 | 特点 |
|------|------|------|
| E2B | 2B | 面向设备端部署，支持音频输入 |
| E4B | 4B | 面向设备端部署，支持音频输入 |
| 26B-A4B | 26B 总参数，4B 激活 | **本文重点**：MoE 架构 |
| 31B | 31B | 最强能力，MMLU Pro 85.2% |

### 为什么选择 26B-A4B？

**关键在于混合专家（Mixture-of-Experts）架构**：
- 总参数 26B，但每次前向传播只激活 4B 参数
- 有效推理成本相当于 4B 密集模型，质量却接近 10B 级别
- 在 MMLU Pro 得分 82.6%，AIME 2026 得分 88.3%
- 与 31B 密集模型（85.2% 和 89.2%）接近，但运行速度更快

在 14 寸 MacBook Pro M4 Pro（48GB 统一内存）上：
- 生成速度：**51 tokens/秒**
- 内存占用：约 21GB（48K 上下文）
- 最大上下文：256K

## LM Studio 0.4.0 新功能

版本 0.4.0 引入了重大架构变化：

- **llmster daemon**：后台服务，管理模型加载和推理
- **lms CLI**：完整的命令行界面
- **并行请求处理**：连续批处理，支持多请求并发
- **有状态 REST API**：新增 `/v1/chat` 端点
- **MCP 集成**：本地模型上下文协议支持

## 安装步骤

```bash
# Linux/Mac
curl -fsSL https://lmstudio.ai/install.sh | bash

# 启动守护进程
lms daemon up

# 更新运行时
lms runtime update llama.cpp
lms runtime update mlx
```

## 下载和使用 Gemma 4

```bash
# 下载模型
lms get google/gemma-4-26b-a4b

# 查看已下载模型
lms ls

# 启动交互式聊天
lms chat google/gemma-4-26b-a4b --stats

# 查看加载的模型
lms ps
```

## 内存估算

| 上下文长度 | 内存需求 |
|------------|----------|
| 4K | ~17.6 GB |
| 48K | ~21 GB |
| 128K | ~28 GB |
| 256K | ~37 GB |

## 模型调优参数

### 上下文长度
```bash
lms load google/gemma-4-26b-a4b --context-length 128000
```

### GPU 卸载
```bash
# 强制全 GPU 卸载
lms load google/gemma-4-26b-a4b --gpu=1.0

# 最大化卸载
lms load google/gemma-4-26b-a4b --gpu=max
```

### TTL 自动卸载
```bash
# 30分钟空闲后自动卸载
lms load google/gemma-4-26b-a4b --ttl 1800
```

## 与 Claude Code 集成

创建 shell 函数配置本地模型：

```bash
claude-lm() {
    export ANTHROPIC_BASE_URL=http://localhost:1234
    export ANTHROPIC_AUTH_TOKEN=lmstudio
    export ANTHROPIC_MODEL="gemma-4-26b-a4b"
    # ... 其他配置
    claude "$@"
}
```

## 关键结论

1. **MoE 模型是本地推理的最佳选择**：26B-A4B 架构以 4B 推理成本提供接近 10B 的质量

2. **无头守护进程改变工作流**：0.4.0 版本支持纯 CLI 操作，适合服务器部署

3. **上下文长度是主要内存变量**：模型本身占用固定 ~17.6GB，线性扩展

4. **Anthropic 兼容端点是重大变革**：可以本地运行 Claude Code

## 注意事项

- Gemma 4 在 `lms chat` 中不会自报名称
- 48GB 机器内存压力较大，建议 64GB+ 配置
- 本地模型不适合依赖扩展思考的复杂多步骤任务

---

*报告生成时间：2026-04-06*
