"""
project: PyBlockchain
author: Abdel Rahman Hussein
email: abdelrahman146@outlook.com
github: http://github.com/abdelrahman146

This class defines the block
Block is the container where the signed SmartContracts are indexed
"""


class Block:

    def __init__(self, previous_block_hash, contracts, miner_public_key, miner_message):
        assert isinstance(contracts, list)
        self.previous_block_hash = previous_block_hash
        self.contracts = contracts
        self.miner_public_key = miner_public_key
        self.miner_message = miner_message

    def get_hash(self):
        pass  # TODO

    def get_dict(self):
        pass  # TODO

    def get_json(self):
        pass  # TODO
