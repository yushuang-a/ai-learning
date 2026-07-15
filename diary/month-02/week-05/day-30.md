# Day 30: Function Calling 深入

**日期**：2026-05-20

## 今天做了什么

今天深入研究了 Function Calling 的参数传递机制。Tool 的 parameters 是 JSON Schema 格式，支持嵌套对象、枚举、数组等复杂类型。

实现了一个并行调用的场景：用户同时问天气和股价，LLM 一次返回两个 tool_calls，并行执行后再交给 LLM 合并回答。

## 明天计划
