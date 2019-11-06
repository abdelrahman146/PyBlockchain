"""
project: PyBlockchain
author: Abdel Rahman Hussein
email: abdelrahman146@outlook.com
github: http://github.com/abdelrahman146
repo: http://github.com/abdelrahman146/PyBlockchain

This is the Issue SmartContract
"""
from abc import ABC

from SmartContracts.SmartContract import SmartContract
import json

from helpers import hashing


class IssueContract(SmartContract, ABC):
    def __init__(self, contract_issuer_pk, amount, msg, signature):
        super().__init__('ISSUE', contract_issuer_pk, amount, msg, signature)

    # this method runs when the miner collects the contracts form the mempool
    def run_contract(self):
        self.issue()

    # issue the amount and deposit money in the reserve
    def issue(self):
        pass  # TODO

    def get_hash(self):
        data = self.get_dict()
        json_data = json.dumps(data)
        return hashing.hash(json_data)

    # TODO
    def is_valid_contract(self):
        return super().is_valid_contract()

    def get_dict(self):
        dict = {
            'contract_name': self.contract_name,
            'contract_issuer_pk': hashing.hash(self.contract_issuer_pk),
            'amount': self.amount,
            'msg': self.msg
        }
        dict_json = json.dumps(dict)
        dict.update({'contract_hash': hashing.hash(dict_json)})
        return dict

    def get_json(self):
        return json.dumps(self.get_dict())
