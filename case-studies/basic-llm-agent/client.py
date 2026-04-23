import os
from pathlib import Path
from typing import Any, Dict, List, Optional

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(dotenv_path=Path(__file__).with_name(".env"))


class HelloAgentsLLM:
    """
    为《Hello Agents》定制的基础 LLM 客户端。

    该客户端用于调用兼容 OpenAI 接口的服务，并默认以流式方式输出模型结果。
    配置优先级为：构造参数 > 环境变量 > 默认值校验失败。
    """

    def __init__(
        self,
        model: Optional[str] = None,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        timeout: Optional[int] = None,
    ) -> None:
        """
        初始化 LLM 客户端。

        Args:
            model: 模型 ID。未提供时从 `LLM_MODEL_ID` 读取。
            api_key: API 密钥。未提供时从 `LLM_API_KEY` 读取。
            base_url: 服务地址。未提供时从 `LLM_BASE_URL` 读取。
            timeout: 请求超时时间，单位秒。未提供时从 `LLM_TIMEOUT` 读取，默认 60。

        Raises:
            ValueError: 当模型 ID、API 密钥或服务地址缺失时抛出。
        """
        self.model = model or os.getenv("LLM_MODEL_ID")
        resolved_api_key = api_key or os.getenv("LLM_API_KEY")
        resolved_base_url = base_url or os.getenv("LLM_BASE_URL")
        resolved_timeout = timeout or int(os.getenv("LLM_TIMEOUT", "60"))

        if not all([self.model, resolved_api_key, resolved_base_url]):
            raise ValueError("模型ID、API密钥和服务地址必须通过参数或 .env 文件提供。")

        self.client = OpenAI(
            api_key=resolved_api_key,
            base_url=resolved_base_url,
            timeout=resolved_timeout,
        )

    def think(
        self,
        messages: List[Dict[str, str]],
        temperature: float = 0,
    ) -> Optional[str]:
        """
        调用大语言模型并返回完整响应文本。

        Args:
            messages: OpenAI Chat Completions 消息列表。
            temperature: 采样温度，默认 0，便于输出稳定结果。

        Returns:
            模型返回的完整文本；当调用失败时返回 `None`。
        """
        print(f"正在调用 {self.model} 模型...")
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=temperature,
                stream=True,
            )

            print("大语言模型响应成功：")
            collected_content: List[str] = []
            for chunk in response:
                content = chunk.choices[0].delta.content or ""
                if content:
                    print(content, end="", flush=True)
                    collected_content.append(content)
            print()
            return "".join(collected_content)
        except Exception as exc:
            print(f"调用 LLM API 时发生错误: {exc}")
            return None
