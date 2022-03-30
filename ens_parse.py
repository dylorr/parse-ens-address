# region WEB3/ENS INTEGRATION
from web3 import Web3
import pandas as pd
infura_url = 'https://mainnet.infura.io/v3/[auth]'
w3 = Web3(Web3.HTTPProvider(infura_url))
from ens import ENS
ns = ENS.fromWeb3(w3)
w3.isConnected() #check connection
# endregion

file = pd.read_csv('addresses_test - Sheet1.csv') #change to csv file name containint ens addresses
ens_addresses = file['address'] #change to column name containing ens addresses

hexadecimal = []
for x in ens_addresses:
    eth_address = ns.address(str(x))
    hexadecimal.append(eth_address)

hexadecimal_df = pd.DataFrame(hexadecimal, columns=['address'])
hexadecimal_df.to_csv('parsed_ens_addresses.csv')
print(hexadecimal_df)
