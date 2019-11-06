"""
project: PyBlockchain
author: Abdel Rahman Hussein
email: abdelrahman146@outlook.com
github: http://github.com/abdelrahman146
repo: http://github.com/abdelrahman146/PyBlockchain

This class defines a Mempool
Mempool is the area where the signed and valid SmartContracts are kept
before being indexed in the blockchain
"""

the_mempool = None


def get_mempool():
    global the_mempool
    if the_mempool is None:
        the_mempool = Mempool()
    return the_mempool


class Mempool:

    def __init__(self):
        self.contracts = []

    def clean_pool(self):
        self.contracts = []

    # insert a new contract
    def insert_contract(self, contract):
        self.contracts.append(contract)

    # check contract is valid (the mempool can accept one smart contract for each public key)
    def is_valid_contract(self, contract):
        pass  # TODO
