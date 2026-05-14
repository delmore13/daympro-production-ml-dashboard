\# DAYMPRO Production ML Dashboard



DAYMPRO is a production-style machine learning dashboard for real-time trading signal monitoring, risk analysis, and mock broker-safe decision tracking.



This project is designed as a portfolio-ready AI/ML software engineering system. It demonstrates how machine learning-style signal logic, risk controls, API development, automated testing, and dashboard monitoring can be combined into a clean production workflow.



\## Project Screenshots



\### FastAPI Documentation



!\[FastAPI Docs](screenshots/fastapi\_docs.png)



\### Streamlit Monitoring Dashboard



!\[Streamlit Dashboard](screenshots/streamlit\_dashboard.png)



\### Passing Test Suite



!\[Pytest Passed](screenshots/pytest\_passed.png)





\## Features



\- FastAPI backend for signal and risk endpoints

\- Streamlit dashboard for visual monitoring

\- Signal engine for market decision logic

\- Risk engine for trade safety checks

\- Mock broker-safe architecture

\- Automated test suite with Pytest

\- Modular Python project structure

\- Production-style separation of API, engine logic, dashboard, and tests



\## Tech Stack



\- Python

\- FastAPI

\- Streamlit

\- Pytest

\- Pydantic

\- Uvicorn

\- Git / GitHub



\## Project Structure



```text

daympro-production-ml-dashboard/

├── app/

│   ├── main.py

│   ├── signal\_engine.py

│   └── risk\_engine.py

├── dashboard/

├── data/

├── logs/

├── tests/

│   ├── test\_api.py

│   ├── test\_signal\_engine.py

│   └── test\_risk\_engine.py

├── requirements.txt

└── README.md

