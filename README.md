# AI Learning Roadmap

从后端工程师到 AI 应用开发的系统性学习记录。

## 目录结构

```
.
├── 01-llm-api-basics/    # LLM API 调用基础
├── 02-rag/               # RAG 检索增强生成
├── 03-agent/             # AI Agent 应用
├── 04-evaluation/        # LLM 应用评估
├── notes/                # 学习笔记
├── requirements.txt      # Python 依赖
└── README.md
```

## 快速开始

```bash
# 创建并激活虚拟环境
python -m venv venv
.\venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt

# 创建 .env 文件并填入 API Key:
# OPENAI_API_KEY=sk-xxx
```

## 学习路线

1. **LLM API 调用基础** -- Chat Completion、Streaming、Function Calling
2. **RAG（检索增强生成）** -- 文档分块、Embedding、向量检索、生成回答
3. **AI Agent** -- Tool Use、ReAct 模式、多工具编排
4. **评估** -- 生成质量评估、检索质量评估

## 笔记

`notes/` 目录下的学习笔记使用中文编写，覆盖了 LLM 基础概念、Prompt Engineering、RAG 技术、Agent 模式、向量数据库和 Evaluation 等主题。

## 环境要求

- Python 3.10+
- OpenAI API Key（或兼容的 API）
