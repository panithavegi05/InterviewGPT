from dashboard_evidence import (
    build_evidence_panel
)

result = build_evidence_panel(
    [
        "tab_switch",
        "copy_paste",
        "inactivity"
    ]
)

print(result)