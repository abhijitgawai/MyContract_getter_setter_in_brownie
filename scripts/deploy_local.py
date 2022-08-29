from dis import Bytecode
from brownie import accounts, Wei, chain, network
from brownie import (OwnerTransfer)
from pyrsistent import s
from scripts.utils.helpful_scripts import *
from web3 import HTTPProvider, Web3


# owner = accounts[0]
# my_address = accounts[0].address
# chain_id = 80001
w3 = Web3(Web3.HTTPProvider(''))


def sign_deploy(contract, *args):
    transaction = contract.constructor(*args).buildTransaction(
    {
        "chainId": chain_id,
        "gasPrice": w3.eth.gas_price,
        "from": my_address,
        "nonce": w3.eth.getTransactionCount(my_address),
    })
    # Sign the transaction
    signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return tx_receipt.contractAddress
    

def set_addresses(contract, *args):
    transaction = contract.functions.setAddresses(*args).buildTransaction(
        {
        "chainId": chain_id,
        "gasPrice": w3.eth.gas_price,
        "from": my_address,
        "nonce": w3.eth.getTransactionCount(my_address),
    })
    # Sign the transaction
    signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)


def set_params(contract, *args):
    transaction = contract.functions.setParams(*args).buildTransaction(
        {
        "chainId": chain_id,
        "gasPrice": w3.eth.gas_price,
        "from": my_address,
        "nonce": w3.eth.getTransactionCount(my_address),
    })
    # Sign the transaction
    signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)


def deploy_eth():
    owner =  accounts[1]
    newContarctAddress = OwnerTransfer.deploy({"from":owner})
    print(newContarctAddress)


def main():
    # get_verified()
    deploy_eth()
