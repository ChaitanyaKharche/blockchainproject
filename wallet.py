
from transaction import Transaction

class Wallet:
    def __init__(self, blockchain):
        self.blockchain = blockchain
        self.balance = 0

    def send_money(self, amount, receiver_wallet):
        if amount > self.balance:
            print("Insufficient funds")
            return

        transaction = Transaction(self, receiver_wallet, amount)
        self.blockchain.pending_transactions.append(transaction)
        print(f"Sent {amount} to {receiver_wallet}")
