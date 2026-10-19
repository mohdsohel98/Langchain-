from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema,runnbale import runnabaleParallel

load_dotenv()

model1 = ChatOpenAI()
model2 = ChatAnthropic()

prompt1 = PromptTemplate(
    template="Generate  short and simple notes from the following text: {text}",  
    input_variables=["text"]
)

prompt2 = PromptTemplate(
  template="Generate 5 pointers summary from following text: {text}",
  input_variables=["text"]
)

prompt3 = PromptTemplate(
  template="Merger the provided nots and quierse into a single document \n notes ->{notes} and quize ->{quiz} ",  
  input_variables=["notes", "quiz"] 
)

parser = StrOutputParser()

parallel_chain = runnabaleParallel(
    chains = [
        prompt1 | model1 | parser,
        prompt2 | model2 | parser
    ],
    input_variables=["text"],
    output_variables=["notes", "quiz"]
)

merger_chain = prompt3 | model1 | parser
chain = parallel_chain | merger_chain
result = chain.invoke({"text": "India is a country in South Asia. It is the seventh-largest country by land area and the second-most populous country in the world. India has a diverse culture, rich history, and a rapidly growing economy. The country is known for its contributions to art, science, and technology. India has a parliamentary system of government and is a federal republic. The official languages are Hindi and English, but there are many regional languages spoken throughout the country."})

print(result);
