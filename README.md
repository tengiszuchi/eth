# Automated Ethereum Classic Mining and Donation
This Python program automates the process of:

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
    - Download and install ```ethminer``` from the official repository.

## Setup Instructions
Clone or Download the Script:
- Save the script to a file named ```main.py```.
- Install Required Python Packages:
    - ```pip install web3 eth-account```
- Install Ethminer

## Variables to Change
Before running the script, you need to replace placeholder values with actual data:

- Mining Pool URL:
Locate the following line in the script:
```mining_pool_url = 'stratum+tcp://your.miningpool.url:port'```
Replace 'stratum+tcp://your.miningpool.url:port' with the URL and port of your chosen Ethereum Classic mining pool.
- Worker Name (Optional):
```worker_name = 'worker1'```
You can change 'worker1' to any name you prefer for identifying your mining worker.
- Charity Wallet Address:
```charity_address = '0xYourCharityWalletAddress'```
Replace '0xYourCharityWalletAddress' with the actual Ethereum Classic (ETC) address of the charity to which you want to donate.
Ensure that the address is valid and intended for ETC, not ETH.
- RPC Endpoint (Optional):
```web3 = Web3(Web3.HTTPProvider('https://www.etcblockexplorer.com/api/eth_rpc'))```
The script uses a public ETC RPC endpoint. You can replace it with another reliable RPC provider if needed.
- Gas Price and Gas Limit (Optional):
```'gas': 21000,```
```'gasPrice': web3.toWei('0.00000002', 'ether'),```
Adjust the gasPrice according to the current network conditions. A higher gas price can result in faster transaction confirmations but will cost more.
- Donation Check Interval (Optional):
```time.sleep(3600)  # Sleep for 1 hour```
The script checks the wallet balance and attempts to send donations every hour. You can adjust the interval by changing the number of seconds in time.sleep().

## Running the program
- Ensure All Prerequisites Are Met:
- Run the Script:
```python main.py```
- Monitor the Output:
    - The script will display the new wallet's address and private key (keep the private key secure and do not share it).
    - It will start the mining process and display the mining process ID (PID).
    - Every hour (or the interval you set), it checks the wallet balance and attempts to send any mined ETC to the charity address.
    - Transaction hashes will be displayed upon successful transfers.

## Important Notes and Warnings
- Private Key Security:
    - Do not share your private key. It provides full access to your wallet and funds.
    - In this script, the private key is printed to the console for simplicity. In a production environment, you should securely store the private key and avoid displaying it.

## Mining Hardware Requirements:
- Effective mining requires powerful GPUs. Mining with insufficient hardware may not yield meaningful results.
- Consider the cost of electricity and hardware wear and tear.
- Be aware of the legal implications of cryptocurrency mining in your country or region.
- Ensure compliance with all local laws and regulations.
- Transactions on the Ethereum Classic network require gas fees paid in ETC.
- The script reserves a small amount of ETC (default is 0.01 ETC) in the wallet to cover transaction fees.
- Reliability of Public RPC Endpoints:
    - Public RPC endpoints may be unreliable or rate-limited.
    - For consistent performance, consider using a dedicated RPC provider or running your own Ethereum Classic node.
- Ensure that the charity wallet address is correct and that the organization accepts donations in ETC.
- Verify the legitimacy of the charity to ensure your donations are used appropriately.

## Why do this?
- Blockchain technology enables provably transparent charitable donations and fundraising by recording every transaction on a public, immutable ledger. When mining cryptocurrencies like Ethereum Classic (ETC) and donating the rewards to a charity, each transaction—from the mining reward to the donation—is permanently recorded on the blockchain. This transparency allows anyone to verify the flow of funds, ensuring that donations reach their intended recipients without interference or misappropriation. Donors and stakeholders can track the donations in real-time, fostering trust and accountability. The decentralized nature of blockchain eliminates the need for intermediaries, reducing overhead costs and increasing the efficiency of charitable contributions. By leveraging blockchain's inherent transparency, charitable organizations can enhance credibility and donors can have confidence that their contributions are making a genuine impact.


## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Author
[Tengis Zuchi](https://github.com/tengiszuchi)
