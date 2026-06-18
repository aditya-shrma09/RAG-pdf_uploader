import streamlit as st
import os

from services.pdf_uploader import extract_text
from services.chunker import chunker
from services.embedding import embedder
from services.retriver import create_vector_store
from services.retriver import retrieve
from services.prompt_builder import prompt_builder
from services.llm import generate_answer
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
    vector_store = create_vector_store(chunks, vectors)

    ques = st.text_input("Ask a question")

    if ques:

        em_ques = embedder(ques)

        top_k_chunks = retrieve(
            em_ques,
            vector_store
        )

        # st.write(top_k_chunks)

        prompt = prompt_builder(
            top_k_chunks,
            ques
        )
        st.write("Generating answer...")
        answer =  generate_answer(prompt)   
        st.write(answer) 
   # st.write(vectors.shape)
    # st.write(vectors[0][:10])
    # st.write("Number of entries:", len(vector_store))
    # st.write(vector_store[0]["text"])
    # st.write(len(vector_store[0]["embedding"]))
    # for i, chunk in enumerate(chunks [:5]):

    #  st.subheader(f"Chunk {i + 1}")

    #  st.text_area(
    #      f"Chunk {i + 1}",
    #     chunk,
    #     height=200
    # )
     
    