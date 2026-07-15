# Day 17: Embedding 模型

**日期**：2026-05-07

## 今天做了什么

今天把文本向量化。OpenAI 的 text-embedding-3-small 返回 1536 维向量。

用余弦相似度计算了两个文本的相似度。"RAG 是什么"和"RAG 的工作原理"的相似度是 0.87，而"RAG 是什么"和"今天天气不错"是 0.12——效果很直观。

经验：Embedding 模型的选型上，text-embedding-3-small 足够了。除非中文场景特别多，可能需要考虑 bge-m3。

## 明天计划
