from app.schemas import MarketSnapshot


def generate_signal(snapshot: MarketSnapshot) -> dict:
    """
    Demo signal engine for the DAYMPRO production ML dashboard.
    This does not place real trades.
    """

    momentum = snapshot.momentum_score
    trend = snapshot.trend_strength
    volatility = snapshot.volatility_score

    confidence = round(
        (momentum * 0.45 + trend * 0.45 + (100 - volatility) * 0.10) / 100,
        2,
    )

    if momentum >= 70 and trend >= 70:
        signal = "BUY"
        suggested_action = "Strong trend continuation detected"
    elif momentum <= 30 and trend >= 70:
        signal = "SELL"
        suggested_action = "Bearish momentum inside strong trend conditions"
    else:
        signal = "HOLD"
        suggested_action = "No high-quality setup detected"

    return {
        "pair": snapshot.pair,
        "signal": signal,
        "confidence": confidence,
        "suggested_action": suggested_action,
    }
