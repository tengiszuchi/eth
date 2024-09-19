# Automated Ethereum Classic Mining and Donation
This Python script automates the process of:

- Creating a new Ethereum Classic wallet.
- Mining Ethereum Classic (ETC) using ethminer or compatible mining software.
- Automatically donating mined ETC to a specified charity wallet address.

## Overview
This script is designed for individuals who wish to mine Ethereum Classic (ETC) and automatically donate the mined coins to a charitable cause. It simplifies the setup by handling wallet creation, mining initiation, and the transfer of funds to the charity's wallet.

## How It Works
- Wallet Creation: Generates a new Ethereum Classic wallet using the eth_account library. The wallet's address and private key are created programmatically.
- Mining Initiation: Starts the mining process by connecting to a specified ETC mining pool using ethminer. The mining rewards are sent to the newly created wallet.
- Automated Donation: Periodically checks the wallet's balance. When ETC is mined and available, the script automatically sends the balance (minus a small amount reserved for transaction fees) to the charity's wallet address.

## Prerequisites
- Operating System: Compatible with Windows, macOS, or Linux.
- Python 3.x: Ensure Python is installed on your system.
- Graphics Card (GPU): A powerful GPU is recommended for effective mining.
- Internet Connection: Required for mining and interacting with the blockchain.
- Required Software and Libraries
- Python Packages:

- ```pip install web3 eth-account```
- Ethminer:

Download and install ethminer from the official repository.
Setup Instructions
Clone or Download the Script:

Save the script to a file named mine_and_donate.py.

Install Required Python Packages:

bash
Copy code
pip install web3 eth-account
Install Ethminer:

Download ethminer suitable for your operating system.
Follow the installation instructions provided in the repository.
Variables to Change
Before running the script, you need to replace placeholder values with actual data:

Mining Pool URL:

Locate the following line in the script:

python
Copy code
mining_pool_url = 'stratum+tcp://your.miningpool.url:port'
Replace 'stratum+tcp://your.miningpool.url:port' with the URL and port of your chosen Ethereum Classic mining pool.

Example:

python
Copy code
mining_pool_url = 'stratum+tcp://etc-eu1.nanopool.org:19999'
Worker Name (Optional):

python
Copy code
worker_name = 'worker1'
You can change 'worker1' to any name you prefer for identifying your mining worker.
Charity Wallet Address:

python
Copy code
charity_address = '0xYourCharityWalletAddress'
Replace '0xYourCharityWalletAddress' with the actual Ethereum Classic (ETC) address of the charity to which you want to donate.
Ensure that the address is valid and intended for ETC, not ETH.
RPC Endpoint (Optional):

python
Copy code
web3 = Web3(Web3.HTTPProvider('https://www.etcblockexplorer.com/api/eth_rpc'))
The script uses a public ETC RPC endpoint. You can replace it with another reliable RPC provider if needed.

Example:

python
Copy code
web3 = Web3(Web3.HTTPProvider('https://etc-geth.0xinfra.com'))
Gas Price and Gas Limit (Optional):

python
Copy code
'gas': 21000,
'gasPrice': web3.toWei('0.00000002', 'ether'),
Adjust the gasPrice according to the current network conditions. A higher gas price can result in faster transaction confirmations but will cost more.
Donation Check Interval (Optional):

python
Copy code
time.sleep(3600)  # Sleep for 1 hour
The script checks the wallet balance and attempts to send donations every hour. You can adjust the interval by changing the number of seconds in time.sleep().
Running the Script
Ensure All Prerequisites Are Met:

Python and required packages are installed.
Ethminer is installed and configured.
Run the Script:

bash
Copy code
python mine_and_donate.py
Monitor the Output:

The script will display the new wallet's address and private key (keep the private key secure and do not share it).
It will start the mining process and display the mining process ID (PID).
Every hour (or the interval you set), it checks the wallet balance and attempts to send any mined ETC to the charity address.
Transaction hashes will be displayed upon successful transfers.
Stopping the Script:

To stop the script and the mining process, press Ctrl+C.
The script will handle the termination of the mining subprocess gracefully.
Important Notes and Warnings
Private Key Security:

Do not share your private key. It provides full access to your wallet and funds.
In this script, the private key is printed to the console for simplicity. In a production environment, you should securely store the private key and avoid displaying it.
Mining Hardware Requirements:

Effective mining requires powerful GPUs. Mining with insufficient hardware may not yield meaningful results.
Consider the cost of electricity and hardware wear and tear.
Electricity Costs:

Mining can consume significant electricity, potentially leading to high utility bills.
Ensure that the cost of electricity does not exceed the value of the mined ETC.
Legal Considerations:

Be aware of the legal implications of cryptocurrency mining in your country or region.
Ensure compliance with all local laws and regulations.
Gas Fees:

Transactions on the Ethereum Classic network require gas fees paid in ETC.
The script reserves a small amount of ETC (default is 0.01 ETC) in the wallet to cover transaction fees.
Reliability of Public RPC Endpoints:

Public RPC endpoints may be unreliable or rate-limited.
For consistent performance, consider using a dedicated RPC provider or running your own Ethereum Classic node.
Charity Verification:

Ensure that the charity wallet address is correct and that the organization accepts donations in ETC.
Verify the legitimacy of the charity to ensure your donations are used appropriately.
Security Best Practices:

Regularly update your software to patch any security vulnerabilities.
Use secure networks and avoid running the script on public or unsecured Wi-Fi.
Explanation of the Script
Imports and Dependencies
python
Copy code
import os
import subprocess
import time
from eth_account import Account
from web3 import Web3
os, subprocess: Used to interact with the operating system and start the mining process.
time: Allows the script to wait between donation checks.
eth_account: Provides functionalities for Ethereum account management.
web3: Enables interaction with the Ethereum Classic blockchain.
Functions
create_wallet()

Generates a new Ethereum Classic wallet.
Prints the wallet address and private key.
python
Copy code
def create_wallet():
    acct = Account.create()
    address = acct.address
    private_key = acct.privateKey.hex()
    print(f"New wallet created:\nAddress: {address}\nPrivate Key: {private_key}\n")
    return address, private_key
start_mining(miner_address)

Constructs the mining command using the mining pool URL, miner's address, and worker name.
Starts the mining process as a subprocess.
Prints the process ID for reference.
python
Copy code
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
send_etc_to_charity(web3, miner_address, private_key, charity_address)

Checks the miner's wallet balance.
If balance is greater than zero, it creates and signs a transaction to send ETC to the charity address.
Sends the transaction to the network and prints the transaction hash.
python
Copy code
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
Main Execution Flow
python
Copy code
def main():
    # Create a new Ethereum wallet
    miner_address, private_key = create_wallet()

    # Connect to an ETC node
    web3 = Web3(Web3.HTTPProvider('https://www.etcblockexplorer.com/api/eth_rpc'))

    # Charity wallet address
    charity_address = '0xYourCharityWalletAddress'

    # Start mining
    mining_process = start_mining(miner_address)

    try:
        while True:
            # Wait before checking balance
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
Wallet Creation: Calls create_wallet() to generate a new wallet.
Blockchain Connection: Establishes a connection to an ETC RPC endpoint.
Mining Process: Starts mining by calling start_mining(miner_address).
Donation Loop: Enters a loop where it sleeps for a specified interval, then checks the wallet balance and attempts to send any mined ETC to the charity.
Graceful Shutdown: Handles KeyboardInterrupt to terminate the mining process when the script is stopped.
License
This script is provided "as is" without warranty of any kind. Use it at your own risk. The author is not responsible for any losses or damages resulting from the use of this script.

### Author
Tengis Zuchi
