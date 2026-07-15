# Day 40: Agent 可观测性

**日期**：2026-05-30

## 今天做了什么

Agent 的执行路径不确定，调试很难。加了一层日志：记录每一轮的 Thought、Action、Observation。

还实现了调用链追踪：每个请求分配一个 trace_id，方便后续分析。

## 明天计划
