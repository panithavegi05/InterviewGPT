from rag import (
    chunk_text,
    create_embeddings,
    create_faiss_index,
    retrieve_chunks
)

from langchain_ollama import OllamaLLM

llm = OllamaLLM(
    model="llama3"
)

def generate_rag_question(
    resume_text,
    query="technical experience"
):

    chunks = chunk_text(
        resume_text
    )

    embeddings = create_embeddings(
        chunks
    )

    index = create_faiss_index(
        embeddings
    )

    context = retrieve_chunks(
        query,
        chunks,
        index,
        top_k=3
    )

    context_text = "\n".join(
        context
    )

    prompt = f"""
    You are a senior technical interviewer.

    Candidate Resume Context:
    {context_text}

    Generate ONE interview question
    based on the candidate's experience.

    Return only the question.
    """

    question = llm.invoke(
        prompt
    )

    return question