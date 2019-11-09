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

from Blockchain.Blockchain import get_blockchain
from SmartContracts.SmartContract import SmartContract
from helpers import hashing


class SendContract(SmartContract, ABC):
    def __init__(self, contract_issuer_pk, contract_counterparty_pk, amount, msg, signature):
        super().__init__('SEND', contract_issuer_pk, amount, msg, signature)
        self.contract_counterparty_pk = contract_counterparty_pk

    def run_contract(self):
        pass

    def get_hash(self):
        data = self.get_dict()
        json_data = json.dumps(data)
        return hashing.hash(json_data)


    def is_valid_contract(self):
        signature_valid = super().is_valid_contract()
        pk_balance = get_blockchain().get_pk_balance(self.contract_issuer_pk)
        if pk_balance >= self.amount:
            return True and signature_valid
        print('not enough balance in wallet')
        return False

    def get_dict(self):
        dict = {
            'contract_name': self.contract_name,
            'contract_issuer_pk': hashing.hash(self.contract_issuer_pk),
            'contract_counterparty_pk': hashing.hash(self.contract_counterparty_pk),
            'amount': self.amount,
            'msg': self.msg
        }
        dict_json = json.dumps(dict)
        dict.update({'contract_hash': hashing.hash(dict_json)})
        return dict

    def get_json(self):
        return json.dumps(self.get_dict())

