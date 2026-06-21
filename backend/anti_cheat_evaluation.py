def evaluate_anti_cheat(events):

    count = len(events)

    if count == 0:

        return {
            "review_recommended": False,
            "reason": "No suspicious activity detected"
        }

    elif count <= 2:

        return {
            "review_recommended": False,
            "reason": "Minor suspicious activity detected"
        }

    else:

        return {
            "review_recommended": True,
            "reason": "Multiple suspicious events detected"
        }