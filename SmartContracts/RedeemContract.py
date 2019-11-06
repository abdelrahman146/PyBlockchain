"""
project: PyBlockchain
author: Abdel Rahman Hussein
email: abdelrahman146@outlook.com
github: http://github.com/abdelrahman146
repo: http://github.com/abdelrahman146/PyBlockchain

This is the Send SmartContract
"""

import json
from abc import ABC

from SmartContracts.SmartContract import SmartContract
from helpers import hashing


class RedeemContract(SmartContract, ABC):
    def __init__(self, contract_issuer_pk, amount, msg, signature):
        self.contract_name = 'REDEEM'
        self.contract_issuer_pk = contract_issuer_pk
        self.amount = amount
        self.msg = msg
        self.signature = signature

    # this method runs when the miner collects the contracts form the mempool
    def run_contract(self):
        self.redeem()

    # burn the amount
    def redeem(self):
        pass  # TODO

    def get_hash(self):
        data = self.get_dict()
        json_data = json.dumps(data)
        return hashing.hash(json_data)

    def is_valid_contract(self):
        pass

    def get_dict(self):
        return {
            'contract_name': self.contract_name,
            'contract_issuer_pk': hashing.hash(self.contract_issuer_pk),
            'amount': self.amount,
            'msg': self.msg,
            'contract_hash': self.get_hash()
        }

    def get_json(self):
        return json.dumps(self.get_dict())
