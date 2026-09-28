 from lanchain_openai import OpenAI
 import dotenv import load_dotenv
 load_dotenv()
 llm = OpenAI(model_name="gpt-3.5-turbo", temperature=0, )
 response = llm.invoke("What is the capital of France?")
 print(response) 