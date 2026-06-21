from langchain_ollama import OllamaLLM

llm = OllamaLLM(
    model="llama3"
)

def evaluate_answer(question, answer):

    prompt = f"""
    Question:
    {question}

    Candidate Answer:
    {answer}

    Evaluate the answer.

    Give only a score from 0 to 100.
    """

    response = llm.invoke(prompt)

    return response