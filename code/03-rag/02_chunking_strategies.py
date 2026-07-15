"""
Document chunking strategies comparison
"""
import re

SAMPLE = """
RAG Chapter 1: Overview
RAG combines retrieval and generation to solve knowledge freshness and hallucination.

Chapter 2: Core Flow
Document -> Chunking -> Embedding -> Vector Store -> Retrieval -> Generation

Chapter 3: Chunking Strategies
3.1 Fixed-length: Simple, may break semantics.
3.2 Recursive: Preserves meaning better.
3.3 Semantic: Best quality, highest cost.
"""

def fixed_chunk(text, size=80, overlap=20):
    chunks = []
    start = 0
    while start < len(text):
        end = start + size
        chunks.append(text[start:end].strip())
        start = end - overlap
    return [c for c in chunks if c]

def paragraph_chunk(text):
    return [p.strip() for p in text.split("

") if p.strip()]

def section_chunk(text):
    pattern = r"(?:#{2,3}\s+.*|Chapter \d+.*|\d+\.\d+\s+.*)"
    sections = re.split(pattern, text)
    titles = re.findall(pattern, text)
    result = []
    for i, s in enumerate(sections):
        s = s.strip()
        if s:
            t = titles[i-1] if i > 0 and i-1 < len(titles) else ""
            result.append(f"{t}
{s}" if t else s)
    return result

if __name__ == "__main__":
    print(f"Fixed: {len(fixed_chunk(SAMPLE))} chunks")
    print(f"Paragraph: {len(paragraph_chunk(SAMPLE))} chunks")
    print(f"Section: {len(section_chunk(SAMPLE))} chunks")
