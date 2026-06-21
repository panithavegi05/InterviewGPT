from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from resume import extract_text, extract_skills
from interview import generate_question
from evaluation import evaluate_answer
from adaptive import get_level
from followup import generate_followup
from technical import technical_round
from coding import generate_coding_question
from behavioral import generate_behavioral_question
from behavioral_evaluation import evaluate_behavioral_answer
from confidence import analyze_confidence
from anti_cheat import log_event, get_events
from rag_question import generate_rag_question
from attention_score import (
    update_attention,
    get_attention
)
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "message": "InterviewGPT Backend Running"
    }

class Candidate(BaseModel):
    name: str
    email: str
    role: str

@app.post("/candidate")
def create_candidate(candidate: Candidate):

    return {
        "message": "Candidate Added",
        "candidate": {
            "name": candidate.name,
            "email": candidate.email,
            "role": candidate.role
        }
    }

@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):

    filepath = f"uploads/{file.filename}"

    with open(filepath, "wb") as buffer:
        buffer.write(await file.read())

    text = extract_text(filepath)

    skills = extract_skills(text)

    return {
        "filename": file.filename,
        "skills": skills
    }

@app.post("/generate-question")
def get_question():

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

    return {
        "question": question
    }

class InterviewAnswer(BaseModel):
    question: str
    answer: str

@app.post("/evaluate-answer")
def evaluate(data: InterviewAnswer):

    score = evaluate_answer(
        data.question,
        data.answer
    )

    return {
        "score": score
    }

@app.post("/adaptive-question")
def adaptive_question():

    previous_score = 85

    level = get_level(previous_score)

    skills = [
        "Python",
        "Machine Learning"
    ]

    question = generate_question(
        skills,
        level
    )

    return {
        "level": level,
        "question": question
    }

class FollowupRequest(BaseModel):
    question: str
    answer: str

@app.post("/followup-question")
def followup(data: FollowupRequest):

    question = generate_followup(
        data.question,
        data.answer
    )

    return {
        "followup_question": question
    }


class TechnicalRequest(BaseModel):
    answer: str


@app.post("/technical-round")
def start_round(data: TechnicalRequest):

    skills = [
        "Python",
        "Machine Learning"
    ]

    result = technical_round(
        skills,
        data.answer
    )

    return result

@app.get("/coding-question")
def coding_question():

    question = generate_coding_question()

    return {
        "question": question
    }

@app.get("/behavioral-question")
def behavioral_question():

    question = generate_behavioral_question()

    return {
        "question": question
    }

class BehavioralRequest(BaseModel):
    question: str
    answer: str


class ConfidenceRequest(BaseModel):
    text: str

class AntiCheatRequest(BaseModel):
    event: str

class AttentionRequest(BaseModel):
    score: int

@app.post("/behavioral-evaluation")
def behavioral_evaluation(data: BehavioralRequest):

    result = evaluate_behavioral_answer(
        data.question,
        data.answer
    )

    return {
        "evaluation": result
    }

@app.post("/confidence-analysis")
def confidence_analysis(data: ConfidenceRequest):

    result = analyze_confidence(data.text)

    return result

@app.post("/anti-cheat")
def anti_cheat(data: AntiCheatRequest):

    return log_event(data.event)


@app.get("/anti-cheat-events")
def anti_cheat_events():

    return get_events()

@app.post("/attention-score")
def save_attention(
    data: AttentionRequest
):

    return update_attention(
        data.score
    )


@app.get("/attention-score")
def attention_score():

    return get_attention()
