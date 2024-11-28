from flask import Flask, jsonify
from flask_cors import CORS
import yfinance as yf
import pytz
from datetime import datetime

app = Flask(__name__)
CORS(app)

def get_ist_time():
    ist = pytz.timezone('Asia/Kolkata')
    return datetime.now(ist).strftime('%d-%b-%Y %H:%M:%S')

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Welcome to NSE API",
        "endpoints": {
            "/api/nifty": "Get NIFTY 50 index data",
            "/health": "Check API health"
        }
    }), 200

@app.route('/api/nifty', methods=['GET'])
def get_nifty_price():
    try:
        # Get NIFTY 50 data using Yahoo Finance (^NSEI is the ticker for NIFTY 50)
        nifty = yf.Ticker("^NSEI")
        hist = nifty.history(period="1d")
        
        if hist.empty:
            return jsonify({
                "success": False,
                "error": "Unable to fetch NIFTY 50 data"
            }), 503
        
        last_price = hist['Close'].iloc[-1]
        prev_close = hist['Open'].iloc[0]
        change = last_price - prev_close
        percent_change = (change / prev_close) * 100
        
        response = {
            "success": True,
            "data": {
                "index_name": "NIFTY 50",
                "last_price": round(last_price, 2),
                "change": round(change, 2),
                "percent_change": round(percent_change, 2),
                "timestamp": get_ist_time()
            }
        }
        return jsonify(response), 200
        
    except Exception as e:
        error_response = {
            "success": False,
            "error": f"Failed to fetch NIFTY data: {str(e)}"
        }
        return jsonify(error_response), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200