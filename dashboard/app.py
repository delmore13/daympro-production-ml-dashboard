import streamlit as st
import requests

st.set_page_config(
    page_title="DAYMPRO Production ML Dashboard",
    page_icon="📈",
    layout="wide"
)

st.title("DAYMPRO Production ML Dashboard")
st.write("Mock trading signal and risk monitoring dashboard for production-style ML engineering.")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    pair = st.selectbox("Currency Pair", ["EUR_USD", "GBP_USD", "USD_JPY", "GBP_JPY"])

with col2:
    momentum_score = st.slider("Momentum Score", 0, 100, 72)

with col3:
    trend_strength = st.slider("Trend Strength", 0, 100, 81)

volatility_score = st.slider("Volatility Score", 0, 100, 35)
price = st.number_input("Current Price", value=1.0850, format="%.5f")

payload = {
    "pair": pair,
    "price": price,
    "momentum_score": momentum_score,
    "trend_strength": trend_strength,
    "volatility_score": volatility_score
}

st.subheader("Signal Request")
st.json(payload)

if st.button("Generate Signal"):
    try:
        response = requests.post("http://127.0.0.1:8000/predict", json=payload)
        response.raise_for_status()
        result = response.json()

        st.subheader("Signal Result")
        st.success("Signal generated successfully")
        st.json(result)

    except requests.exceptions.ConnectionError:
        st.error("FastAPI server is not running. Start it with: python -m uvicorn app.main:app --reload")
    except Exception as e:
        st.error(f"Something went wrong: {e}")