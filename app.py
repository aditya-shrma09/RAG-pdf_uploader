import streamlit as st
import os

from services.pdf_uploader import extract_text
from services.chunker import chunker
from services.embedding import embedder
UPLOAD_DIR = "data/uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:

    file_path = os.path.join(
        UPLOAD_DIR,
        uploaded_file.name
    )

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    text = extract_text(file_path)
    chunks = chunker(text)
    vectors = embedder(chunks)
   

    st.write(vectors.shape)
    st.write(vectors[0][:10])
    for i, chunk in enumerate(chunks [:5]):

     st.subheader(f"Chunk {i + 1}")

     st.text_area(
         f"Chunk {i + 1}",
        chunk,
        height=200
    )
     
    