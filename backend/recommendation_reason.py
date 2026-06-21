def generate_recommendation_reason(
    recommendation,
    overall_score,
    risk_level
):

    reasons = []

    if overall_score >= 80:
        reasons.append(
            "Strong overall interview performance"
        )

    elif overall_score >= 60:
        reasons.append(
            "Acceptable interview performance"
        )

    else:
        reasons.append(
            "Low interview performance"
        )

    if risk_level == "Low":

        reasons.append(
            "Low interview risk"
        )

    elif risk_level == "Medium":

        reasons.append(
            "Minor interview concerns detected"
        )

    else:

        reasons.append(
            "High interview risk detected"
        )

    return {
        "recommendation": recommendation,
        "reasons": reasons
    }