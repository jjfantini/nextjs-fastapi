import yfinance as yf
from fastapi import FastAPI

app = FastAPI()

@app.get("/api/python")
def hello_world():
    return {"message": "Hello World"}

@app.get("/api/healthcheck")
def healthcheck():
    return {"status": "Check, Check, 1..2...!"}

@app.get("/api/apple_stock")
def get_apple_stock():
    apple = yf.Ticker("AAPL")
    hist = apple.history(period="1d")
    latest_price = hist['Close'].iloc[-1]
    rounded_price = round(latest_price, 2)
    return {"price": rounded_price}
