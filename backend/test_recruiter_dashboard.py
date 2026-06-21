from recruiter_dashboard import (
    build_dashboard
)

result = build_dashboard(
    candidate_name="Panitha",
    technical_score=85,
    behavioral_score=80,
    confidence_score=90,
    attention_score=88,
    overall_score=82.75,
    recommendation="Hire",
    risk_level="Medium",
    final_decision="Proceed to next round"
)

print(result)