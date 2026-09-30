from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
 from langchain_core.promps import PromptTemplate
 from langchain_core.output_parsers import StrOutputParser
load_dotenv()


llm = HuggingFaceEndpoint(
    endpoint_url="https://api-inference.huggingface.co/models/tiiuae

    task="text-generation",

)


template1  = PromptTemplate(
  
    input_variables=["topic"],
    template="You are a helpful assistant. Please answer the following question: {topic}",
)

template2 = PromptTemplate(
    input_variables=["text"],
    template="You are a helpful assistant. Please answer the following question: {text}",
)



 parser = StrOutputParser()
 chain = template1 | model | parser | template2 |model | parser

  result =  chain.invoke({"topic": "black hole"})

  print(result);

