import os
import requests
from tavily import TavilyClient

def get_weather(city: str) -> str:
    """
    通过调用 wttr.in API 查询真实的天气信息。
    """
    url = f"https://wttr.in/{city}?format=j1"
    try:
        response = requests.get(url)
        response.raise_for_status() 
        data = response.json()
        
        current_condition = data['current_condition'][0]
        weather_desc = current_condition['weatherDesc'][0]['value']
        temp_c = current_condition['temp_C']
        
        return f"{city}当前天气:{weather_desc}，气温{temp_c}摄氏度"
    except Exception as e:
        return f"错误:查询天气时出现问题 - {e}"

def get_attraction(city: str, weather: str) -> str:
    """
    根据城市和天气，使用 Tavily Search API 搜索并返回旅游景点推荐。
    """
    api_key = os.getenv("TAVILY_API_KEY")
    if not api_key or api_key == "YOUR_TAVILY_API_KEY":
        return "错误:未配置或未填写有效的 TAVILY_API_KEY 环境变量。"

    tavily = TavilyClient(api_key=api_key)
    query = f"'{city}' 在'{weather}'天气下最值得去的旅游景点推荐及理由"
    
    try:
        response = tavily.search(query=query, search_depth="basic", include_answer=True)
        if response.get("answer"):
            return response["answer"]
        
        formatted_results = [f"- {r['title']}: {r['content']}" for r in response.get("results", [])]
        return "\n".join(formatted_results) if formatted_results else "抱歉，没有找到相关的旅游景点推荐。"
    except Exception as e:
        return f"错误:执行 Tavily 搜索时出现问题 - {e}"

# 导出工具字典
available_tools = {
    "get_weather": get_weather,
    "get_attraction": get_attraction,
}
