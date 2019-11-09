"""
project: PyBlockchain
author: Abdel Rahman Hussein
email: abdelrahman146@outlook.com
github: http://github.com/abdelrahman146
repo: http://github.com/abdelrahman146/PyBlockchain

This is the SmartContract abstract class
SmartContract is the factory of actions that can be made in the blockchain
"""

from abc import ABC, abstractmethod

from helpers import crypto, hashing


class SmartContract(ABC):

    def __init__(self, contract_name, contract_issuer_pk, amount, msg, signature):
        self.contract_name = contract_name
        self.contract_issuer_pk = contract_issuer_pk
        self.amount = amount
        self.msg = msg
        self.signature = signature

    def is_valid_contract(self):
        valid = crypto.verify_signature(
            public_pem_string=self.contract_issuer_pk,
            signature=self.signature,
            message=self.get_hash()
        )
        if not valid:
            print('signature is not valid')
        return valid

    @abstractmethod
    def run_contract(self):
        pass

    @abstractmethod
    def get_hash(self):
        pass

    @abstractmethod
    def get_dict(self):
        pass

    @abstractmethod
    def get_json(self):
        pass
