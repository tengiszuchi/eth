import os
import subprocess
import time
from eth_account import Account
from web3 import Web3

# Function to create an Ethereum wallet
def create_wallet():
    acct = Account.create()
    address = acct.address
    private_key = acct.privateKey.hex()
    print(f"New wallet created:\nAddress: {address}\nPrivate Key: {private_key}\n")
    return address, private_key

# Function to start mining ETC
def start_mining(miner_address):
    # Replace with your mining pool details
    mining_pool_url = 'stratum+tcp://your.miningpool.url:port'
    worker_name = 'worker1'

    # Command to start mining
    command = f'ethminer -P {mining_pool_url} -U -O {miner_address}.{worker_name}'

    # Start the mining process
    print("Starting mining process...")
    process = subprocess.Popen(command, shell=True)
    print(f"Mining started with PID: {process.pid}\n")
    return process

# Function to send mined ETC to charity wallet
def send_etc_to_charity(web3, miner_address, private_key, charity_address):
    # Check balance
    balance = web3.eth.get_balance(miner_address)
    print(f"Current balance: {web3.fromWei(balance, 'ether')} ETC")

    if balance == 0:
        print("No balance to send. Waiting for mining rewards...\n")
        return False

    # Build the transaction
    txn = {
        'to': charity_address,
        'value': balance - web3.toWei(0.01, 'ether'),  # Keep 0.01 ETC for gas
        'gas': 21000,
        'gasPrice': web3.toWei('0.00000002', 'ether'),  # Adjust gas price as needed
        'nonce': web3.eth.get_transaction_count(miner_address),
        'chainId': 61  # Chain ID for Ethereum Classic
    }

    # Sign the transaction
    signed_txn = web3.eth.account.sign_transaction(txn, private_key=private_key)

    # Send the transaction
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    print(f"Transaction sent! TX Hash: {tx_hash.hex()}\n")
    return True

def main():
    # Create a new Ethereum wallet
    miner_address, private_key = create_wallet()

    # Connect to an ETC node (you can use a public RPC endpoint)
    web3 = Web3(Web3.HTTPProvider('https://www.etcblockexplorer.com/api/eth_rpc'))

    # Charity wallet address (replace with actual charity ETC address)
    charity_address = '0xYourCharityWalletAddress'

    # Start mining
    mining_process = start_mining(miner_address)

    try:
        while True:
            # Wait for a certain period before checking balance (e.g., every hour)
            time.sleep(3600)  # Sleep for 1 hour

            # Attempt to send ETC to charity
            success = send_etc_to_charity(web3, miner_address, private_key, charity_address)
            if success:
                print("Donation sent successfully!\n")

    except KeyboardInterrupt:
        print("Stopping mining process...")
        mining_process.terminate()
        mining_process.wait()
        print("Mining process stopped.")

if __name__ == '__main__':
    main()
