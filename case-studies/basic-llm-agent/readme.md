# 案例 1: 基础 LLM 客户端

这个案例对应书中 4.1.1 到 4.1.3 的内容，用来演示如何安装依赖、配置环境变量，并封装一个可复用的基础 LLM 客户端。

## 核心特性
- **统一环境变量配置**：通过 `.env` 管理 `LLM_API_KEY`、`LLM_MODEL_ID`、`LLM_BASE_URL`。
- **客户端封装**：使用 `HelloAgentsLLM` 统一处理模型调用细节。
- **流式输出**：默认以流式方式打印模型返回内容，便于观察生成过程。

## 运行前准备
1. 安装依赖：
   ```bash
   pip install openai python-dotenv
   ```
2. 复制本案例模板并填写配置：
   ```bash
   cp case-studies/basic-llm-agent/.env.example case-studies/basic-llm-agent/.env
   ```
3. 编辑本案例目录下的 `.env` 文件：
   ```env
   LLM_API_KEY="YOUR-API-KEY"
   LLM_MODEL_ID="YOUR-MODEL"
   LLM_BASE_URL="YOUR-URL"
   ```

## 如何运行
```bash
python case-studies/basic-llm-agent/main.py
```

## 文件结构
- `client.py`: 基础 LLM 客户端封装。
- `main.py`: 调用示例入口。

## 说明
- 如果你的服务需要超时时间，可以额外配置 `LLM_TIMEOUT`，单位为秒。
- 这个案例只演示最基础的模型调用闭环，适合作为后续 `travel-agent` 等智能体案例的起点。
