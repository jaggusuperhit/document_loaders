from langchain_community.document_loaders import PyPDFLOader
loader = PyPDFLOader('dl-curricculum.pdf')
docs = loader.load()
print(len(docs))
print(docs[0].page_content)
print(docs[1].metadata)
