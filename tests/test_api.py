from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root_endpoint_returns_health_message():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_signal_endpoint_returns_buy_signal():
    payload = {
        "pair": "EUR_USD",
        "price": 1.085,
        "momentum_score": 75,
        "trend_strength": 82,
        "volatility_score": 35,
    }

    response = client.post("/signal", json=payload)

    assert response.status_code == 200

    data = response.json()
    assert data["pair"] == "EUR_USD"
    assert data["signal"] == "BUY"
    assert data["risk_level"] == "Low"
    assert data["confidence"] >= 0.75
