from langchain_community.document_loaders import WebBaseLoader
from helper import ask_from_docs

loader = WebBaseLoader("https://docs.langchain.com/oss/python/integrations/document_loaders")
docs = loader.load()

# print(docs[0].metadata)
# print(docs[0].page_content[:2000])

question = "Total how many types of document loaders are there?"

answer = ask_from_docs(docs, question)
print(answer)