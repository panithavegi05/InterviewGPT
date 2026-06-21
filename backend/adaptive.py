def get_level(score):

    try:
        score = int(str(score).strip())

    except:
        score = 50

    if score >= 80:
        return "hard"

    elif score >= 50:
        return "medium"

    else:
        return "easy"