# main.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from web3 import Web3

app = Flask(__name__)
CORS(app)

# Connect to local Ethereum node
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

@app.route('/')
def hello():
    return 'Hello, this is the blockchain backend!'

@app.route('/balance', methods=['POST'])
def get_balance():
    data = request.get_json()
    address = data.get('address')
    balance = w3.eth.get_balance(address)
    return jsonify({'balance': balance})

@app.route('/transaction', methods=['POST'])
def create_transaction():
    data = request.get_json()
    sender = data.get('sender')
    recipient = data.get('recipient')
    amount = data.get('amount')
    
    transaction = Transaction(sender, recipient, amount)
    blockchain.create_transaction(transaction)
    
    return jsonify({'message': 'Transaction created successfully'})

if __name__ == '__main__':
    app.run(debug=True)
