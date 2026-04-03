# Hypura 项目洞察报告

## 基本信息

- **项目链接**: https://github.com/t8/hypura
- **项目名称**: Hypura
- **项目描述**: 在 Apple Silicon 上运行超出内存容量的大型语言模型
- **星标数**: 173
- **编程语言**: Rust (91.8%), Shell (5.4%), C (2.8%)
- **许可证**: MIT
- **发布日期**: 2026年3月17日

## 项目概述

Hypura 是一个存储层感知的 LLM 推理调度器，专为 Apple Silicon 设计。它能够根据访问模式、带宽成本和硬件能力，将模型张量放置在 GPU、RAM 和 NVMe 三个存储层上，从而使超出物理内存的模型能够运行而不会崩溃系统。

## 核心功能

### 1. 内存分层管理

Hypura 智能地将模型张量分配到三个存储层：

- **GPU (Metal)**: 注意力层、归一化层和嵌入层。访问速度最快，受限于 `recommendedMaxWorkingSetSize`
- **RAM**: 溢出层，通过 mmap 访问
- **NVMe**: 剩余层，通过直接 I/O (`F_NOCACHE` + `pread`) 按需加载

### 2. 推理模式

Hypura 根据模型大小、架构和可用内存自动选择最佳推理模式：

- **全驻留模式 (Full-resident)**: 模型适合 GPU+RAM，无需 NVMe I/O，达到完整 Metal 速度
- **专家流式模式 (Expert-streaming)**: 适用于 MoE 模型（如 Mixtral），仅保留非专家张量（约 1GB）在 GPU 上，专家张量从 NVMe 流式传输，通过神经元缓存实现 99.5% 的命中率
- **密集 FFN 流式模式 (Dense FFN-streaming)**: 适用于无法放入 GPU 的密集模型（如 Llama 70B），注意力+归一化保留在 GPU 上（约 8GB），FFN 张量从 NVMe 流式传输

### 3. 性能表现

在 M1 Max, 32GB 统一内存, ~5.1GB/s NVMe 顺序读取的测试环境下：

| 模型 | 大小 | GPU | NVMe | 模式 | Hypura | llama.cpp |
|------|------|-----|------|------|--------|-----------|
| Qwen 2.5 14B Q4_K_M | 8.4 GB | 8.4 GB | - | 全驻留 | 21 tok/s | ~21 tok/s |
| Mixtral 8x7B Q5_K_M | 30.9 GB | 1.1 GB | 29.8 GB | 专家流式 | 2.2 tok/s | OOM |
| Llama 3.3 70B Q4_K_M | 39.6 GB | 7.8 GB | 31.8 GB | 密集FFN流式 | 0.3 tok/s | OOM |

### 4. Ollama 兼容服务器

Hypura 提供 Ollama 兼容的 HTTP API，可作为任何 Ollama 工具的即插即用替代品，支持 `/api/generate` 和 `/api/chat` 端点。

## 技术架构

Hypura 是一个 Cargo 工作区，包含两个 crate：

- **`hypura`**: 主二进制文件和库，包含 CLI 和核心逻辑
- **`hypura-sys`**: llama.cpp 的 FFI 绑定

关键模块：
- `scheduler/placement.rs`: LP + 贪心张量放置
- `compute/inference.rs`: 推理引擎
- `compute/nvme_backend.rs`: 自定义 GGML 缓冲类型，池式专家/FFN 流式传输
- `server/routes.rs`: Axum HTTP 处理器

## 安全说明

- SSD 不会损坏：Hypura 仅从 SSD 读取数据，从不写入
- `bench --baseline` 在模型超过 RAM 减去 4GB 头部空间时被阻止
- 建议在未经测试的模型上先使用 `--max-tokens 10`

## 总结

Hypura 是一个创新性的项目，通过利用 Apple Silicon 的统一内存架构和 NVMe 存储扩展能力，使消费级硬件能够运行超出物理内存的大型语言模型。对于适合内存的模型，Hypura 零开销；对于无法放入内存的模型，Hypura 是"能运行"和"崩溃"之间的唯一区别。
