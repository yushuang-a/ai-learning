 # LLM 基础概念
 
 ## 什么是 LLM
 LLM（Large Language Model）是基于 Transformer 架构、在海量文本上训练的大语言模型，核心能力是理解和生成自然语言。
 
 ## 关键概念
 
 **Token**：LLM 处理文本的最小单位。中文场景一个汉字通常对应 1-2 个 Token。API 按 Token 计费。
 
 **Context Window（上下文窗口）**：LLM 一次能处理的 Token 数量上限，常见 8K/16K/128K 等。
 
 **Temperature**：控制输出随机性。0-2 范围，事实性任务用低值（0.1-0.3），创意性任务用高值（0.7-0.9）。
 
 **System / User / Assistant Prompt**：分别对应角色设定、用户输入、AI 回复。
 
 ## 常见模型
 - GPT-4o / GPT-4o-mini：OpenAI 主力，性价比高
 - Claude 3.5 Sonnet：Anthropic，代码能力强
 - DeepSeek-V3：国内优秀模型，性价比极高
 
 ## 从 Java 开发者理解 LLM
 - API = RESTful 接口
 - Context Window = 缓存上限
 - Token = 带宽计费单位
 - Temperature = 规则执行的严格程度
 
 作为后端开发者，理解这些类比后，LLM API 没有特别复杂的地方。
