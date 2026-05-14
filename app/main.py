from fastapi import FastAPI

from app.schemas import MarketSnapshot, SignalResponse
from app.signal_engine import generate_signal
from app.risk_engine import calculate_risk_level


app = FastAPI(
    title="DAYMPRO Production ML Dashboard",
    description="Production-style trading signal and risk monitoring API using mock market data.",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "message": "DAYMPRO Production ML Dashboard API is running",
        "status": "healthy",
    }


@app.post("/signal", response_model=SignalResponse)
def create_signal(snapshot: MarketSnapshot):
    signal_data = generate_signal(snapshot)

    risk_level = calculate_risk_level(
        confidence=signal_data["confidence"],
        volatility_score=snapshot.volatility_score,
    )

    return {
        **signal_data,
        "risk_level": risk_level,
    }
