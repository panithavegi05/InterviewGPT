from langchain_ollama import OllamaLLM

llm = OllamaLLM(
    model="llama3"
)

def generate_coding_question():

    prompt = """
    Generate one medium difficulty coding interview problem.

    Give:
    Title
    Problem Statement

    Keep it concise.
    """

    response = llm.invoke(prompt)

    return response