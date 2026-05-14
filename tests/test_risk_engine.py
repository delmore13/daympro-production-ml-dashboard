from app.risk_engine import calculate_risk_level


def test_high_volatility_returns_high_risk():
    result = calculate_risk_level(confidence=0.90, volatility_score=85)

    assert result == "High"


def test_strong_confidence_and_low_volatility_returns_low_risk():
    result = calculate_risk_level(confidence=0.80, volatility_score=40)

    assert result == "Low"


def test_medium_confidence_returns_medium_risk():
    result = calculate_risk_level(confidence=0.60, volatility_score=55)

    assert result == "Medium"
