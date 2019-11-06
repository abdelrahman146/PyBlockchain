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


class SendContract(SmartContract, ABC):
    def __init__(self, contract_issuer_pk, contract_counterparty_pk, amount, msg, signature):
        self.contract_name = 'SEND'
        self.contract_issuer_pk = contract_issuer_pk
        self.contract_counterparty_pk = contract_counterparty_pk
        self.amount = amount
        self.msg = msg
        self.signature = signature

    def run_contract(self):
        pass

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
            'contract_counterparty_pk': hashing.hash(self.contract_counterparty_pk),
            'amount': self.amount,
            'msg': self.msg
        }

    def get_json(self):
        return json.dumps(self.get_dict())