"""
project: PyBlockchain
author: Abdel Rahman Hussein
email: abdelrahman146@outlook.com
github: http://github.com/abdelrahman146

This class defines the wallet
Wallet is the interface of the blockchain user. where the user can create new smart contracts
"""
import json

from Blockchain.Blockchain import get_blockchain
from Mempool import get_mempool
from SmartContracts.IssueContract import IssueContract
from SmartContracts.RedeemContract import RedeemContract
from SmartContracts.SendContract import SendContract
from helpers import crypto, hashing
import os

class Wallet:
    def __init__(self, name):
        self.name = name
        self.private_key_file_path = 'storage/private_key_%s.json' % name
        if os.path.isfile(self.private_key_file_path):
            self.private_key, self.password = self.load_from_file()
        else:
            self.password = crypto.generate_password()
            self.private_key = crypto.generate_private_pem_string(password=self.password)
            self.save_to_file()
        self.public_key = crypto.generate_public_pem_string(private_pem_string=self.private_key, password=self.password)
        self.blockchain = get_blockchain()
        self.mempool = get_mempool()

    def get_balance(self):
        return self.blockchain.get_pk_balance(self.public_key)

    def send(self, amount, contract_counterparty_pk, msg):
        dict = {
            'contract_name': 'SEND',
            'contract_issuer_pk': hashing.hash(self.public_key),
            'contract_counterparty_pk': hashing.hash(contract_counterparty_pk),
            'amount': amount,
            'msg': msg
        }
        dict_json = json.dumps(dict)
        dict.update({'contract_hash': hashing.hash(dict_json)})
        contract_json = json.dumps(dict)
        signature = crypto.sign(
            private_pem_string=self.private_key,
            password=self.password,
            message=hashing.hash(contract_json)
        )
        contract = SendContract(
            contract_issuer_pk=self.public_key,
            contract_counterparty_pk=contract_counterparty_pk,
            amount=amount,
            msg=msg,
            signature=signature
        )
        self.mempool.insert_contract(contract=contract)

    def issue(self, amount, msg=''):
        dict = {
            'contract_name': 'ISSUE',
            'contract_issuer_pk': hashing.hash(self.public_key),
            'amount': amount,
            'msg': msg
        }
        dict_json = json.dumps(dict)
        dict.update({'contract_hash': hashing.hash(dict_json)})
        contract_json = json.dumps(dict)
        signature = crypto.sign(
            private_pem_string=self.private_key,
            password=self.password,
            message=hashing.hash(contract_json)
        )
        contract = IssueContract(
            contract_issuer_pk=self.public_key,
            amount=amount,
            msg=msg,
            signature= signature
        )
        self.mempool.insert_contract(contract=contract)

    def redeem(self, amount, msg=''):
        dict = {
            'contract_name': 'REDEEM',
            'contract_issuer_pk': hashing.hash(self.public_key),
            'amount': amount,
            'msg': msg
        }
        dict_json = json.dumps(dict)
        dict.update({'contract_hash': hashing.hash(dict_json)})
        contract_json = json.dumps(dict)
        signature = crypto.sign(
            private_pem_string=self.private_key,
            password=self.password,
            message=hashing.hash(contract_json)
        )
        contract = RedeemContract(
            contract_issuer_pk=self.public_key,
            amount=amount,
            msg=msg,
            signature=signature
        )
        self.mempool.insert_contract(contract=contract)

    def save_to_file(self):
        data = {
            "private_key": self.private_key,
            "password": self.password
        }
        with open(self.private_key_file_path, "w") as output:
            output.write(json.dumps(data))

    def load_from_file(self):
        with open(self.private_key_file_path, "r") as input_file:
            data = json.loads(input_file.read())
            return data["private_key"], data["password"]

