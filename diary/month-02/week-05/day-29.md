# Day 29: Agent 概念与 ReAct 模式

**日期**：2026-05-19

## 今天做了什么

Agent 最核心的思想就是 ReAct：Reasoning + Acting。LLM 先思考需要做什么，然后执行工具调用，观察结果，再决定下一步。这打破了传统 LLM 的"一问一答"模式。

从后端视角理解：Agent 的 Thought-Action-Observation 循环 ≈ 工作流引擎中的状态机。每一步的状态由 LLM 的动态推理决定，而不是写死的有向图。

## 明天计划
