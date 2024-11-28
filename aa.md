# NIFTY Price API

A Flask API to fetch NIFTY 50 index prices using Yahoo Finance data.

## Features

- Real-time NIFTY 50 index data
- Automatic timezone conversion to IST
- CORS enabled for cross-origin requests
- Health check endpoint

## Endpoints

### GET /api/nifty
Fetches the current NIFTY 50 index price and related information.

Response format:
```json
{
    "success": true,
    "data": {
        "index_name": "NIFTY 50",
        "last_price": 19345.65,
        "change": 123.45,
        "percent_change": 0.64,
        "timestamp": "28-Nov-2023 15:30:00"
    }
}
```

### GET /health
Health check endpoint to verify if the API is running.

## Setup and Running

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the application:
   ```
   python app.py
   ```

The API will be available at `http://localhost:5001`

## Notes

- Data is sourced from Yahoo Finance using the ^NSEI ticker
- All timestamps are in Indian Standard Time (IST)
- Price updates may have a slight delay due to data provider limitations