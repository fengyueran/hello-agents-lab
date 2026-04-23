# 案例 3: 本地调用开源大语言模型

这个案例展示了如何在本地直接加载 Hugging Face 开源模型，并完成单轮对话、多轮对话和生成参数控制。

## 核心特性
- **本地推理**：直接使用 `transformers` 加载本地或 Hugging Face Hub 上的开源模型。
- **自动设备选择**：优先使用 `CUDA`，其次尝试 `MPS`，最后回退到 `CPU`。
- **多种示例场景**：
  - 单轮问答
  - 多轮上下文对话
  - 通过 `temperature` 和 `top_p` 调整生成风格

## 文件结构
- `client.py`: 本地模型客户端封装，负责模型加载与文本生成。
- `main.py`: 运行示例入口。

## 运行前准备
1. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
2. 可选配置 `.env`：
   ```bash
   LOCAL_MODEL_ID=Qwen/Qwen1.5-0.5B-Chat
   LOCAL_MAX_NEW_TOKENS=256
   ```

## 依赖体积说明
- `transformers` 本身不算大，但 `torch` 相对普通 Python 库会更大一些。
- 如果你使用的是 `pip install -r requirements.txt`，安装时间和下载体积会明显高于一般 Web 项目依赖。
- 对这个案例来说，真正更占空间的通常不是 `transformers`，而是首次下载的模型权重文件。

## 如何运行
```bash
python case-studies/open-source-llm-agent/main.py
```

## 说明
- 首次运行会自动下载模型文件和分词器配置，因此会比后续运行更慢。
- 下载完成后，文件会缓存到本地，后续再次运行通常不会重复下载。
- Hugging Face 的默认缓存目录通常是 `~/.cache/huggingface/hub`。
- 如果你希望修改缓存位置，可以配置 `HF_HOME` 或 `HF_HUB_CACHE` 环境变量。
- 如果本地已经提前下载好模型，也可以把 `LOCAL_MODEL_ID` 改为本地模型目录。
- 如果本机没有 GPU，也可以在 CPU 上运行，只是推理速度会较慢。
- 如果希望更换模型，只需要修改 `LOCAL_MODEL_ID` 即可。
