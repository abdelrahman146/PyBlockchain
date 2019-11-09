"""
project: PyBlockchain
author: Abdel Rahman Hussein
email: abdelrahman146@outlook.com
github: http://github.com/abdelrahman146

This class defines the blockchain
Blockchain is the sequence of blocks that contains all the history of the system
"""
import json
import os

from Blockchain.Block import Genesis, Block
from helpers import crypto, hashing

the_blockchain = None

def get_blockchain():
    global the_blockchain
    if the_blockchain is None:
        the_blockchain = Blockchain()
    return the_blockchain



class Blockchain:

    def __init__(self):
        self.blockhain_file_path = 'storage/blockchain'
        if not os.path.isfile(self.blockhain_file_path):
            password = crypto.generate_password()
            private_key = crypto.generate_private_pem_string(password=password)
            self.creator_public_key = crypto.generate_public_pem_string(private_pem_string=private_key,password=password)
            self.insert_block(Genesis(miner_public_key=self.creator_public_key, miner_message='THE GENESIS BLOCK'))

    # return the top most block
    def peak(self):
        blockchain = self.load_blockchain()
        last_block = None
        for block in blockchain:
            last_block = block
        return last_block

    def get_height(self):
        blockchain = self.load_blockchain()
        counter = 0
        for block in blockchain:
            counter = counter + 1
        return counter

    # insert a new block
    def insert_block(self, block):
        assert isinstance(block, Block)
        assert self.is_valid_block(block)
        self.store_block(block)

    # store block in the blockchain file
    def store_block(self, block):
        with open('storage/blockchain', 'a+') as blockchain:
            blockchain.write(block.get_json() + '\n')


    def get_pk_balance(self, public_key):
        balance = 0
        blockchain = self.load_blockchain()
        public_key = hashing.hash(public_key)
        for block in blockchain:
            block = json.loads(block)
            for contract in block['contracts']:
                if contract['contract_name'] == 'ISSUE':
                    if contract['contract_issuer_pk'] == public_key:
                        balance = balance + int(contract['amount'])
                elif contract['contract_name'] == 'REDEEM':
                    if contract['contract_issuer_pk'] == public_key:
                        balance = balance - int(contract['amount'])
                elif contract['contract_name'] == 'SEND':
                    if contract['contract_issuer_pk'] == public_key:
                        balance = balance - int(contract['amount'])
                    if contract['contract_counterparty_pk'] == public_key:
                        balance = balance + int(contract['amount'])
        return balance

    def get_pk_contracts(self, public_key):
        contracts = []
        blockchain = self.load_blockchain()
        public_key = hashing.hash(public_key)
        for block in blockchain:
            block = json.loads(block)
            for contract in block['contracts']:
                if contract['contract_issuer_pk'] == public_key:
                    contracts.append(contract)
                elif contract.contract_name == 'SEND':
                    if contract['contract_counterparty_pk'] == public_key:
                        contracts.append(contract)
        return contracts

    def get_balance(self):
        balance = 0
        blockchain = self.load_blockchain()
        for block in blockchain:
            block = json.loads(block)
            for contract in block['contracts']:
                if contract['contract_name'] == 'ISSUE':
                    balance = balance + int(contract['amount'])
                elif contract['contract_name'] == 'REDEEM':
                    balance = balance - int(contract['amount'])
        return balance

    def is_valid_block(self, block):
        if self.get_height() > 0:
            pre_block = json.loads(self.peak())
            if block.previous_block_hash == pre_block['block_hash']:
                return True
            return False
        return True

    # print blockchain
    def print_blockchain(self):
        blockchain = self.load_blockchain()
        for i,block in blockchain:
            print('%d -> %s' % i, block)

    # load blocks from the blockchain DB
    def load_blockchain(self):
        with open(self.blockhain_file_path, 'r') as blockchain:
            for block in blockchain:
                yield block
