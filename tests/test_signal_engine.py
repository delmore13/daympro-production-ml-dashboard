from app.schemas import MarketSnapshot
from app.signal_engine import generate_signal


def test_generate_buy_signal_for_strong_momentum_and_trend():
    snapshot = MarketSnapshot(
        pair="EUR_USD",
        price=1.085,
        momentum_score=75,
        trend_strength=82,
        volatility_score=35,
    )

    result = generate_signal(snapshot)

    assert result["pair"] == "EUR_USD"
    assert result["signal"] == "BUY"
    assert result["confidence"] >= 0.75


def test_generate_hold_signal_for_weak_setup():
    snapshot = MarketSnapshot(
        pair="GBP_JPY",
        price=190.25,
        momentum_score=45,
        trend_strength=50,
        volatility_score=60,
    )

    result = generate_signal(snapshot)

    assert result["pair"] == "GBP_JPY"
    assert result["signal"] == "HOLD"
