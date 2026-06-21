from interview import generate_question
from evaluation import evaluate_answer
from followup import generate_followup
from adaptive import get_level


def technical_round(skills, answer):

    question = generate_question(
        skills,
        "medium"
    )

    score = evaluate_answer(
        question,
        answer
    )

    level = get_level(score)

    followup = generate_followup(
        question,
        answer
    )

    return {
        "question": question,
        "score": score,
        "level": level,
        "followup": followup
    }