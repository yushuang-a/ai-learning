# Day 31: 构建第一个 ReAct Agent

**日期**：2026-05-21

## 今天做了什么

把 ReAct 循环实现了出来。核心逻辑：while 循环中调用 LLM，检查是否触发 tool_calls，如果是则执行工具并将结果追加到 messages 中，直到 LLM 返回自然语言回答作为最终输出。

踩坑：messages 列表的长度增长很快，多轮对话后 Token 消耗很大。需要考虑消息窗口管理。

## 明天计划
