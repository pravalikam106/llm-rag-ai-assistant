from fastapi import FastAPI
from rag import generate_response
from evaluator import evaluate_response
from embeddings import load_documents, create_embeddings

app = FastAPI()

load_documents()
create_embeddings()

@app.get("/ask")
def ask_question(query: str):
    response, context = generate_response(query)
    evaluation = evaluate_response(query, response)

    return {
        "query": query,
        "response": response,
        "context": context,
        "evaluation": evaluation
    }
