def evaluate_response(query, response):
    score = 0

    if query.lower() in response.lower():
        score += 1

    if len(response) > 20:
        score += 1

    return {
        "relevance_score": score,
        "length": len(response)
    }
