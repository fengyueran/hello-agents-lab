from client import HelloAgentsLLM


def run_demo() -> None:
    """
    运行基础 LLM 调用示例。
    """
    llm_client = HelloAgentsLLM()

    example_messages = [
        {
            "role": "system",
            "content": "你是一个擅长解释 Python 代码的助手，请给出清晰、可运行的示例。",
        },
        {
            "role": "user",
            "content": "请用 Python 写一个快速排序，并简单解释一下它的时间复杂度。",
        },
    ]

    print("--- 调用 LLM ---")
    response_text = llm_client.think(example_messages)

    if response_text:
        print("\n--- 完整模型响应 ---")
        print(response_text)


if __name__ == "__main__":
    try:
        run_demo()
    except ValueError as exc:
        print(exc)
