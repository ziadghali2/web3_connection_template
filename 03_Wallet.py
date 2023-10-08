from web3 import Web3

# Connect to Web3

INFURA = 'https://mainnet.infura.io/v3/b7de5915219d4885bf950a0c8ad389ad'
web3 = Web3(Web3.HTTPProvider(INFURA))
print(f'Connected: {web3.is_connected()}')

# Connect to contracts
target_address = web3.to_checksum_address("0x514910771AF9Ca656af840dff83E8264EcF986CA")

print(f'balance : {web3.eth.get_balance(target_address)}')
print(f'byte_code: {web3.to_hex(web3.eth.get_code(target_address))}')