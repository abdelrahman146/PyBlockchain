"""
project: PyBlockchain
author: Abdel Rahman Hussein
email: abdelrahman146@outlook.com
github: http://github.com/abdelrahman146

This class defines a Miner
The Miner is the machine that creates new blocks and add it to the Blockchain
"""

from Mempool import get_mempool
from Blockchain.Block import Block
from Blockchain.Blockchain import get_blockchain

the_miner = None


def get_miner():
    global the_miner
    if the_miner is None:
        the_miner = Miner()
    return the_miner


class Miner:
    def __init__(self, owner_public_key=None, owner_message=None):
        self.blockchain = get_blockchain()
        self.mempool = get_mempool()
        self.owner_public_key = owner_public_key
        self.owner_message = owner_message

    def mine(self, contracts):
        previous_block_hash = self.blockchain.peak().get_hash()
        block = Block(
            previous_block_hash=previous_block_hash,
            contracts=contracts,
            miner_public_key=self.owner_public_key,
            miner_message=self.owner_message
        )
        self.blockchain.insert_block(block)
        self.mempool.clean_pool()
