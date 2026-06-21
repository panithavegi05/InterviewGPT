from langchain_ollama import OllamaLLM

llm = OllamaLLM(
    model="llama3"
)

def evaluate_code(problem, code):

    prompt = f"""
    Problem:
    {problem}

    Candidate Code:
    {code}

    Evaluate:

    1. Correctness
    2. Time Complexity
    3. Code Quality

    Give score out of 100.
    """

    response = llm.invoke(prompt)

    return response