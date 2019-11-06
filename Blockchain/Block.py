"""
project: PyBlockchain
author: Abdel Rahman Hussein
email: abdelrahman146@outlook.com
github: http://github.com/abdelrahman146

This class defines the block
Block is the container where the signed SmartContracts are indexed
"""
import json

from helpers import hashing


class Block:

    def __init__(self, previous_block_hash, contracts, miner_public_key, miner_message):
        assert isinstance(contracts, list)
        self.previous_block_hash = previous_block_hash
        self.contracts = contracts
        self.miner_public_key = miner_public_key
        self.miner_message = miner_message

    def get_hash(self):
        data = self.get_dict()
        json_data = json.dumps(data)
        return hashing.hash(json_data)

    def get_dict(self):
        contracts_list = []
        for contract in self.contracts:
            contracts_list.append(contract.get_dict())
        return {
            'previous_block_hash': self.previous_block_hash,
            'contracts': contracts_list,
            'miner_public_key': self.miner_public_key,
            'miner_msg': self.miner_message
        }

    def get_json(self):
        return json.dumps(self.get_dict())


class Genesis(Block):
    def __init__(self, miner_public_key, miner_message):
        self.miner_public_key = miner_public_key
        self.miner_message = miner_message

    def get_hash(self):
        data = self.get_dict()
        json_data = json.dumps(data)
        return hashing.hash(json_data)

    def get_dict(self):
        return {
            'miner_public_key': self.miner_public_key,
            'miner_msg': self.miner_message
        }

    def get_json(self):
        return json.dumps(self.get_dict())