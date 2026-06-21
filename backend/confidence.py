def analyze_confidence(text):

    filler_words = [
        "um",
        "uh",
        "maybe",
        "like",
        "hmm",
        "not sure"
    ]

    count = 0

    for word in filler_words:

        count += text.lower().count(word)

    confidence = max(0, 100 - count * 10)

    return {
        "confidence": confidence,
        "filler_words": count
    }