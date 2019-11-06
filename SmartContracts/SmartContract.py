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


class SmartContract(ABC):

    @abstractmethod
    def is_valid_contract(self):
        pass

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
