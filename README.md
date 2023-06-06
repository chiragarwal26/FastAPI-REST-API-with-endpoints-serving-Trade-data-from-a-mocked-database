# Building-a-FastAPI-REST-API-with-endpoints-serving-Trade-data-from-a-mocked-database : 

This API represents a common request when building an API. I have provided a set of endpoints for retrieving a list of Trades, retrieving a single trade by ID, searching against Trades, and filtering Trades.

# The code provided is a functional implementation of the API using FastAPI. It includes endpoints to : 
* retrieve a list of trades 
* retrieve a single trade by ID
* search for trades
* filter trades based on optional query parameters
* Pagination and sorting are also supported.


To run the API, save the code in a Python file (e.g., api.py) and execute it using the Python interpreter or a command line tool. Ensure that you have the FastAPI and Uvicorn packages installed. You can install them using pip:

# pip install fastapi uvicorn
Then, you can run the API using the following command:

# uvicorn api:app --reload

The API will be accessible at http://localhost:8000.
