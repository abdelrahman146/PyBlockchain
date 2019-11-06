"""
Project: PyBlockchain
Author: Abdel Rahman Hussein
Email: abdelrahman146@outlook.com
github: http://github.com/abdelrahman146

This class defines the block
"""


class Block:

    def __init__(self, previous_block_hash, transactions, nonce):
        assert isinstance(transactions, list)
        assert isinstance(nonce, int)
        self.previous_block_hash = previous_block_hash
        self.transactions = transactions
        self.nonce = nonce

    def get_hash(self):
        pass  # TODO

    def get_dict(self):
        pass  # TODO

    def get_json(self):
        pass  # TODO
