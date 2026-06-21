def build_evidence_panel(
    anti_cheat_events
):

    evidence = []

    for event in anti_cheat_events:

        if event == "tab_switch":

            evidence.append(
                "Tab switched during interview"
            )

        elif event == "copy_paste":

            evidence.append(
                "Large answer pasted"
            )

        elif event == "inactivity":

            evidence.append(
                "Long inactivity detected"
            )

        else:

            evidence.append(
                event
            )

    return {
        "evidence": evidence,
        "review_recommended":
            len(evidence) > 0
    }