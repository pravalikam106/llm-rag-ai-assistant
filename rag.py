from embeddings import search

def generate_response(query):
    context = search(query)
    context_text = " ".join(context)

    response = f"Based on context: {context_text} Answer: {query}"

    return response, context_text
