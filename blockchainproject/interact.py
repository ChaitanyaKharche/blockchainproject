from web3 import Web3
import json

# Connect to Ganache
ganache_url = "http://127.0.0.1:8545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Check connection
if not web3.is_connected():
    print("Failed to connect to Ganache")
    exit()

# Set the default account
web3.eth.default_account = web3.eth.accounts[0]

# Load the contract ABI
with open('build/contracts/CryptoPrototype.json', 'r') as file:
    contract_json = json.load(file)
    contract_abi = contract_json['abi']

# Address of the deployed contract
contract_address = "0x1ef86e843a73114Fb90B8ceEe26A37041bA59b33"  # Replace with your contract address

# Create the contract instance
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# Interact with the contract
# Example: Get the length of the chain
length_of_chain = contract.functions.chainLength().call()
print(f"Length of the chain: {length_of_chain}")
