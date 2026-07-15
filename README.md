 # AI Learning Roadmap
 
 从 8 年 Java 后端工程师转型 AI 应用开发 —— 3 个月系统学习计划。
 
 ## 学习总览
 
 | 阶段 | 时间 | 核心内容 |
 |------|------|----------|
 | 基础期 | 第 1-4 周 | Python 生态、LLM API、Prompt Engineering、RAG |
 | 进阶期 | 第 5-8 周 | Agent 模式、评估体系、生产化部署 |
 | 实战期 | 第 9-12 周 | 项目实战、高级话题、面试准备 |
 
 详细计划见 [PLAN.md](/PLAN.md)。
 每天的学习记录见 [diary/](/diary/) 目录。
 
 ## 目录结构
 
 ```
 ├── PLAN.md              # 3 个月详细学习计划
 ├── diary/               # 每日学习日记（12 周 84 天）
 ├── code/                # 代码示例
 │   ├── 01-llm-basics/
 │   ├── 02-prompt-engineering/
 │   ├── 03-rag/
 │   ├── 04-agent/
 │   ├── 05-evaluation/
 │   └── 06-production/
 ├── notes/               # 系统性学习笔记
 ├── projects/            # 实战项目
 └── requirements.txt
 ```
 
 ## 如何使用
 
 ```bash
 python -m venv venv
 .\venv\Scripts\activate
 pip install -r requirements.txt
 # 创建 .env: OPENAI_API_KEY=sk-xxx
 ```
