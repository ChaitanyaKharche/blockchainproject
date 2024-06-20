# Simple Cryptocurrency Project

## Overview

This project is a foundational crypto prototype developed using native Python. It focuses on basic blockchain operations (ops) like transaction handling, block mining, and wallet functionalities. The code serves as prototyping groundwork for scalable blockchain writing.

![image](https://github.com/ChaitanyaKharche/blockchainproject/assets/72820371/3ce1d8ba-e1f0-4d48-9325-4e9d2fbcf904)

## Key Aspects

### Blockchain Class
- Manages the chain of blocks
- Implements Proof-of-Work for block mining
- Handles pending transactions and mining rewards

### Block Class
- Contains transaction data
- Holds the hash of the previous block to maintain chain integrity
- Uses SHA-256 for hashing

### Transaction Class
- Simple representation of a transaction between two wallets
- Consists of a sender, receiver, and amount

### Wallet Class
- Simulates a basic cryptocurrency wallet
- Handles transactions and balance

## Running the Project

1. Make sure you have Python installed.
2. Run `main.py` to execute the blockchain code.

## Future Scope

- Implement Merkle Trees for efficient transaction verification
- Integrate a peer-to-peer network for decentralized operation
- Add smart contract functionality
- Optimize the proof-of-work algorithm for better scalability

## License

This project is for educational purposes. Feel free to use and modify the code.

