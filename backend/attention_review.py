def attention_review(attention_percentage):

    if attention_percentage >= 80:

        return {
            "review_recommended": False,
            "reason": "Candidate maintained good attention"
        }

    elif attention_percentage >= 60:

        return {
            "review_recommended": False,
            "reason": "Candidate attention was acceptable"
        }

    else:

        return {
            "review_recommended": True,
            "reason": "Low attention detected during interview"
        }