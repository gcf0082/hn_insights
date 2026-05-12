# DeepSeek V4 Flash 本地推理引擎 ds4.c 洞察报告

## 基本信息

| 项目 | 内容 |
|------|------|
| **项目名称** | ds4 (DeepSeek 4 Flash) |
| **仓库地址** | https://github.com/antirez/ds4 |
| **作者** | antirez (Redis 作者) |
| **编程语言** | C (55.4%), Objective-C (30.2%), Metal (13.8%) |
| **星标数** | 312 |
| **Fork 数** | 12 |
| **许可证** | MIT |
| **提交数** | 7 |

## 项目概述

ds4.c 是一个专为 DeepSeek V4 Flash 模型打造的本地推理引擎，仅支持 Metal (Apple GPU)。该项目基于 llama.cpp 和 GGML 构建，但不做为通用 GGUF 加载器使用，而是针对 DeepSeek V4 Flash 的特定张量布局、量化方式和元数据进行专门优化。

## 核心特性

### 1. 模型优势

- **高速推理**：相比更小的稠密模型，DeepSeek V4 Flash 因活跃参数更少而速度更快
- **高效思维模式**：启用思维模式时，生成的思考内容比其他模型短得多（有时仅为 1/5），且长度与问题复杂度成正比
- **超长上下文**：支持 100 万 token 的上下文窗口
- **知识深度**：284B 参数相比 27B/35B 模型在知识边缘表现更优
- **语言质量**：英文和意大利文写作质量接近前沿模型水平
- **KV Cache 压缩**：压缩率极高，支持在本地计算机上进行长上下文推理，并可将 KV Cache 持久化到磁盘
- **2-bit 量化**：通过特殊非对称量化（路由 MoE 专家使用 IQ2_XXS/Q2_K，其余保持原始精度），可在 128GB 内存的 MacBook 上运行

### 2. 技术架构

- **Metal 专用**：仅支持 Apple Metal 后端，CPU 代码仅用于正确性验证（存在 macOS 虚拟内存 bug 会导致内核崩溃）
- **KV Cache 磁盘化**：将 KV Cache 视为磁盘一等公民，利用现代 MacBook 的高速 SSD
- **GGUF 专用格式**：仅支持为本项目特制的 GGUF 文件，不兼容通用的 DeepSeek/GGUF 文件

### 3. 性能数据

| 机器配置 | 提示类型 | 预填充速度 | 生成速度 |
|----------|----------|------------|----------|
| MacBook Pro M3 Max, 128GB | 短提示 | 58.52 t/s | 26.68 t/s |
| MacBook Pro M3 Max, 128GB | 11709 tokens | 250.11 t/s | 21.47 t/s |
| Mac Studio M3 Ultra, 512GB | 短提示 | 84.43 t/s | 36.86 t/s |
| Mac Studio M3 Ultra, 512GB | 11709 tokens | 468.03 t/s | 27.39 t/s |

### 4. 工具支持

- **CLI 工具** (`./ds4`)：支持单次提示和交互式多轮对话，命令包括 `/help`, `/think`, `/nothink`, `/ctx N` 等
- **Server 工具** (`./ds4-server`)：提供 OpenAI 和 Anthropic 兼容的 HTTP API，支持 SSE 流式传输
- **Agent 集成**：可与 opencode、Pi、Claude Code 等本地编码代理配合使用

### 5. 磁盘 KV Cache

- 通过 SHA1 哈希缓存 token 前缀，支持跨会话恢复
- 缓存文件格式包含固定头部、渲染文本和 DS4 会话负载
- 支持冷保存、继续保存、驱逐保存和关闭保存四种时机

## 使用方式

### 下载模型

```bash
./download_model.sh q2   # 128GB 内存机器
./download_model.sh q4   # >= 256GB 内存机器
```

### 启动服务

```bash
./ds4-server --ctx 100000 --kv-disk-dir /tmp/ds4-kv --kv-disk-space-mb 8192
```

### API 调用示例

```bash
curl http://127.0.0.1:8000/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{
    "model":"deepseek-v4-flash",
    "messages":[{"role":"user","content":"List three Redis design principles."}],
    "stream":true
  }'
```

## 项目愿景

项目的愿景是让本地推理成为三个组件完美协作的整体：
1. 带 HTTP API 的推理引擎
2. 专为特定引擎和假设优化的 GGUF 文件
3. 通过编码代理实现测试和验证

## 总结

ds4.c 是一个专注于 DeepSeek V4 Flash 的本地推理引擎，充分利用了 Apple Silicon 的 Metal 能力和该模型独特的 KV Cache 压缩技术。项目体现了 antirez 对本地 AI 推理的深入思考，特别是将 KV Cache 从 RAM 扩展到磁盘的理念。虽然代码由 GPT 5.5 大量辅助开发（alpha 质量），但对于拥有大内存 Mac 设备的开发者来说，这是一个值得关注的本地大模型推理方案。