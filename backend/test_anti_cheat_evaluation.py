from anti_cheat_evaluation import evaluate_anti_cheat

events = [
    {
        "event": "tab_switch"
    },
    {
        "event": "long_inactivity"
    },
    {
        "event": "tab_switch"
    }
]

print(
    evaluate_anti_cheat(events)
)