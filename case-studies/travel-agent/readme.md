# 案例 2: 智能旅行助手 (ReAct 循环)

这个案例展示了如何构建一个具有“思考”和“行动”能力的智能体。

## 核心特性
- **ReAct 范式**：模型遵循 `Thought -> Action -> Observation` 的循环进行决策。
- **外部工具集成**：
  - `get_weather`: 获取实时天气。
  - `get_attraction`: 使用 Tavily 搜索景点。

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
