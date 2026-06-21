def generate_evaluation_report(
    technical_score,
    behavioral_score,
    confidence_score,
    attention_score,
    anti_cheat_events
):

    strengths = []

    weaknesses = []

    if technical_score >= 80:
        strengths.append(
            "Strong technical knowledge"
        )
    else:
        weaknesses.append(
            "Needs technical improvement"
        )

    if behavioral_score >= 80:
        strengths.append(
            "Good communication skills"
        )
    else:
        weaknesses.append(
            "Behavioral responses need improvement"
        )

    if confidence_score >= 80:
        strengths.append(
            "Confident during interview"
        )
    else:
        weaknesses.append(
            "Low confidence"
        )

    if attention_score >= 80:
        strengths.append(
            "Maintained attention"
        )
    else:
        weaknesses.append(
            "Frequently distracted"
        )

    risk_level = "Low"

    if len(anti_cheat_events) >= 3:
        risk_level = "High"

    elif len(anti_cheat_events) >= 1:
        risk_level = "Medium"

    return {
        "strengths": strengths,
        "weaknesses": weaknesses,
        "risk_level": risk_level
    }