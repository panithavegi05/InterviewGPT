from evaluation_report import (
    generate_evaluation_report
)

result = generate_evaluation_report(
    technical_score=85,
    behavioral_score=80,
    confidence_score=90,
    attention_score=88,
    anti_cheat_events=[
        "tab_switch",
        "copy_paste"
    ]
)

print(result)