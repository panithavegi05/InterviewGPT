def calculate_attention(face_frames, away_frames):

    total = face_frames + away_frames

    if total == 0:

        return {
            "attention_percentage": 0,
            "status": "No Data"
        }

    attention = (
        face_frames / total
    ) * 100

    if attention >= 80:

        status = "Focused"

    elif attention >= 60:

        status = "Mostly Focused"

    else:

        status = "Needs Review"

    return {
        "attention_percentage": round(attention, 2),
        "status": status
    }