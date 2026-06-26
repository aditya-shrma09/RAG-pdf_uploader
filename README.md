# PDF-RAG

A simple Retrieval-Augmented Generation (RAG) application built with **Streamlit**, **Sentence Transformers**, and **Google Gemini**. The application allows users to upload a PDF and ask questions about its contents. Answers are generated using relevant information retrieved from the uploaded document.

## Features

* Upload PDF documents
* Extract text from PDFs
* Split documents into chunks
* Generate embeddings using Sentence Transformers
* Retrieve relevant chunks using cosine similarity
* Build prompts from retrieved context
* Generate answers with Google Gemini
* Interactive Streamlit interface

## Project Structure

```
RAG-pdf_uploader/
│
├── app.py
├── .env
├── services/
│   ├── pdf_uploader.py
│   ├── chunker.py
│   ├── embedding.py
│   ├── retriver.py
│   ├── prompt_builder.py
│   └── llm.py
│
├── data/
│   └── uploads/
│
└── requirements.txt
```

## Installation

Clone the repository:

```bash
git clone https://github.com/aditya-shrma09/RAG-pdf_uploader.git
cd RAG-pdf_uploader
```
Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root:

```text
GEMINI_API_KEY=your_api_key_here
```

## Running the Application

Start the Streamlit app:

```bash
streamlit run app.py
```

## How It Works

1. Upload a PDF.
2. Extract text from the document.
3. Split text into chunks.
4. Generate embeddings for each chunk.
5. Store chunk embeddings in a vector store.
6. Embed the user's question.
7. Retrieve the most relevant chunks.
8. Build a prompt using the retrieved context.
9. Send the prompt to Google Gemini.
10. Display the generated answer.

## Technologies Used

* Python
* Streamlit
* Sentence Transformers
* scikit-learn
* NumPy
* PyPDF2
* Google Gemini API

## Future Improvements

* FAISS vector database
* Conversation memory
* Source citations
* Multi-PDF support
* Chat interface
* Persistent vector storage

## Example

**Question:**

> What is the European economy?

**Answer:**

> The European economy has traditionally been strong in all mid-technology sectors that are not at the center of radical technological advances. It has less activity in sectors where much of the productivity growth has originated in recent years, notably the ICT sector and the exploitation of large-scale digital services. The EU outperforms the US in mid-technology sectors like manufacturing of transport equipment, agriculture, and in the wholesale and retail sectors. At its root, Europe's weak position in digital tech is due to a static industrial structure which produces a vicious circle of low investment and low innovation. Growth in the EU has been slowing, driven by weakening productivity growth, and its economic growth has been persistently slower than in the US over the past two decades.
