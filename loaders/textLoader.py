from langchain_community.document_loaders import TextLoader
from helper import ask_from_docs


loader = TextLoader(r"D:\AISchoolOfIndia\GENAI_AgenticAI course\RAG\loaders\today_news.txt", encoding= 'utf-8')
docs = loader.load()

# print(len(docs))
# print(docs[0].metadata)
# print(docs[0].page_content)

question = "what happened to hardik pandya? why is he not selected into indian squad?"

answer = ask_from_docs(docs, question)
print(answer)