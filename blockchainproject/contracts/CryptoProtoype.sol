// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract CryptoPrototype {
    struct Transaction {
        address sender;
        address receiver;
        uint amount;
    }

    struct BlockStruct {
        uint index;
        uint timestamp;
        Transaction[] transactions;
        bytes32 previousHash;
        bytes32 hash;
        uint nonce;
    }

    BlockStruct[] public chain;
    Transaction[] public pendingTransactions;

    uint public difficulty = 3;
    uint public miningReward = 1;

    constructor() {
        createGenesisBlock();
    }

    function createGenesisBlock() private {
        BlockStruct storage genesisBlock = chain.push();
        genesisBlock.index = 0;
        genesisBlock.timestamp = block.timestamp;
        genesisBlock.previousHash = 0x0;
        genesisBlock.hash = 0x0;
        genesisBlock.nonce = 0;
    }

    function createTransaction(address _receiver, uint _amount) public {
        Transaction memory newTransaction = Transaction({
            sender: msg.sender,
            receiver: _receiver,
            amount: _amount
        });
        pendingTransactions.push(newTransaction);
    }

    function minePendingTransactions(address _miner) public {
        BlockStruct storage previousBlock = chain[chain.length - 1];
        bytes32 previousHash = previousBlock.hash;
        uint index = chain.length;

        BlockStruct storage newBlock = chain.push();
        newBlock.index = index;
        newBlock.timestamp = block.timestamp;
        newBlock.previousHash = previousHash;
        newBlock.nonce = 0;

        for (uint i = 0; i < pendingTransactions.length; i++) {
            newBlock.transactions.push(pendingTransactions[i]);
        }

        newBlock.hash = calculateHash(newBlock.index, newBlock.timestamp, newBlock.transactions, newBlock.previousHash, newBlock.nonce);
        delete pendingTransactions;
        
        createTransaction(_miner, miningReward);
    }

    function calculateHash(uint index, uint timestamp, Transaction[] memory transactions, bytes32 previousHash, uint nonce) private pure returns (bytes32) {
        bytes memory serializedTransactions = serializeTransactions(transactions);
        return keccak256(abi.encodePacked(index, timestamp, serializedTransactions, previousHash, nonce));
    }

    function serializeTransactions(Transaction[] memory transactions) private pure returns (bytes memory) {
        bytes memory serialized = "";
        for (uint i = 0; i < transactions.length; i++) {
            serialized = abi.encodePacked(serialized, transactions[i].sender, transactions[i].receiver, transactions[i].amount);
        }
        return serialized;
    }

    function chainLength() public view returns (uint) {
        return chain.length;
    }
}
