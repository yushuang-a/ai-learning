 """
 LLM API 基础调用示例
 """
 import os
 from openai import OpenAI
 
 client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
 
 
 def simple_chat(user_message, system_prompt="你是一个有帮助的助手。"):
     response = client.chat.completions.create(
         model="gpt-4o-mini",
         messages=[
             {"role": "system", "content": system_prompt},
             {"role": "user", "content": user_message},
         ],
         temperature=0.7,
         max_tokens=1024,
     )
     return response.choices[0].message.content
 
 
 if __name__ == "__main__":
     result = simple_chat("请用一句话解释什么是 RAG？")
     print(f"回答：{result}")
