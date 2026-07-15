 # AI Agent 模式
 
 ## 什么是 Agent
 Agent 是能够自主决策、使用工具、执行多步任务的 AI 系统。
 
 ## ReAct 模式
 1. 思考（Thought）-> 2. 行动（Action）-> 3. 观察（Observation）-> 重复 -> 最终答案
 
 ## Function Calling
 这是 Agent 的基础能力。LLM 能理解可用工具、选择合适的工具、提取参数。
 开发者只需定义 tool schema 并实现工具逻辑。
 
 ## 多工具编排
 ```
 用户："查 AI 新闻，翻译成英文，总结要点"
 Agent: search_news() -> translate_text() -> summarize_text()
 ```
 
 ## 挑战
 - 错误恢复：工具调用失败时能否优雅处理
 - 循环检测：Agent 反复执行同一操作
 - Token 消耗：多轮对话成本高
 - 安全边界：限制 Agent 的工具范围
 
 ## Agent vs 微服务编排
 Agent 的 Tool-Use 很像服务编排。区别在于 Agent 用自然语言做决策，执行路径不确定。
 主流框架：LangChain/LangGraph、CrewAI、AutoGen、OpenAI Assistants API。
