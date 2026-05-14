def calculate_risk_level(confidence: float, volatility_score: float) -> str:
    """
    Simple risk classification layer for the DAYMPRO dashboard.
    """

    if volatility_score >= 80:
        return "High"

    if confidence >= 0.75 and volatility_score <= 50:
        return "Low"

    if confidence >= 0.50:
        return "Medium"

    return "High"
