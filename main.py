
from blockchain import Blockchain
from wallet import Wallet

def main():
    blockchain = Blockchain()
    alice_wallet = Wallet(blockchain)
    bob_wallet = Wallet(blockchain)

    alice_wallet.balance = 100
    alice_wallet.send_money(30, bob_wallet)
    bob_wallet.send_money(10, alice_wallet)

    blockchain.add_block(blockchain.pending_transactions)

    for block in blockchain.chain:
        print(f"Index: {block.index}, Transactions: {[(tx.sender, tx.receiver, tx.amount) for tx in block.transactions]}, Hash: {block.hash}")

if __name__ == "__main__":
    main()
