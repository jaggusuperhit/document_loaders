import os
from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

def main():
    try:
        openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
        if not openrouter_api_key:
            raise ValueError("OPENROUTER_API_KEY not found in environment variables")

        # Initialize model
        model = ChatOpenAI(
            model="openai/gpt-3.5-turbo",
            openai_api_base="https://openrouter.ai/api/v1",
            openai_api_key=openrouter_api_key,
            temperature=0.3
        )
        
        prompt = PromptTemplate(
            template="Write a concise summary of the following poem - \n{poem}",
            input_variables=["poem"]
        )

        # Load the text file
        try:
            loader = TextLoader("cricket.txt", encoding="utf-8")
            docs = loader.load()
            
            # Debugging info
            print("Document type:", type(docs))
            print("Number of documents:", len(docs))
            print("First document type:", type(docs[0]))
            print("Metadata:", docs[0].metadata)
            
            poem_content = docs[0].page_content
            print("\nOriginal Poem:\n", poem_content)
            
        except Exception as e:
            raise Exception(f"Error loading document: {str(e)}")

        # Create and run the chain
        chain = prompt | model | StrOutputParser()
        summary = chain.invoke({"poem": poem_content})
        
        print("\nSummary:\n", summary)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()