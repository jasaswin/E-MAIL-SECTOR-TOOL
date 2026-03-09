def classify_sector(text):
    """
    Classifies company sector based on keyword frequency.
    Returns (sector, confidence_score)
    """

    if not text:
        return "Unknown", 0.0

    text = text.lower()

    sector_keywords = {

    "IT Services": [
        "software","technology","cloud","developer",
        "platform","digital","ai","data","enterprise"
    ],

    "Finance": [
        "bank","finance","loan","investment","insurance"
    ],

    "E-Commerce": [
        "shopping","marketplace","retail","buy","sell"
    ]
}
    scores = {}

    for sector, keywords in sector_keywords.items():
        score = 0
        for keyword in keywords:
            score += text.count(keyword)
        scores[sector] = score

    best_sector = max(scores, key=scores.get)
    max_score = scores[best_sector]

    if max_score == 0:
        return "Unknown", 0.0

    total_score = sum(scores.values())
    confidence = round(max_score / total_score, 2) if total_score > 0 else 0

    return best_sector, confidence


def confidence_score(domain, company, sector):

    score = 0

    if domain:
        score += 1

    if company != "Unknown":
        score += 1

    if sector != "Unknown":
        score += 1

    if score == 3:
        return "High"

    if score == 2:
        return "Medium"

    return "Low"