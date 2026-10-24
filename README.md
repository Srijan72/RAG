# Retrieval-Augmented Generation (RAG) Using LangChain

## 📌 Project Overview

This project demonstrates how to build a Retrieval-Augmented Generation (RAG) pipeline using LangChain. It allows users to retrieve relevant information from documents and answer questions using a Large Language Model (LLM).

The project explores document loading, text chunking, embeddings, vector storage, similarity search, and question answering.

## 🚀 Features

* **Document Loading:** Load information from PDF files, text files, and websites.
* **Text Chunking:** Split documents into smaller chunks for efficient retrieval.
* **Text Embeddings:** Convert text into numerical vectors using embedding models.
* **Vector Database:** Store and retrieve document embeddings using ChromaDB.
* **Semantic Search:** Find relevant information based on the meaning of a query.
* **Question Answering:** Generate answers using retrieved context and an LLM.
* **Local Embeddings:** Experiment with Ollama embedding models.

## 🛠️ Technologies Used

* Python
* LangChain
* Groq LLM API
* Hugging Face Sentence Transformers
* ChromaDB
* Ollama
* PyPDF
* BeautifulSoup

## 📂 Project Structure

```text
RAG/
├── chunking/
│   └── PIPELINE/
│       ├── complete_pipeline.ipynb
│       └── data_retrieval.py
│
└── loaders/
    ├── helper.py
    ├── pdfLoader.py
    ├── textLoader.py
    ├── webLoader.py
    ├── requirements.txt
    ├── ML_Algorithms_Cheat_Sheet.pdf
    └── today_news.txt
```

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the Project Folder

```bash
cd RAG/loaders
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure the Groq API Key

Create a `.env` file inside the `loaders` folder and add:

```text
GROQ_API_KEY=your_groq_api_key
```

Replace the placeholder with your actual API key. Never upload your `.env` file to GitHub.

## ▶️ Running the Project

Run the following commands from the `loaders` folder.

### PDF Question Answering

```bash
python pdfLoader.py
```

### Text File Question Answering

```bash
python textLoader.py
```

### Website Question Answering

```bash
python webLoader.py
```

**Important:** Update the file paths in `pdfLoader.py` and `textLoader.py` to match the location of your files. The website loader requires an internet connection.

The PDF and text examples use the shared `helper.py` pipeline.

## 🔄 How RAG Works

1. **Load:** Read data from a PDF, text file, or website.
2. **Split:** Divide the loaded documents into smaller chunks.
3. **Embed:** Convert chunks into numerical vectors.
4. **Store:** Save the vectors in a vector database.
5. **Retrieve:** Find the most relevant chunks for a question.
6. **Generate:** Send the retrieved context and question to the LLM to generate an answer.

## 🎯 Learning Objectives

* Understand the fundamentals of Retrieval-Augmented Generation.
* Learn document loading and text splitting with LangChain.
* Understand embeddings and vector databases.
* Implement semantic search using ChromaDB.
* Build a basic document question-answering pipeline.
* Explore local embeddings and LLM integration.

## 🔮 Future Improvements

* Build an interactive Streamlit user interface.
* Support multiple PDF uploads.
* Add conversation history.
* Improve document retrieval and ranking.
* Add source citations to generated answers.
* Deploy the application as a web service.

## 👨‍💻 Author

**Srijan Akuthota**

GitHub: [Srijan72](https://github.com/Srijan72)

---

⭐ If you find this project useful, consider giving the repository a star!
