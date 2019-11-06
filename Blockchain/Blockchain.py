"""
Project: PyBlockchain
Author: Abdel Rahman Hussein
Email: abdelrahman146@outlook.com
github: http://github.com/abdelrahman146

This class defines the blockchain
"""


class Blockchain:

    def __init__(self):
        self.blocks = {}

    # return the top most block
    def peak(self):
        pass  # TODO

    # insert a new block
    def insert_block(self, block):
        pass  # TODO

    # get the balance of a public key
    def get_utxos(self, public_key):
        pass  # TODO

    # compare which blockchain is taller
    def get_height(self):
        pass  # TODO

    # check the validity of the received blockchain
    def is_valid_blockchain(self, blocks):
        pass  # TODO

    # retrieve blockchain json
    def get_json(self):
        pass  # TODO

    # retrieve blockchain dict
    def get_dict(self):
        pass  # TODO

    # retrieve blockchain hashes
    def get_dict(self):
        pass  # TODO
