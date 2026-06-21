from langchain_ollama import OllamaLLM

llm = OllamaLLM(
    model="llama3"
)

def evaluate_behavioral_answer(question, answer):

    prompt = f"""
    Behavioral Question:
    {question}

    Candidate Answer:
    {answer}

    Evaluate:

    1. Communication
    2. Leadership
    3. Problem Solving
    4. STAR Format

    Give:
    Communication Score
    Leadership Score
    Problem Solving Score
    STAR Score

    Also give a short feedback.
    """

    response = llm.invoke(prompt)

    return response