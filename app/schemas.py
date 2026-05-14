from pydantic import BaseModel, Field


class MarketSnapshot(BaseModel):
    pair: str = Field(json_schema_extra={"example": "EUR_USD"})
    price: float = Field(json_schema_extra={"example": 1.0850})
    momentum_score: float = Field(ge=0, le=100, json_schema_extra={"example": 72})
    trend_strength: float = Field(ge=0, le=100, json_schema_extra={"example": 81})
    volatility_score: float = Field(ge=0, le=100, json_schema_extra={"example": 35})


class SignalResponse(BaseModel):
    pair: str
    signal: str
    confidence: float
    risk_level: str
    suggested_action: str