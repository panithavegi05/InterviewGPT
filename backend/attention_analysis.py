def analyze_attention(score):

    if score > 100:

        return {
            "attention_score": 95,
            "status": "Focused"
        }

    elif score > 50:

        return {
            "attention_score": 75,
            "status": "Mostly Focused"
        }

    else:

        return {
            "attention_score": 40,
            "status": "Needs Review"
        }