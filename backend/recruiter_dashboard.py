def build_dashboard(
    candidate_name,
    technical_score,
    behavioral_score,
    confidence_score,
    attention_score,
    overall_score,
    recommendation,
    risk_level,
    final_decision
):

    return {
        "candidate_name": candidate_name,
        "technical_score": technical_score,
        "behavioral_score": behavioral_score,
        "confidence_score": confidence_score,
        "attention_score": attention_score,
        "overall_score": overall_score,
        "recommendation": recommendation,
        "risk_level": risk_level,
        "final_decision": final_decision
    }