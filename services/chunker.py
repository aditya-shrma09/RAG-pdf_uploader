def chunker(text):
    chunk_size = 100

    w = text.split()
    chunks =[]
    for i in range (0,len(w),chunk_size):
        chunk = w[i:i+chunk_size]
        chunks.append(" ".join(chunk))
    return chunks