# LLM-Based AI Assistant with RAG and Evaluation Pipeline

This project demonstrates a simple AI assistant using retrieval-based logic.

## Features
- Retrieval-Augmented Generation (RAG)
- Embedding-based search using FAISS
- FastAPI endpoint for queries
- Basic response evaluation

## Tech Stack
- Python
- FastAPI
- FAISS
- NumPy

## Run the project
pip install -r requirements.txt  
uvicorn app:app --reload  

## API Example
GET /ask?query=What is FastAPI?
