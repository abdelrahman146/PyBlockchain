from Miner import Miner
from Wallet import Wallet
from helpers import crypto

if __name__ == '__main__':
    password = crypto.generate_password()
    private_key = crypto.generate_private_pem_string(password=password)
    public_key = crypto.generate_public_pem_string(private_pem_string=private_key, password=password)
    # wallet = Wallet('alice')
    # wallet2 = Wallet('bob')
    miner = Miner(owner_public_key=public_key, owner_message='Mined by the Miner')
    miner.start()
    # wallet.issue(100, msg='I have deposited 100')
    # wallet.redeem(50,msg="redeemed")
    # wallet2.issue(75, msg='I have deposited 75')
    # wallet.send(50, wallet2.public_key, 'this is a gift')
    # wallet2.send(75, wallet.public_key, 'this is a better gift')

    wallets = []

    for i in range(10):
        wallets.append(Wallet(str(i)))
        wallets[i].issue(100, msg="deposited 100 fiat currency")

    for i in range(0,10,2):

        wallets[i].send(25, wallets[i+1].public_key, msg="money transfer to %d" % i)

    for i in range(3,8):
        wallets[i].redeem(50, msg="withdrawn 15 fiat currency")