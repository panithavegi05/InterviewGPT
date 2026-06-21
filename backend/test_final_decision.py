from final_decision import (
    generate_final_decision
)

result = generate_final_decision(
    overall_score=82.75,
    recommendation="Hire",
    reasons=[
        "Strong overall interview performance",
        "Minor interview concerns detected"
    ]
)

print(result)