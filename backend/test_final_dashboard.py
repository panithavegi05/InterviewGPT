from recruiter_dashboard import build_dashboard
from dashboard_evidence import build_evidence_panel
from final_dashboard import build_final_dashboard

dashboard = build_dashboard(
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

evidence = build_evidence_panel(
    [
        "tab_switch",
        "copy_paste",
        "inactivity"
    ]
)

result = build_final_dashboard(
    dashboard,
    evidence
)

print(result)