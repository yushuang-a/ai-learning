# Day 10: 结构化 Prompt 输出

**日期**：2026-04-30

## 今天做了什么

要求 LLM 输出 JSON 格式，然后解析 JSON 做后续处理——这让我想起了后端 API 的 request/response 模式。用 `response_format={"type": "json_object"}` 可以强制 LLM 输出合法 JSON。

**代码**：写了一个 Prompt 模板管理器，支持变量替换和版本管理。

## 明天计划
