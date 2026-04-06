# Parlor：端侧实时多模态AI应用

**洞察链接**: https://github.com/fikrikarim/parlor  
**项目名称**: Parlor  
**类型**: 开源项目  
** stars**: 592  
** forks**: 37  
**许可证**: Apache 2.0  

---

## 项目概述

Parlor 是一个端侧运行的实时多模态AI应用，让用户能够通过语音和视觉与本地运行的AI进行自然对话。该项目使用 Google 的 Gemma 4 E2B 模型进行语音和视觉理解，使用 Kokoro 进行文本转语音。用户可以直接对着麦克风说话、打开摄像头，AI 就会实时回复，所有计算都在本地设备上完成，无需任何服务器成本。

该项目最初是为了解决作者自托管免费语音AI服务的可持续性问题。通过将所有计算转移到用户设备上运行，完全消除了服务器成本。作者的目标是让人们可以在手机等移动设备上运行这类AI，实现看图说话、多语言对话等功能。

---

## 技术架构

### 系统流程

```
浏览器（麦克风 + 摄像头）
    │
    │  WebSocket（音频PCM + JPEG帧）
    ▼
FastAPI 服务器
    ├── Gemma 4 E2B（通过LiteRT-LM在GPU上运行）→ 理解语音和视觉
    └── Kokoro TTS（Mac上使用MLX，Linux上使用ONNX）→ 语音回复
    │
    │  WebSocket（流式音频块）
    ▼
浏览器（播放 + 转录文本）
```

### 核心技术组件

**语音理解**: 采用 Gemma 4 E2B 模型，能够实时处理语音输入和视觉信息。  
**语音合成**: 使用 Kokoro TTS 模型，在 Apple Silicon 上通过 MLX 加速，在 Linux 上通过 ONNX 运行。  
**语音活动检测**: 浏览器端使用 Silero VAD 实现免提操作，无需按键说话。  
**打断功能**: 用户可以在AI说话中途随时打断它。  
**流式TTS**: 句子级别的音频流式播放，音频在完整响应生成之前就开始播放。

### 性能表现（Apple M3 Pro）

| 阶段 | 时间 |
|------|------|
| 语音+视觉理解 | ~1.8-2.2秒 |
| 响应生成（约25个token）| ~0.3秒 |
| 文本转语音（1-3句）| ~0.3-0.7秒 |
| **端到端总耗时** | **~2.5-3.0秒** |

解码速度：约83 tokens/秒（在Apple M3 Pro GPU上）。

---

## 需求与环境

### 运行要求

- Python 3.12+
- macOS Apple Silicon 或 Linux（需支持GPU）
- 约3GB可用内存（用于模型加载）

### 快速开始

```bash
git clone https://github.com/fikrikarim/parlor.git
cd parlor
cd src
uv sync
uv run server.py
```

然后打开 http://localhost:8000 ，授予摄像头和麦克风权限即可开始对话。首次运行时会自动下载模型（约2.6GB的Gemma 4 E2B加上TTS模型）。

---

## 项目结构

```
src/
├── server.py              # FastAPI WebSocket服务器 + Gemma 4推理
├── tts.py                 # 平台感知的TTS（Mac用MLX，Linux用ONNX）
├── index.html             # 前端UI（VAD、摄像头、音频播放）
├── pyproject.toml         # 依赖管理
└── benchmarks/
    ├── bench.py           # 端到端WebSocket基准测试
    └── benchmark_tts.py   # TTS后端对比
```

---

## 技术亮点

1. **完全本地运行**: 所有AI计算都在用户设备上完成，无需云端服务器，保护隐私且无运营成本。

2. **多模态交互**: 同时支持语音输入和视觉输入，可以边看边聊。

3. **实时响应**: 端到端延迟仅2.5-3秒，支持打断和流式音频。

4. **跨平台支持**: 在Apple Silicon Mac和Linux GPU上都能运行。

5. **免提操作**: 集成语音活动检测，无需按键即可开始对话。

---

## 技术栈

- **后端框架**: FastAPI
- **AI模型**: Gemma 4 E2B（Google DeepMind）
- **推理运行时**: LiteRT-LM（Google AI Edge）
- **语音合成**: Kokoro TTS（Hexgrad）
- **语音活动检测**: Silero VAD
- **macOS加速**: MLX
- **Linux加速**: ONNX

---

## 许可证

Apache 2.0

---

*本文档由 hn_insights 自动生成*