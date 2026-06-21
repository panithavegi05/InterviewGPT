from recruiter_summary import (
    generate_recruiter_summary
)

summary = generate_recruiter_summary(
    overall_score=82.75,
    strengths=[
        "Strong technical knowledge",
        "Good communication skills",
        "Confident during interview"
    ],
    weaknesses=[],
    risk_level="Medium"
)

print(summary)