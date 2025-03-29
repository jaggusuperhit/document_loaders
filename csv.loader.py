from langchain_community.document_loaders import CSVLoader

# Load the CSV file
loader = CSVLoader(file_path='Social_Network_Ads.csv')
docs = loader.load()

# Print basic info
print(f"Total rows loaded: {len(docs)}")  # Number of rows
print(f"Columns in first row: {len(docs[0].page_content.split(','))}")  # Estimated columns

# Print first row content
print("\nFirst row content:")
print(docs[0].page_content)

# Print metadata (if any)
print("\nMetadata:")
print(docs[0].metadata)