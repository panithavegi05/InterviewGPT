from pdf_report import (
    generate_pdf_report
)

report = {

    "Candidate":
        "Panitha",

    "Overall Score":
        82.75,

    "Recommendation":
        "Hire",

    "Risk Level":
        "Medium",

    "Final Decision":
        "Proceed to next round",

    "Strengths": [
        "Strong technical knowledge",
        "Good communication skills",
        "Confident during interview"
    ],

    "Weaknesses": [
        "Minor anti-cheat concerns"
    ],

    "Evidence": [
        "Tab switched during interview",
        "Large answer pasted",
        "Long inactivity detected"
    ],

    "Review Recommended":
        True
}

generate_pdf_report(
    "candidate_report_v2.pdf",
    report
)