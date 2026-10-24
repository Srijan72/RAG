from langchain_community.document_loaders import PyPDFLoader
from helper import ask_from_docs

loader = PyPDFLoader(r"D:\AISchoolOfIndia\GENAI_AgenticAI course\RAG\loaders\ML_Algorithms_Cheat_Sheet.pdf")
docs = loader.load()

# print(docs[0].metadata)
# print(docs[0].page_content[:2000])

question = "what is the advantage of L1 regularization"

answer = ask_from_docs(docs, question)
print(answer)
