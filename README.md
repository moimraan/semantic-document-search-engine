# Semantic Document Search Engine

A scalable semantic search system that enables intelligent document retrieval using transformer embeddings and vector similarity search.

The system converts documents into embeddings and performs semantic matching to return the most relevant results for user queries.

---

## System Architecture

Document Processing  
→ Text Embedding Generation  
→ Vector Indexing  
→ Query Embedding  
→ Similarity Search  

---

## Key Features

Transformer based text embeddings  
Vector similarity search using FAISS  
Document preprocessing pipeline  
Fast semantic query retrieval  
REST API for search queries  
Interactive search interface with Streamlit  

---

## Tech Stack

Python  
Sentence Transformers  
FAISS  
FastAPI  
Streamlit  

---
## Project Structure


semantic-document-search-engine
│
├── preprocessing
│ ├── document_cleaning.py
│
├── embeddings
│ ├── embedding_model.py
│
├── indexing
│ ├── faiss_index_builder.py
│
├── search
│ ├── semantic_search.py
│
├── api
│ ├── search_api.py
│
├── ui
│ ├── streamlit_app.py
│
└── README.md

## Project Structure
