# 案例 2: 智能旅行助手 (ReAct 循环)

这个案例展示了如何构建一个具有“思考”和“行动”能力的智能体。

## 核心特性
- **ReAct 范式**：模型遵循 `Thought -> Action -> Observation` 的循环进行决策。
- **外部工具集成**：
  - `get_weather`: 获取实时天气。
  - `get_attraction`: 使用 Tavily 搜索景点。

## 技术原理：工具调用是如何实现的？

在这个案例中，你需要理解一个核心概念：**大模型本身并不具备执行 Python 代码或调用 API 的能力。**

1. **决策层 (LLM)**：大模型基于 `Thought` 进行推理，并输出一个“想要执行的操作”字符串（例如 `get_weather(city="北京")`）。
2. **执行层 (Python Agent)**：`main.py` 通过正则表达式解析模型产生的字符串，提取出函数名和参数，然后在本地执行真实的 Python 函数。
3. **反馈闭环**：函数执行的结果（Observation）被拼接回上下文，喂给大模型进行下一次推理。

这种“模型决策 -> 代码执行 -> 结果反馈”的闭环就是 **ReAct 范式** 的本质。

## 如何运行

1. **配置 API Key**：
   在根目录的 `.env` 文件中配置 `TAVILY_API_KEY`。
2. **运行代码**：
   ```bash
   python case-studies/travel-agent/main.py
   ```

## 文件结构
- `tools.py`: 定义工具函数。
- `client.py`: LLM 客户端封装。
- `main.py`: ReAct 循环主逻辑。
