# Import the FastAPI and pydantic libraries.
from fastapi import FastAPI
from pydantic import BaseModel


# Defining a Trade model.
class Trade(BaseModel):
    counterparty: str
    instrument_id: str
    instrument_name: str
    trader: str
    trade_datetime: str
    trade_details: dict


# Creating a FastAPI app.
app = FastAPI()


# Defining a `get_trades` endpoint that returns a list of trades.
@app.get("/trades/")
def get_trades(
    search: str,
    asset_class: str = None,
    end: str = None,
    max_price: float = None,
    min_price: float = None,
    start: str = None,
    trade_type: str = None,
    page: int = 1,
    size: int = 10,
):
    # Get all trades from the database.
    trades = get_all_trades()

    # Filter the trades based on the query parameters.
    if search:
        trades = [trade for trade in trades if search.lower() in trade.lower()]
    if asset_class:
        trades = [trade for trade in trades if trade.asset_class == asset_class]
    if end:
        trades = [trade for trade in trades if trade.trade_datetime <= end]
    if max_price:
        trades = [trade for trade in trades if trade.trade_details.price <= max_price]
    if min_price:
        trades = [trade for trade in trades if trade.trade_details.price >= min_price]
    if start:
        trades = [trade for trade in trades if trade.trade_datetime >= start]
    if trade_type:
        trades = [trade for trade in trades if trade.trade_details.buySellIndicator == trade_type]

    # Paginate the trades.
    trades = trades.paginate(page=page, size=size)

    # Return the trades.
    return trades


# Defining a `get_trade` endpoint that returns a single trade by its ID.
@app.get("/trades/{trade_id}")
def get_trade(trade_id: str):
    # Get the trade from the database.
    trade = get_trade_by_id(trade_id)

    # Return the trade.
    return trade


# Defining a function to get all trades from the database.
def get_all_trades():
    # Mock database interaction layer here
    return [
        Trade(
            counterparty="Bob Smith",
            instrument_id="123456789",
            instrument_name="Apple",
            trader="John Doe",
            trade_datetime="2023-06-05T12:00:00",
            trade_details={"price": 100.0},
        ),
        Trade(
            counterparty="Jane Doe",
            instrument_id="987654321",
            instrument_name="Microsoft",
            trader="Mary Smith",
            trade_datetime="2023-06-06T13:00:00",
            trade_details={"price": 200.0},
        ),
    ]


# Defining a function to get a single trade by its ID from the database.
def get_trade_by_id(trade_id: str):
    # Mock database interaction layer here
    return get_all_trades()[0]


# Running the app in debug mode.
if __name__ == "__main__":
    app.run(debug=True)
