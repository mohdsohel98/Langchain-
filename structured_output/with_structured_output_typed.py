 from langchain_openai import ChatOpenAI
  from dotenv import load_dotenv
   from typing import typeDict

   load_dotenv()

   model = ChatOpenAI()

   class Review (TypeDict):
    summary :: str
    sentiment : str
    structured_model  = model.with_structured_output(Review)

    result = structured_model.predict("The product was great, but the delivery was late.")
    print(result)