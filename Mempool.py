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
from SmartContracts.SmartContract import SmartContract

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
        assert isinstance(contract, SmartContract)
        assert contract.is_valid_contract()
        assert self.is_valid_contract(contract)
        self.contracts.append(contract)

    # check is valid (to elemenate double spending the mempool can accept one smart contract per pk)
    def is_valid_contract(self, contract):
        contract_issuer_pk = contract.contract_issuer_pk
        for contract in self.contracts:
            if contract.contract_issuer_pk == contract_issuer_pk:
                return False
        return True