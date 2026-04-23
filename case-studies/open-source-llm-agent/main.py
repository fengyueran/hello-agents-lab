import os

from dotenv import load_dotenv

from client import DEFAULT_MODEL_ID, LocalTransformersClient

load_dotenv()


def run_single_turn_example(llm: LocalTransformersClient, max_new_tokens: int) -> None:
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "你好，请介绍一下你自己。"},
    ]

    response = llm.generate(messages, max_new_tokens=max_new_tokens)

    print("=== 单轮对话示例 ===")
    print(f"用户: {messages[1]['content']}")
    print(f"模型: {response}\n")


def run_multi_turn_example(llm: LocalTransformersClient, max_new_tokens: int) -> None:
    conversation = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "我想在本地运行开源大语言模型，应该先做什么？"},
    ]

    first_reply = llm.generate(conversation, max_new_tokens=max_new_tokens)
    conversation.append({"role": "assistant", "content": first_reply})
    conversation.append(
        {"role": "user", "content": "如果我的电脑没有独立显卡，还有什么适合初学者的建议？"}
    )
    second_reply = llm.generate(conversation, max_new_tokens=max_new_tokens)

    print("=== 多轮对话示例 ===")
    print(f"用户: {conversation[1]['content']}")
    print(f"模型: {first_reply}")
    print(f"用户: {conversation[3]['content']}")
    print(f"模型: {second_reply}\n")


def run_creative_example(llm: LocalTransformersClient, max_new_tokens: int) -> None:
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "请用三句话介绍为什么本地部署大语言模型适合学习。"},
    ]

    response = llm.generate(
        messages,
        max_new_tokens=max_new_tokens,
        temperature=0.9,
        top_p=0.95,
    )

    print("=== 采样参数示例 ===")
    print(f"用户: {messages[1]['content']}")
    print(f"模型: {response}\n")


def run_agent() -> None:
    model_id = os.getenv("LOCAL_MODEL_ID", DEFAULT_MODEL_ID)
    max_new_tokens = int(os.getenv("LOCAL_MAX_NEW_TOKENS", "256"))
    llm = LocalTransformersClient(model_id=model_id)

    print(f"正在加载本地模型: {model_id}")
    print(f"当前推理设备: {llm.device}\n")

    try:
        run_single_turn_example(llm, max_new_tokens)
        run_multi_turn_example(llm, max_new_tokens)
        run_creative_example(llm, max_new_tokens)
    except Exception as exc:
        print(f"运行本地模型示例时发生错误: {exc}")


if __name__ == "__main__":
    run_agent()
