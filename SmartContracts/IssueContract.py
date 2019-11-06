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
        self.contract_name = 'ISSUE'
        self.contract_issuer_pk = contract_issuer_pk
        self.amount = amount
        self.msg = msg
        self.signature = signature

    # this method runs when the miner collects the contracts form the mempool
    def run_contract(self):
        self.issue()

    # burn the amount
    def issue(self):
        pass  # TODO

    def get_hash(self):
        data = self.get_dict()
        json_data = json.dumps(data)
        return hashing.hash(json_data)

    def get_dict(self):
        return {
            'contract_name': self.contract_name,
            'contract_issuer_pk': self.contract_issuer_pk,
            'amount': self.amount,
            'msg': self.msg
        }

    def get_json(self):
        return json.dumps(self.get_dict())
