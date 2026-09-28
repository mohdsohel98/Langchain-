from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()

client = InferenceClient(
    token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

st.header("Chat Application with Hugging Face API")

user_input = st.text_input("Enter your prompt:")

if st.button("Submit"):
    if user_input:
        result = client.chat_completion(
            model="openai/gpt-oss-120b:fastest",
            messages=[
                {"role": "user", "content": user_input}
            ]
        )

        st.write(result.choices[0].message.content)