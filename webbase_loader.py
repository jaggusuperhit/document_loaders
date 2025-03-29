import os
import requests
from dotenv import load_dotenv
from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

# Load environment variables
load_dotenv()
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")

# Debugging: Check API Key
if not openrouter_api_key:
    raise ValueError("ERROR: OPENROUTER_API_KEY is missing! Check your .env file.")

# Test API Key
response = requests.get(
    "https://openrouter.ai/api/v1/models",
    headers={"Authorization": f"Bearer {openrouter_api_key}"}
)
if response.status_code == 401:
    raise ValueError("ERROR: Invalid OpenRouter API Key. Check your credentials.")

# Set up the model
model = ChatOpenAI(
    model="openai/gpt-3.5-turbo",
    openai_api_base="https://openrouter.ai/api/v1",
    openai_api_key=openrouter_api_key,
    temperature=0.3
)


# Define prompt template
prompt = PromptTemplate(
    template="""Extract information from the following text to answer the question.
    
    Question: {question}
    
    Text: {text}
    
    Answer concisely:""",
    input_variables=['question', 'text']
)

parser = StrOutputParser()

# Set user-agent to avoid blocking
os.environ["USER_AGENT"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

# Flipkart page (note: may still block scraping)
url = 'https://www.flipkart.com/q/macbook-air-13-inch'
loader = WebBaseLoader(url)

try:
    docs = loader.load()
    
    # Debugging: Print content length
    print(f"Loaded content length: {len(docs[0].page_content)} characters")
    
    # Run the query
    chain = prompt | model | parser
    response = chain.invoke({
        'question': 'What products are listed on this page?',
        'text': docs[0].page_content[:10000]  # Limit input to 10k chars
    })
    
    print("Response:", response)

except Exception as e:
    print(f"Error: {str(e)}")
    print("Note: Flipkart may block web scraping attempts. Consider using Selenium or ScraperAPI.")
