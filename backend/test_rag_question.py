from rag_question import generate_rag_question

resume_text = """
Python Developer

Built FastAPI APIs.
Worked with AWS EC2.
Used Docker containers.
Created Machine Learning projects.
"""

question = generate_rag_question(
    resume_text
)

print(question)