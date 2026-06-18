def prompt_builder(topchunks,ques):
    context = "\n\n".join(topchunks)
    prompt = f"""
You are a helpful assistant.

Answer only using the context below.
If the answer is not in the context, say "I don't know."

Context:
{context}

Question:
{ques}

Answer:
"""
    return prompt