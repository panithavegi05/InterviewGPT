from langchain_ollama import OllamaLLM

llm = OllamaLLM(
    model="llama3"
)

def generate_behavioral_question():

    prompt = """
    Generate ONE behavioral interview question.

    Return only the question.
    """

    response = llm.invoke(prompt)

    return response