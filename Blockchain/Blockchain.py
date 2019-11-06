"""
project: PyBlockchain
author: Abdel Rahman Hussein
email: abdelrahman146@outlook.com
github: http://github.com/abdelrahman146

This class defines the blockchain
Blockchain is the sequence of blocks that contains all the history of the system
"""

the_blockchain = None


def get_blockchain():
    global the_blockchain
    if the_blockchain == None:
        the_blockchain = Blockchain()
    return the_blockchain

class Blockchain:

    def __init__(self):
        self.blocks = {}

    # return the top most block
    def peak(self):
        pass  # TODO

    # insert a new block
    def insert_block(self, block):
        pass  # TODO

    # compare which blockchain is taller
    def get_height(self):
        pass  # TODO

    # check the validity of the received blockchain
    def is_valid_blockchain(self, blocks):
        pass  # TODO

    def store_block(self, block):
        pass # TODO add the block in storage

    # retrieve blockchain json
    def get_json(self):
        pass  # TODO

    # retrieve blockchain dict
    def get_dict(self):
        pass  # TODO

    # retrieve blockchain hashes
    def get_dict(self):
        pass  # TODO
