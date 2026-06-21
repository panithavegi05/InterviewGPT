from recommendation_reason import (
    generate_recommendation_reason
)

result = generate_recommendation_reason(
    recommendation="Hire",
    overall_score=82.75,
    risk_level="Medium"
)

print(result)