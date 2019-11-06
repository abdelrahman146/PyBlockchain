"""
project: PyBlockchain
author: Abdel Rahman Hussein
email: abdelrahman146@outlook.com
github: http://github.com/abdelrahman146

This class defines a Miner
The Miner is the machine that creates new blocks and add it to the Blockchain
"""


class Miner:

    def __init__(self, owner_public_key):
        self.owner_public_key = owner_public_key

    def mine(self):
        pass  # TODO
