
from block import Block
from transaction import Transaction

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.pending_transactions = []
        self.mining_reward = 10
        self.difficulty = 4

    def create_genesis_block(self):
        return Block(0, [], "0")

    def add_block(self, transactions):
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), transactions, previous_block.hash)
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)
