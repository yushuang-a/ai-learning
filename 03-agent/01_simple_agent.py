
import os, json
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

TOOLS = [
    {"type": "function", "function": {"name": "calculator", "description": "Calculate math expression.",
        "parameters": {"type": "object", "properties": {"expr": {"type": "string"}}, "required": ["expr"]}}},
    {"type": "function", "function": {"name": "get_time", "description": "Get current time.",
        "parameters": {"type": "object", "properties": {}}}},
]

def calculator(expr):
    try: return str(eval(expr, {"__builtins__": {}}, {}))
    except: return f"Error: {expr}"

def get_time():
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

FUNCS = {"calculator": calculator, "get_time": get_time}

def run_agent(msg, max_steps=5):
    messages = [{"role": "system", "content": "You are a helpful agent with tools."},
                {"role": "user", "content": msg}]
    for step in range(max_steps):
        resp = client.chat.completions.create(model="gpt-4o-mini", messages=messages, tools=TOOLS, tool_choice="auto")
        reply = resp.choices[0].message
        print(f"[Step {step+1}] Thought: {reply.content or '(using tools...)'}")
        if not reply.tool_calls:
            return reply.content
        messages.append(reply)
        for tc in reply.tool_calls:
            args = json.loads(tc.function.arguments) if tc.function.arguments else {}
            result = FUNCS[tc.function.name](**args)
            print(f"  Tool {tc.function.name}({args}) -> {result}")
            messages.append({"role": "tool", "tool_call_id": tc.id, "content": str(result)})
    return "Max steps reached."

if __name__ == "__main__":
    result = run_agent("Calculate 12345 * 67890 and tell me the time.")
    print(f"
Final: {result}")
