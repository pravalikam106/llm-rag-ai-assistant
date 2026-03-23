import numpy as np
import faiss

documents = []
index = None

def load_documents():
    global documents
    with open("data/sample_docs.txt", "r") as f:
        documents = f.readlines()

def create_embeddings():
    global index
    vectors = np.random.rand(len(documents), 128).astype("float32")
    index = faiss.IndexFlatL2(128)
    index.add(vectors)

def search(query):
    query_vector = np.random.rand(1, 128).astype("float32")
    _, I = index.search(query_vector, k=2)
    return [documents[i] for i in I[0]]
