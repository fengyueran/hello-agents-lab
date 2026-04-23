import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from context or specific path
load_dotenv()

def run_agent():
    """
    A simple Hello World Agent implementation.
    """
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
    )
    model = os.getenv("MODEL_NAME", "gpt-3.5-turbo")

    print(f"Agent is starting with model: {model}...")
    
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": "你是谁？"}]
        )
        print("Response from Agent:", response.choices[0].message.content)
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    run_agent()
