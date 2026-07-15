
import os, json
from datetime import datetime
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

TEST_CASES = [
    {"q": "What is RAG?", "golden": "RAG retrieves relevant docs and uses LLM to answer based on them.", "relevant": [0]},
    {"q": "Name vector databases.", "golden": "Chroma, Qdrant, Milvus, Pinecone.", "relevant": [2]},
]

KB = [
    "RAG combines retrieval and generation for knowledge-grounded answers.",
    "RAG flow: chunk -> embed -> store -> search -> generate.",
    "Vector DBs: Chroma (dev), Qdrant (production), Milvus (large-scale).",
    "Embedding models convert text to vectors for semantic search.",
]

def embed(text):
    r = client.embeddings.create(model="text-embedding-3-small", input=text)
    return r.data[0].embedding

def retrieve(q, k=3):
    qv = embed(q)
    scores = []
    for d in KB:
        dv = embed(d)
        dot = sum(a*b for a,b in zip(qv,dv))
        nq = sum(a*a for a in qv)**0.5
        nd = sum(b*b for b in dv)**0.5
        scores.append(dot/(nq*nd) if nq and nd else 0)
    return sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:k]

def generate(q, ctx):
    resp = client.chat.completions.create(model="gpt-4o-mini",
        messages=[{"role": "user", "content": f"Based on:
{chr(10).join(ctx)}

Q: {q}
A:"}],
        temperature=0.3)
    return resp.choices[0].message.content

def eval_retrieval(retrieved, relevant):
    tp = len(set(retrieved) & set(relevant))
    p = tp/len(retrieved) if retrieved else 0
    r = tp/len(relevant) if relevant else 0
    f1 = 2*p*r/(p+r) if p+r > 0 else 0
    return {"precision": round(p,3), "recall": round(r,3), "f1": round(f1,3)}

def eval_generation(q, answer, golden):
    resp = client.chat.completions.create(model="gpt-4o-mini",
        messages=[{"role": "user",
                   "content": f'Score 1-5 for accuracy, completeness, relevance. JSON only.
Q: {q}
Golden: {golden}
Answer: {answer}'}],
        response_format={"type": "json_object"})
    return json.loads(resp.choices[0].message.content)

if __name__ == "__main__":
    print(f"RAG Evaluation - {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"Test cases: {len(TEST_CASES)}
")
    avg_ret = {"precision": [], "recall": [], "f1": []}
    avg_gen = {"accuracy": [], "completeness": [], "relevance": []}

    for i, tc in enumerate(TEST_CASES):
        print(f"--- Case {i+1}: {tc['q'][:30]} ---")
        idx = retrieve(tc["q"])
        es = eval_retrieval(idx, tc["relevant"])
        print(f"  Retrieval: {es}")
        for k in avg_ret: avg_ret[k].append(es[k])

        ctx = [KB[j] for j in idx]
        ans = generate(tc["q"], ctx)
        qs = eval_generation(tc["q"], ans, tc["golden"])
        print(f"  Quality: acc={qs.get('accuracy','?')} comp={qs.get('completeness','?')} rel={qs.get('relevance','?')}")
        for k in avg_gen: avg_gen[k].append(qs.get(k, 0))

    print(f"
--- Summary ---")
    print(f"Avg retrieval: {sum(avg_ret['precision'])/len(avg_ret['precision']):.3f} precision, "
          f"{sum(avg_ret['recall'])/len(avg_ret['recall']):.3f} recall")
    print(f"Avg quality: {sum(avg_gen['accuracy'])/len(avg_gen['accuracy']):.1f} accuracy, "
          f"{sum(avg_gen['completeness'])/len(avg_gen['completeness']):.1f} completeness")
