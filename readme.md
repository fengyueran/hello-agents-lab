# Hello Agents Lab

本项目是跟随 Datawhale [hello-agents](https://github.com/datawhalechina/hello-agents) 教程学习智能体（Agent）开发的实验案例库。

## 🎯 项目介绍

2025 年开启了 "Agent 元年"。本项目旨在通过系统性的学习，深入理解并构建真正的 AI Native Agent。我们将从智能体的核心原理出发，深入其核心架构，理解经典范式，并最终亲手构建属于自己的多智能体应用。

## ✨ 你将收获什么？

- **理解核心原理**：深入理解智能体的概念、历史与经典范式。
- **亲手实现**：掌握热门低代码平台和智能体代码框架的使用。
- **自研框架**：从零构建一个基于 OpenAI 原生 API 的智能体框架。
- **掌握高级技能**：逐步实现上下文工程、Memory、协议、评估等系统性技术。
- **实战驱动**：参与开发智能旅行助手、赛博小镇等综合项目。

## 🛠️ 环境准备

### 1. 克隆项目
```bash
git clone <your-repo-url>
cd hello-agents-lab
```

### 2. 创建虚拟环境 (建议使用 Conda)
```bash
conda create -n hello-agents python=3.10 -y
conda activate hello-agents
```

### 3. 配置环境变量
1. 如果你要运行某个具体案例，优先复制该案例目录下的 `.env.example`：
   - `case-studies/basic-llm-agent/.env.example`
   - `case-studies/travel-agent/.env.example`
   - `case-studies/open-source-llm-agent/.env.example`
2. 按案例分别放置 `.env` 文件，避免不同示例的变量互相混杂。
3. 说明：
   - 基础 LLM 客户端示例读取 `case-studies/basic-llm-agent/.env`。
   - `travel-agent` 示例读取 `case-studies/travel-agent/.env`。
   - `open-source-llm-agent` 示例读取 `case-studies/open-source-llm-agent/.env`。
4. 如果你想快速查看统一模板，也可以参考 `configs/.env.example`。
5. `open-source-llm-agent` 示例通常不依赖 API Key，可按需配置本地模型相关变量。

### 4. 安装依赖
```bash
pip install -r requirements.txt
```

## 📂 目录结构

- `case-studies/`: 学习案例及实战代码。
- `case-studies/basic-llm-agent/`: 基础 LLM 客户端示例，对应 4.1.1 到 4.1.3。
- `docs/`: 学习笔记与文档说明。
- `configs/`: 配置文件模板。

## 🤝 致谢

感谢 [Datawhale](https://github.com/datawhalechina) 提供的开源教程。
