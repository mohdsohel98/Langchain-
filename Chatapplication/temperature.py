import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

client = InferenceClient(
    api_key=os.getenv("HUGGINGFACE_ACCESS_TOKEN")
)

response = client.chat_completion(
    model="openai/gpt-oss-120b:fastest",
    messages=[
        {
            "role": "user",
            "content": "What is the capital of France?"
        }
    ]
)

print(response.choices[0].message.content)