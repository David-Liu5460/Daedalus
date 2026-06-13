import os

from dotenv import load_dotenv
from langchain_openai.chat_models import ChatOpenAI

load_dotenv()

ARK_BASE_URL = "https://ark.cn-beijing.volces.com/api/v3"
DOUBAO_SEED_MODEL = "doubao-seed-2-0-pro-260215"


def init_chat_model():
    api_key = os.getenv("ARK_API_KEY")
    if not api_key:
        raise ValueError("The `ARK_API_KEY` environment variable is not set")
    return ChatOpenAI(
        model=DOUBAO_SEED_MODEL,
        api_key=api_key,
        base_url=ARK_BASE_URL,
    )


if __name__ == "__main__":
    chat_model = init_chat_model()
    print(chat_model.invoke("What is the capital of France?"))
