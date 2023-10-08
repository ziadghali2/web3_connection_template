from web3 import Web3


# Connect to Web3

INFURA = 'https://mainnet.infura.io/v3/b7de5915219d4885bf950a0c8ad389ad'
web3 = Web3(Web3.HTTPProvider(INFURA))
print(f'Connected: {web3.is_connected()}')


# Connect to contracts
target_address = web3.to_checksum_address("")
target_ABI = ""
target = web3.eth.contract(address=target_address, abi=target_ABI)


