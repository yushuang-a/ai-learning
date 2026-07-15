 # Prompt Engineering
 
 ## 核心原则
 1. **清晰具体**：模糊的 Prompt 得到模糊的回答
 2. **给出格式要求**：指定 JSON/表格等格式提升可用性
 3. **角色设定**："你是一名资深 Java 架构师..."
 4. **Few-shot 示例**：给几个输入输出示例，LLM 会按模式执行
 
 ## 高级技巧
 - **Chain-of-Thought（思维链）**：让 LLM 逐步推理，对复杂问题效果显著
 - **结构化 Prompt**：按 Role、Task、Constraints、Output Format 组织
 - **Prompt 注入防护**：明确告知 LLM 忽略后续的"系统指令"
 
 ## 常见误区
 - 不是越长的 Prompt 越好，关键信息要有优先级
 - 不要假设 LLM 知道上下文，每次调用提供必要背景
 - System Prompt 要在最前面，角色设定优先于具体任务
 
 写 Prompt 就像写接口文档：清晰、无歧义、给预期输出格式。
