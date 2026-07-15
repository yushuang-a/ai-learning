"""
Basic RAG Pipeline
"""
import os
from openai import OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

DOCS = [
    "RAG is Retrieval-Augmented Generation, combining retrieval and generation.",
    "RAG flow: chunk -> embed -> store -> retrieve -> generate.",
    "Vector DB options: Chroma, Qdrant, Milvus, Pinecone.",
    "Chunking strategies: fixed, recursive, semantic.",
]

def embed(text):
    r = client.embeddings.create(model="text-embedding-3-small", input=text)
    return r.data[0].embedding

def cosine_sim(a, b):
    dot = sum(x*y for x,y in zip(a,b))
    na = sum(x*x for x in a)**0.5
    nb = sum(y*y for y in b)**0.5
    return dot/(na*nb) if na and nb else 0

class VecStore:
    def __init__(self):
        self.vecs, self.txts = [], []
    def add(self, texts):
        for t in texts:
            self.vecs.append(embed(t)); self.txts.append(t)
        print(f"Added {len(texts)} docs")
    def search(self, q, k=3):
        qv = embed(q)
        scores = [cosine_sim(qv, v) for v in self.vecs]
        top = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:k]
        return [self.txts[i] for i in top]

def answer(query, contexts):
    ctx = "\n".join(contexts)
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": f"Based on:\n{ctx}"},
                  {"role": "user", "content": query}],
        temperature=0.3)
    return resp.choices[0].message.content

if __name__ == "__main__":
    store = VecStore(); store.add(DOCS)
    q = "What is RAG?"
    ctx = store.search(q)
    print(f"Context: {ctx}")
    print(f"Answer: {answer(q, ctx)}"
