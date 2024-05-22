from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import json
import requests
import random
      
app = Flask(__name__)
cors = CORS(app, origins=['http://localhost:4200'])
app.config['CORS_HEADERS'] = 'application/json'

@app.route('/api/exchange')
@cross_origin()
def api1s():
    fromCurrency = request.args.get("from")
    toCurrency = request.args.get("to")
    ratesSoles = {'USD' : 3.75, 'EUR': 3.98}
    amount = float( request.args.get("amount"))
    rate = 1.0
    if(toCurrency == 'SOL'):
        rate = ratesSoles[fromCurrency]
    elif fromCurrency == 'SOL':
        rate = 1.0 / ratesSoles[toCurrency]
    else:
        return jsonify({'amount': 0.0, 'message': 'moneda no soportada'})
    return jsonify({'amount': round(amount * rate, 2)})
#http://127.0.0.1:5000/api1

if __name__ == '__main__':
    app.run(debug=True, threaded=False, port=5000)
