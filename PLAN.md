 # 3 个月 AI 应用开发学习计划
 
 本计划假设你已掌握 Java 后端开发（8 年经验），目标是转型 AI 应用开发。
 每天投入约 2-3 小时，周末可加倍。
 
 ## Month 1: 基础期（第 1-4 周）
 
 **目标**：掌握 LLM API 调用、Prompt Engineering、RAG 技术栈，能独立搭建 RAG 系统。
 
 ### Week 1: Python + LLM API
 | Day | 主题 | 内容 |
 |-----|------|------|
 | 1 | Python 热身 | 类型注解、async/await、pydantic、dotenv |
 | 2 | Chat Completion | 首次 LLM API 调用、System/User 角色 |
 | 3 | 流式输出 | Streaming 实现、可中断机制 |
 | 4 | Function Calling | Tool Use 定义与执行 |
 | 5 | 错误处理 | Rate Limit、Retry、超时 |
 | 6 | CLI Chat 助手 | 周末实战：多轮对话 |
 | 7 | 复习回顾 | 梳理知识点 |
 
 ### Week 2: Prompt Engineering
 | Day | 主题 | 内容 |
 |-----|------|------|
 | 8 | Prompt 基础 | 角色设定、格式控制 |
 | 9 | Few-shot & CoT | 示例学习、思维链 |
 | 10 | 结构化 Prompt | JSON、表格输出控制 |
 | 11 | 安全防护 | 注入防护、输出过滤 |
 | 12 | 模板工程 | 可复用 Prompt 模板 |
 | 13 | 模型对比 | GPT-4o vs Claude vs DeepSeek |
 | 14 | 复习回顾 | 梳理知识点 |
 
 ### Week 3: RAG 基础
 | Day | 主题 | 内容 |
 |-----|------|------|
 | 15 | RAG 概念 | 原理、与传统搜索的差异 |
 | 16 | 文档分块 | Chunking 策略对比 |
 | 17 | Embedding | 文本向量化、模型选型 |
 | 18 | 向量数据库 | Chroma 入门 |
 | 19 | 首个 RAG | 完整 Pipeline 搭建 |
 | 20 | 检索优化 | Hybrid Search |
 | 21 | 复习回顾 | 梳理知识点 |
 
 ### Week 4: RAG 系统构建
 | Day | 主题 | 内容 |
 |-----|------|------|
 | 22 | Query 改写 | 多角度改写策略 |
 | 23 | Reranking | Cross-encoder 排序 |
 | 24 | 高级检索 | Multi-query、Self-RAG |
 | 25 | 项目搭建 | 知识库问答系统 |
 | 26 | 项目完善 | UI、测试、部署 |
 | 27 | 性能调优 | 延迟、缓存、成本 |
 | 28 | Month 1 总结 | 复盘与查漏补缺 |
 
 ## Month 2: 进阶期（第 5-8 周）
 
 **目标**：掌握 Agent 模式、评估体系、生产化部署。
 
 ### Week 5: Agent 入门
 | Day | 主题 | 内容 |
 |-----|------|------|
 | 29 | Agent 概念 | ReAct 模式详解 |
 | 30 | Function Calling 深入 | 复杂参数、并行调用 |
 | 31 | 构建 Agent | 带推理的工具调用 |
 | 32 | Agent 记忆 | 对话历史管理 |
 | 33 | 错误恢复 | Agent 异常处理 |
 | 34 | 研究助手 | 周末实战 |
 | 35 | 复习回顾 | 梳理知识点 |
 
 ### Week 6: 高级 Agent
 | Day | 主题 | 内容 |
 |-----|------|------|
 | 36 | 多工具编排 | 工具链设计 |
 | 37 | LangGraph 入门 | 有向图工作流 |
 | 38 | 多 Agent 系统 | CrewAI 协作模式 |
 | 39 | Web 搜索集成 | Tavily / SerpAPI |
 | 40 | 可观测性 | Tracing、Logging |
 | 41 | 工作流 Agent | 周末实战 |
 | 42 | 复习回顾 | 梳理知识点 |
 
 ### Week 7: 评估体系
 | Day | 主题 | 内容 |
 |-----|------|------|
 | 43 | 评估价值 | 如何建立评估集 |
 | 44 | 检索评估 | Precision、Recall、MRR |
 | 45 | 生成评估 | 准确性、忠实度 |
 | 46 | LLM-as-Judge | 自动化评估 |
 | 47 | 评估 Pipeline | 持续评估框架 |
 | 48 | 对比实验 | Chunking/Model 对比 |
 | 49 | 复习回顾 | 梳理知识点 |
 
 ### Week 8: 生产部署
 | Day | 主题 | 内容 |
 |-----|------|------|
 | 50 | 缓存策略 | Redis / 语义缓存 |
 | 51 | 成本控制 | Token 追踪、模型路由 |
 | 52 | 监控告警 | LangSmith / 自定义 |
 | 53 | API 网关 | 限流、鉴权、灰度 |
 | 54 | Docker 部署 | 容器化 AI 应用 |
 | 55 | 压测优化 | 周末实战 |
 | 56 | Month 2 总结 | 复盘与查漏补缺 |
 
 ## Month 3: 实战期（第 9-12 周）
 
 **目标**：完成可展示的项目，覆盖面试知识体系。
 
 ### Week 9: 项目启动
 | Day | 主题 | 内容 |
 |-----|------|------|
 | 57 | 项目设计 | 需求分析、架构设计 |
 | 58 | 数据处理 | 文档清洗、分块 |
 | 59 | RAG 实现 | Embedding + 检索 |
 | 60 | Agent 集成 | 对话 Agent 对接 |
 | 61 | 评估搭建 | 评估集 + Pipeline |
 | 62 | 第一版完成 | 功能联调 |
 | 63 | 复习回顾 | 梳理知识点 |
 
 ### Week 10: 项目打磨
 | Day | 主题 | 内容 |
 |-----|------|------|
 | 64 | 性能优化 | 延迟、召回率 |
 | 65 | 前端 / API | Streamlit / FastAPI |
 | 66 | 测试 | 单元、集成、E2E |
 | 67 | 文档 | README、API 文档 |
 | 68 | 部署上线 | Docker + Cloud |
 | 69 | 演示准备 | Demo 视频、截图 |
 | 70 | 复习回顾 | 梳理知识点 |
 
 ### Week 11: 高级话题
 | Day | 主题 | 内容 |
 |-----|------|------|
 | 71 | 微调基础 | LoRA 概念、数据集准备 |
 | 72 | 多模态 | Vision、Whisper 集成 |
 | 73 | LangChain 深入 | LCEL、Callback |
 | 74 | MCP 协议 | 工具服务化 |
 | 75 | RAGAS | 高级评估框架 |
 | 76 | 前沿探索 | Agents、MCP 生态 |
 | 77 | 复习回顾 | 梳理知识点 |
 
 ### Week 12: 求职冲刺
 | Day | 主题 | 内容 |
 |-----|------|------|
 | 78 | 简历优化 | AI 应用岗简历 |
 | 79 | 面试题 | Agent、RAG、System Design |
 | 80 | System Design | AI 应用架构设计 |
 | 81 | 模拟面试 | 自我演练 |
 | 82 | 最终整理 | 项目、笔记、博客 |
 | 83 | 投递启动 | 岗位筛选、投递 |
 | 84 | 毕业总结 | 复盘与下一步 |
