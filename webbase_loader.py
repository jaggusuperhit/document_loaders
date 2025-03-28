from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTempalte
from dotenv  import load_dotenv

load_dotenv()

model = ChatOpenAI()

prompt = PromptTempalte(
    template='Answer the following question \n{question} from the following text - \n {text}',
    input_variables = ['question','text']
)

parser = StrOutputParser()

url = 'https://www.flipkart.com/q/macbook-air-13-inch'
loader = WebBaseLoader(url)

docs = loader.load()

chain = prompt | model | parser
print(chain.invoke({'question':'what is the product that we are talking about?', 'text':docs[0].page_content}))

# print(len(docs))
# print(docs[0].page_content)

