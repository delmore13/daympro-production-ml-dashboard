from pydantic import BaseModel, Field


class MarketSnapshot(BaseModel):
    pair: str = Field(example="EUR_USD")
    price: float = Field(example=1.0850)
    momentum_score: float = Field(ge=0, le=100, example=72)
    trend_strength: float = Field(ge=0, le=100, example=81)
    volatility_score: float = Field(ge=0, le=100, example=35)


class SignalResponse(BaseModel):
    pair: str
    signal: str
    confidence: float
    risk_level: str
    suggested_action: str
