"""
project: PyBlockchain
author: Abdel Rahman Hussein
email: abdelrahman146@outlook.com
github: http://github.com/abdelrahman146

This class defines the blockchain node
Blockchain node is the peer interface, once it starts the blockchain system starts
the blockchcain node is the API where the nodes communicate and data can be accessed
"""
from Blockchain.Blockchain import get_blockchain
from Mempool import get_mempool
from helpers import crypto


class Node:
    def __init__(self):
        self.private_key = crypto.generate_private_key()
        self.password = crypto.generate_password()
        self.public_key = crypto.generate_public_key(private_key=self.private_key)
        self.blockchain = get_blockchain()
        self.mempool = get_mempool()
