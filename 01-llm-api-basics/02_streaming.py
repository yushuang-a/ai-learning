 """
 Streaming 流式输出示例
 """
 import os
 from openai import OpenAI
 
 client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
 
 
 def stream_chat(user_message):
     response = client.chat.completions.create(
         model="gpt-4o-mini",
         messages=[
             {"role": "system", "content": "你是一个知识丰富的助手。"},
             {"role": "user", "content": user_message},
         ],
         stream=True,
     )
     full_content = []
     for chunk in response:
         delta = chunk.choices[0].delta
         if delta.content:
             full_content.append(delta.content)
             print(delta.content, end="", flush=True)
     print()
     return "".join(full_content)
 
 
 if __name__ == "__main__":
     result = stream_chat("请用 100 字解释为什么需要流式输出？")
     print(f"\n完整内容长度：{len(result)} 字符")
