def generate_final_decision(
    overall_score,
    recommendation,
    reasons
):

    if recommendation in [
        "Strong Hire",
        "Hire"
    ]:

        decision = (
            "Proceed to next round"
        )

    elif recommendation == "Consider":

        decision = (
            "Needs recruiter review"
        )

    else:

        decision = (
            "Do not proceed"
        )

    return {
        "overall_score": overall_score,
        "recommendation": recommendation,
        "reasons": reasons,
        "final_decision": decision
    }