from langchain_ollama import OllamaLLM

llm = OllamaLLM(
    model="llama3"
)

def generate_followup(question, answer):

    prompt = f"""
    Original Question:
    {question}

    Candidate Answer:
    {answer}

    Generate ONE follow-up interview question.

    Return only the question.
    """

    response = llm.invoke(prompt)

    return response