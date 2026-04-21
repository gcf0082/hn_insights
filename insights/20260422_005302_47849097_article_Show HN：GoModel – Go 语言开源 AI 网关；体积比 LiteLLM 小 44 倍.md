# GoModel - AI 网关洞察报告

## 基本信息

| 项目 | 详情 |
|------|------|
| **洞察链接** | https://github.com/ENTERPILOT/GOModel/ |
| **项目名称** | GoModel |
| **所有者** | ENTERPILOT |
| **描述** | 用 Go 编写的高性能 AI 网关，统一 OpenAI 兼容 API |
| **Star** | 172 |
| **Fork** | 13 |
| **最新版本** | v0.1.19 (2026-04-21) |
| **许可证** | MIT |
| **主要语言** | Go 83.1%, JavaScript 11.6% |

## 核心功能

GoModel 是一个高性能 AI 网关，支持多个 LLM 提供商的统一接入：

| 提供商 | 支持功能 |
|--------|----------|
| **OpenAI** | Chat、Responses、Embeddings、Files、Batches、Passthru |
| **Anthropic** | Chat、Responses、Passthru |
| **Google Gemini** | Chat、Responses、Embeddings、Files、Batches |
| **Groq** | Chat、Responses、Embeddings、Files、Batches |
| **OpenRouter** | 全部功能 |
| **xAI (Grok)** | Chat、Responses、Embeddings、Files、Batches |
| **Azure OpenAI** | 全部功能 |
| **Ollama** | Chat、Responses、Embeddings |

## 主要特性

1. **统一 OpenAI 兼容 API** - 一次对接，多提供商切换
2. **响应缓存** - 两层缓存（精确匹配 + 语义相似），可降低 60-70% API 成本
3. **Guardrails** - 可配置的安全防护管道
4. **流式响应** - 支持实时流式输出
5. **可观测性** - Prometheus 指标、审计日志、仪表盘
6. **存储后端** - 支持 SQLite、PostgreSQL、MongoDB

## API 端点

- `/v1/chat/completions` - 聊天补全
- `/v1/embeddings` - 文本嵌入
- `/v1/files` - 文件管理
- `/v1/batches` - 批量处理
- `/p/{provider}/...` - 提供商直连
- `/admin/dashboard` - 管理仪表盘

## 快速部署

```bash
docker run --rm -p 8080:8080 \
  -e OPENAI_API_KEY="your-key" \
  enterpilot/gomodel
```

## 技术栈

- **语言**: Go 1.26.2+
- **框架**: 高性能 HTTP 服务
- **缓存**: Redis + 向量数据库（Qdrant/Pgvector/Pinecone/Weaviate）
- **部署**: Docker、Docker Compose、Kubernetes (Helm)

## 路线图 (0.2.0)

- 智能路由
- 预算管理
- 更广泛的提供商支持（Cohere、DeepSeek V3）
- 完整的 Responses/Conversations API 支持
- 集群模式

## 总结

GoModel 是一个生产级别的 AI 网关解决方案，提供统一 API 接口访问多个 LLM 提供商，具有高性能、缓存优化、可观测性和安全防护等企业级特性。相比 LiteLLM，它更轻量且专注于统一 API 层。对于需要灵活切换 LLM 提供商或构建内部 AI 平台的开发者来说是一个值得关注的开源项目。