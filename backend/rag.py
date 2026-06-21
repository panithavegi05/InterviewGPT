from sentence_transformers import SentenceTransformer
import faiss
import numpy as np


# Load embedding model
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


# Split resume into chunks
def chunk_text(text, chunk_size=500):

    chunks = []

    for i in range(0, len(text), chunk_size):

        chunks.append(
            text[i:i + chunk_size]
        )

    return chunks


# Convert chunks into embeddings
def create_embeddings(chunks):

    embeddings = model.encode(
        chunks
    )

    return embeddings


# Store embeddings in FAISS
def create_faiss_index(embeddings):

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(
        dimension
    )

    index.add(
        np.array(
            embeddings,
            dtype=np.float32
        )
    )

    return index


# Retrieve most relevant chunks
def retrieve_chunks(
    query,
    chunks,
    index,
    top_k=3
):

    query_embedding = model.encode(
        [query]
    )

    distances, indices = index.search(
        np.array(
            query_embedding,
            dtype=np.float32
        ),
        top_k
    )

    results = []

    for idx in indices[0]:

        results.append(
            chunks[idx]
        )

    return results