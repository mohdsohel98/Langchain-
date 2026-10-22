from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain-schema.runnable import RunnableSequence

load_dotenv()


prompt1 = PromptTemplate(
    template="  generate 5 jokes  {topic}",
    input_variables=["topic"]
)

model = ChatOpenAI()

parser = StrOutputParser()

prompt2 = PromptTemplate(
    template="explain the following jokes   {topic}",
    input_variables=["topic"]
)

chain  = RunnableSequence(prompt1, model, parser, prompt2, model, parser)

print(chain.invoke({"topic": "AI"}))
