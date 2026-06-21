from rag import (
    chunk_text,
    create_embeddings,
    create_faiss_index,
    retrieve_chunks
)

sample_text = """
Python developer with FastAPI experience.
Built Machine Learning projects.
Worked with AWS and Docker.
Created REST APIs.
""" * 50

chunks = chunk_text(sample_text)

embeddings = create_embeddings(
    chunks
)

index = create_faiss_index(
    embeddings
)

print(
    "Vectors Stored:",
    index.ntotal
)

results = retrieve_chunks(
    "AWS Docker experience",
    chunks,
    index
)

print("\nRetrieved Chunks:\n")

for r in results:

    print(r[:150])
    print("-" * 50)