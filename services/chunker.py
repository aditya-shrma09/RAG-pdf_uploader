def chunker(text):
    chunk_size = 500
    overlap = 50
    start =0
    w = text.split()
    chunks =[]
    while start < len(text):

        end = start + chunk_size
        chunk = " ".join(w[start:end])
        chunks.append(chunk)

        start += chunk_size - overlap
    # for i in range (0,len(w),chunk_size):
    #     chunk = w[i:i+chunk_size]
    #     chunks.append(" ".join(chunk))
    return chunks