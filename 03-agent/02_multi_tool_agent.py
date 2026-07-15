
import os, json
from openai import OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

TOOLS = [
    {"type": "function", "function": {"name": "search", "description": "Search news by keyword.",
        "parameters": {"type": "object", "properties": {"kw": {"type": "string"}}, "required": ["kw"]}}},
    {"type": "function", "function": {"name": "translate", "description": "Translate text.",
        "parameters": {"type": "object", "properties": {"text": {"type": "string"}, "lang": {"type": "string"}}, "required": ["text", "lang"]}}},
    {"type": "function", "function": {"name": "summarize", "description": "Summarize text.",
        "parameters": {"type": "object", "properties": {"text": {"type": "string"}, "max_len": {"type": "integer"}}, "required": ["text", "max_len"]}}},
]

def search(kw):
    db = {"AI": "2026: Major AI releases with agent and multimodal capabilities.",
          "Python": "Python 3.13 with JIT compilation released."}
    return db.get(kw, f"No news for: {kw}")

def translate(text, lang):
    resp = client.chat.completions.create(model="gpt-4o-mini",
        messages=[{"role": "system", "content": f"Translate to {lang}."}, {"role": "user", "content": text}])
    return resp.choices[0].message.content

def summarize(text, max_len=100):
    resp = client.chat.completions.create(model="gpt-4o-mini",
        messages=[{"role": "user", "content": f"Summarize within {max_len} words:
{text}"}])
    return resp.choices[0].message.content

FUNCS = {"search": search, "translate": translate, "summarize": summarize}

def run(msg):
    msgs = [{"role": "system", "content": "Multi-tool agent."}, {"role": "user", "content": msg}]
    for i in range(6):
        resp = client.chat.completions.create(model="gpt-4o-mini", messages=msgs, tools=TOOLS, tool_choice="auto")
        reply = resp.choices[0].message
        msgs.append(reply)
        if not reply.tool_calls:
            return reply.content
        for tc in reply.tool_calls:
            args = json.loads(tc.function.arguments) if tc.function.arguments else {}
            print(f"  [{i+1}] {tc.function.name}({args})")
            result = FUNCS[tc.function.name](**args)
            msgs.append({"role": "tool", "tool_call_id": tc.id, "content": str(result)})
    return "Max iterations."

if __name__ == "__main__":
    result = run("Search AI news, summarize, then translate to Chinese.")
    print(f"
{result}")
