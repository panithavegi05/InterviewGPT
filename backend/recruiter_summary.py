def generate_recruiter_summary(
    overall_score,
    strengths,
    weaknesses,
    risk_level
):

    summary = f"""
Candidate Score: {overall_score}/100

Strengths:
"""

    for item in strengths:

        summary += f"\n• {item}"

    summary += "\n\nWeaknesses:"

    if weaknesses:

        for item in weaknesses:

            summary += f"\n• {item}"

    else:

        summary += "\n• No major weaknesses identified"

    summary += f"""

Risk Level:
• {risk_level}

Overall Assessment:
"""

    if overall_score >= 85:

        summary += (
            "Excellent candidate with strong "
            "technical and communication skills."
        )

    elif overall_score >= 70:

        summary += (
            "Good candidate with solid skills "
            "and potential for growth."
        )

    else:

        summary += (
            "Candidate requires further "
            "development before hiring."
        )

    return summary