def prompt_builder(topchunks,ques):
    context = "\n\n".join(topchunks)
    prompt = f"""
Answer the question using only the context below.

Context:
{context}

Question:
{ques}

Answer:
"""
    return prompt