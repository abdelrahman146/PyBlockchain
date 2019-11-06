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
from helpers import hashing
from threading import Thread


class Miner(Thread):
    def __init__(self, owner_public_key, owner_message):
        Thread.__init__(self)
        self.mempool = get_mempool()
        self.blockchain = get_blockchain()
        self.owner_public_key = owner_public_key
        self.owner_message = owner_message

    def run(self):
        while True:
            self.mine()

    def mine(self):
        if len(self.mempool.contracts) == 5:
            previous_block_hash = self.blockchain.peak().get_hash()
            block = Block(
                previous_block_hash=previous_block_hash,
                contracts=self.mempool.contracts,
                miner_public_key=hashing.hash(self.owner_public_key),
                miner_message=self.owner_message
            )
            self.blockchain.insert_block(block)
            print("A new Block is successfully added by the miner")
            print(get_blockchain().get_json())
            self.mempool.clean_pool()
