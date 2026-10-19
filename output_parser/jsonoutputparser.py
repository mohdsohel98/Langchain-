from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
 from langchain_core.promps import PromptTemplate
 from langchain_core.output_parsers import StrOutputParser
load_dotenv()


llm = HuggingFaceEndpoint(
    endpoint_url="https://api-inference.huggingface.co/models/tiiuae

    task="text-generation",

)

model = ChatHuggingFace(llm = llm)
 parser = JsonOutputParser()

 template = PromptTemplate(
    input_variables=["topic"],
    template="You are a helpful assistant. Please answer the following question: {topic}",

    partial_variable = {'format_instruction' : parser.get_format_instructions() }

 )

  prompt = template.format()
  result  =  model.invoke(prompt)
  print(result) 