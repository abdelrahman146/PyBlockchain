"""
Project: PyBlockchain
Author: Abdel Rahman Hussein
Email: abdelrahman146@outlook.com
github: http://github.com/abdelrahman146

This class defines a Miner
"""

class Miner:

    def __init__(self, owner_public_key):
        self.owner_public_key = owner_public_key
        while True:
            self.mine()

    def mine(self):
        pass  # TODO