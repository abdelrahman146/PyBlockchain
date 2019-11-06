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


class Wallet:
    def __init__(self):
        self.private_key = crypto.generate_private_key()
        self.password = crypto.generate_password()
        self.public_key = crypto.generate_public_key(private_key=self.private_key)
        self.blockchain = get_blockchain()
        self.mempool = get_mempool()

    def get_balance(self):
        return self.blockchain.get_pk_balance(self.public_key)

    def send(self, amount, contract_counterparty_pk, msg):
        contract_json = json.dumps({
            'contract_name': 'SEND',
            'contract_issuer_pk': self.public_key,
            'contract_counterparty_pk': contract_counterparty_pk,
            'amount': amount,
            'msg': msg
        })
        signature = crypto.sign(
            private_pem_string=crypto.generate_private_pem_string(self.private_key,self.password),
            password=self.password,
            message=hashing.hash(contract_json)
        )
        contract = SendContract(
            contract_issuer_pk=self.public_key,
            contract_counterparty_pk=contract_counterparty_pk,
            amount=amount,
            msg=msg,
            signature= signature
        )
        self.mempool.insert_contract(contract=contract)

    def issue(self, amount, msg=''):
        contract_json = json.dumps({
            'contract_name': 'ISSUE',
            'contract_issuer_pk': self.public_key,
            'amount': amount,
            'msg': msg
        })
        signature = crypto.sign(
            private_pem_string=crypto.generate_private_pem_string(self.private_key,self.password),
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
        contract_json = json.dumps({
            'contract_name': 'REDEEM',
            'contract_issuer_pk': self.public_key,
            'amount': amount,
            'msg': msg
        })
        signature = crypto.sign(
            private_pem_string=crypto.generate_private_pem_string(self.private_key,self.password),
            password=self.password,
            message=hashing.hash(contract_json)
        )
        contract = RedeemContract(
            contract_issuer_pk=self.public_key,
            amount=amount,
            msg=msg,
            signature= signature
        )
        self.mempool.insert_contract(contract=contract)
