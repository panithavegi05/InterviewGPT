def evaluate_candidate(
    technical_score,
    behavioral_score,
    confidence_score,
    attention_score,
    anti_cheat_events
):

    anti_cheat_penalty = (
        len(anti_cheat_events) * 2
    )

    overall_score = (
        technical_score +
        behavioral_score +
        confidence_score +
        attention_score
    ) / 4

    overall_score -= anti_cheat_penalty

    if overall_score < 0:
        overall_score = 0

    return {
        "technical_score": technical_score,
        "behavioral_score": behavioral_score,
        "confidence_score": confidence_score,
        "attention_score": attention_score,
        "anti_cheat_events": len(
            anti_cheat_events
        ),
        "overall_score": round(
            overall_score,
            2
        )
    }