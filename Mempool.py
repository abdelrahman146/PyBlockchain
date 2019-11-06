"""
Project: PyBlockchain
Author: Abdel Rahman Hussein
Email: abdelrahman146@outlook.com
github: http://github.com/abdelrahman146

This class defines a Mempool
"""


class Mempool:

    def __init__(self):
        self.transactions = []

    # insert a new transaction
    def insert_transaction(self, transaction):
        pass  # TODO

    # remove a transaction from a mempool
    def remove_transaction(self, transaction_hash):
        pass  # TODO

    # check transaction is valid
    def is_valid_transaction(self, transaction):
        pass  # TODO
