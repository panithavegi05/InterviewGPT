def get_hiring_recommendation(
    overall_score,
    risk_level
):

    if overall_score >= 90 and risk_level == "Low":

        recommendation = "Strong Hire"

    elif overall_score >= 75:

        recommendation = "Hire"

    elif overall_score >= 60:

        recommendation = "Consider"

    else:

        recommendation = "Reject"

    return {
        "recommendation": recommendation
    }