from langchain_community.document_loaders import CSVLoader
loader = CSVLoader(file_path='Social_Network_Ads.csv')

docs = loader.load()
print(len(docs[0]))
print(docs[0])

