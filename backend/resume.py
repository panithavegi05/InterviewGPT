from pypdf import PdfReader

def extract_text(pdf_path):

    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text

    return text
skills_db = [
    "Python",
    "Java",
    "C++",
    "FastAPI",
    "SQL",
    "PostgreSQL",
    "AWS",
    "Docker",
    "Machine Learning",
    "TensorFlow",
    "React",
    "JavaScript"
]

def extract_skills(text):

    found_skills = []

    for skill in skills_db:

        if skill.lower() in text.lower():

            found_skills.append(skill)

    return found_skills