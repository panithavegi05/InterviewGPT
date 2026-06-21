from hiring_recommendation import (
    get_hiring_recommendation
)

result = get_hiring_recommendation(
    overall_score=82.75,
    risk_level="Medium"
)

print(result)