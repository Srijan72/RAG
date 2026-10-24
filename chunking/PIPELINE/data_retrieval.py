from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

vector = embeddings.embed_query(
    "What is RAG?"
)

print(type(vector))
print(len(vector))
print(vector[:10])


# chunks = [
#     "RAG helps LLMs access external knowledge.",
#     "Embeddings convert text into vectors.",
#     "Vector databases store embeddings."
# ]

# vectors = embeddings.embed_documents(
#     chunks
# )

# print(len(vectors))

# print(len(vectors[0]))