

def create_vector_store(chunks, vectors):

    vector_store = []

    for chunk, vector in zip(chunks, vectors):

        vector_store.append({
            "text": chunk,
            "embedding": vector
        })

    return vector_store

