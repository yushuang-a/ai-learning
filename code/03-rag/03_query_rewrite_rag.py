
import os
from openai import OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

KB = [
    "Vector DBs store vectors for semantic search.",
    "Common VDBs: Chroma, Qdrant, Milvus.",
    "Cosine similarity measures vector similarity.",
    "HNSW is a popular ANN algorithm.",
    "Hybrid Search combines vector + keyword search.",
    "Reranking refines initial search results.",
]

def embed(text):
    r = client.embeddings.create(model="text-embedding-3-small", input=text)
    return r.data[0].embedding

def search(query, k=3):
    qv = embed(query)
    scores = []
    for doc in KB:
        dv = embed(doc)
        dot = sum(a*b for a,b in zip(qv,dv))
        nq = sum(a*a for a in qv)**0.5
        nd = sum(b*b for b in dv)**0.5
        scores.append(dot/(nq*nd) if nq and nd else 0)
    top = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:k]
    return [KB[i] for i in top]

def rewrite_query(q):
    prompt = f"Rewrite this into 2 search queries: {q}"
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}])
    return [s.strip() for s in resp.choices[0].message.content.strip().split("
") if s.strip()]

def gen_answer(q, ctx):
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": f"Context:\n{chr(10).join(ctx)}\n\nQ: {q}\nA:"}],
        temperature=0.3)
    return resp.choices[0].message.content

if __name__ == "__main__":
    q = "How does Hybrid Search work?"
    print(f"Q: {q}")
    rewritten = rewrite_query(q)
    print(f"Rewritten: {rewritten}")
    all_ctx = []
    for rq in rewritten[:2]:
        all_ctx.extend(search(rq, k=2))
    seen = set()
    uniq = []
    for c in all_ctx:
        if c not in seen:
            seen.add(c); uniq.append(c)
    print(f"Context: {uniq[:3]}")
    print(f"Answer: {gen_answer(q, uniq[:3])}")
