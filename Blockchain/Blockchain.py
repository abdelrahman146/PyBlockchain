"""
project: PyBlockchain
author: Abdel Rahman Hussein
email: abdelrahman146@outlook.com
github: http://github.com/abdelrahman146

This class defines the blockchain
Blockchain is the sequence of blocks that contains all the history of the system
"""
import json

from Blockchain.Block import Genesis
from helpers import crypto

the_blockchain = None

def get_blockchain():
    global the_blockchain
    if the_blockchain is None:
        the_blockchain = Blockchain()
    return the_blockchain


class Blockchain:

    def __init__(self):
        self.blocks = []
        password = crypto.generate_password()
        private_key = crypto.generate_private_pem_string(password=password)
        self.creator_public_key = crypto.generate_public_pem_string(private_pem_string=private_key, password=password)
        self.blocks.append(Genesis(miner_public_key=self.creator_public_key, miner_message='The GENESIS BLOCK'))

    # return the top most block
    def peak(self):
        return self.blocks[-1]

    # insert a new block
    def insert_block(self, block):
        self.blocks.append(block)

    def get_pk_balance(self, public_key):
        balance = 0
        for block in self.blocks:
            for contract in block.contracts:
                if contract.contract_name == 'ISSUE':
                    if contract.contract_issuer_pk == public_key:
                        balance = balance + contract.amount
                elif contract.contract_name == 'REDEEM':
                    if contract.contract_issuer_pk == public_key:
                        balance = balance - contract.amount
                elif contract.contract_name == 'SEND':
                    if contract.contract_issuer_pk == public_key:
                        balance = balance - contract.amount
                    if contract.contract_counterparty_pk == public_key:
                        balance = balance + contract.amount
        return balance

    def get_pk_contracts(self, public_key):
        contracts = []
        for block in self.blocks:
            for contract in block.contracts:
                if contract.contract_issuer_pk == public_key:
                    contracts.append(contract)
                elif contract.contract_name == 'SEND':
                    if contract.contract_counterparty_pk == public_key:
                        contracts.append(contract)
        return contracts

    # compare which blockchain is taller
    def get_height(self):
        return len(self.blocks)

    def get_balance(self):
        balance = 0
        for block in self.blocks:
            for contract in block.contracts:
                if contract.contract_name == 'ISSUE':
                    balance = balance + contract.amount
                elif contract.contract_name == 'REDEEM':
                    balance = balance - contract.amount
        return balance

    # check the validity of the received blockchain
    def is_valid_blockchain(self, blocks):
        pass  # TODO

    def store_block(self, block):
        pass  # TODO add the block in storage

    # retrieve blockchain json
    def get_json(self):
        return json.dumps(self.get_dict())

    # retrieve blockchain dict
    def get_dict(self):
        blocks_dict = []
        for block in self.blocks:
            blocks_dict.append(block.get_dict())
        return {
            'height': self.get_height(),
            'balance': self.get_balance(),
            'blocks': blocks_dict
        }
