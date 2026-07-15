 """
 Function Calling / Tool Use 示例
 """
 import os
 import json
 from openai import OpenAI
 
 client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
 
 TOOLS = [
     {
         "type": "function",
         "function": {
             "name": "get_weather",
             "description": "获取指定城市的天气信息",
             "parameters": {
                 "type": "object",
                 "properties": {
                     "city": {"type": "string", "description": "城市名称，如 北京、上海"}
                 },
                 "required": ["city"],
             },
         },
     },
     {
         "type": "function",
         "function": {
             "name": "get_stock_price",
             "description": "获取指定股票的当前价格",
             "parameters": {
                 "type": "object",
                 "properties": {
                     "symbol": {"type": "string", "description": "股票代码，如 600519"}
                 },
                 "required": ["symbol"],
             },
         },
     },
 ]
 
 
 def get_weather(city):
     data = {"北京": "25 C 晴", "上海": "28 C 多云", "重庆": "32 C 阴"}
     return data.get(city, "暂无数据")
 
 
 def get_stock_price(symbol):
     prices = {"600519": "1568.00", "000858": "138.50", "300750": "192.30"}
     return prices.get(symbol, "暂无数据")
 
 
 TOOL_FUNCTIONS = {"get_weather": get_weather, "get_stock_price": get_stock_price}
 
 
 def run_conversation(user_message):
     messages = [{"role": "system", "content": "你可以使用工具查询天气和股票信息。"},
                 {"role": "user", "content": user_message}]
 
     response = client.chat.completions.create(
         model="gpt-4o-mini",
         messages=messages,
         tools=TOOLS,
         tool_choice="auto",
     )
 
     msg = response.choices[0].message
     if not msg.tool_calls:
         return msg.content
 
     messages.append(msg)
     for tc in msg.tool_calls:
         func_name = tc.function.name
         args = json.loads(tc.function.arguments)
         result = TOOL_FUNCTIONS[func_name](**args)
         messages.append({"role": "tool", "tool_call_id": tc.id, "content": str(result)})
 
     final = client.chat.completions.create(model="gpt-4o-mini", messages=messages)
     return final.choices[0].message.content
 
 
 if __name__ == "__main__":
     result = run_conversation("北京天气如何？顺便查茅台股价。")
     print(result)
