from langchain_ollama import OllamaLLM

llm = OllamaLLM(
    model="llama3"
)

def generate_question(skills, level):

    prompt = f"""
    You are a senior technical interviewer.

    Candidate Skills:
    {skills}

    Difficulty:
    {level}

    Generate ONE interview question.

    Return only the question.
    """

    response = llm.invoke(prompt)

    return response