from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
def create_vector_store(chunks, vectors):

    vector_store = []

    for chunk, vector in zip(chunks, vectors):

        vector_store.append({
            "text": chunk,
            "embedding": vector
        })

    return vector_store

def retrieve(equery, vector_store, k=3):
     chunk_embeddings = [
        item["embedding"]
        for item in vector_store
    ]
     scores = cosine_similarity(
        [equery],
        chunk_embeddings
    )[0]
     top_indices = np.argsort(scores)[::-1][:k]
     return [
        vector_store[i]["text"]
        for i in top_indices
    ]


