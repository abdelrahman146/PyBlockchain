

from Miner import Miner
from Wallet import Wallet
from helpers import crypto, hashing



if __name__ == '__main__':
    password1 = crypto.generate_password()
    private_key1 = crypto.generate_private_pem_string(password=password1)
    public_key1 = crypto.generate_public_pem_string(private_pem_string=private_key1, password=password1)
    wallet = Wallet()
    wallet2 = Wallet()
    miner = Miner(owner_public_key=public_key1, owner_message=' Mined by me')
    miner.start()
    wallet.issue(100, msg='I have deposited 100')
    wallet2.issue(75, msg='I have deposited 75')
    wallet.send(50, wallet2.public_key, 'this is a gift')
    wallet2.send(75, wallet.public_key, 'this is a better gift')
    print(wallet.get_balance())
    print(wallet2.get_balance())
    # print(wallet.get_balance()


