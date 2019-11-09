import json

from Blockchain.Blockchain import get_blockchain
from Miner import Miner
from Wallet import Wallet
from helpers import crypto, hashing

if __name__ == '__main__':

    # blocks = get_blockchain().load_blockchain()
    #
    # for block in blocks:
    #     print(json.loads(block))
    #
    # exit()
    password = crypto.generate_password()
    private_key = crypto.generate_private_pem_string(password=password)
    public_key = crypto.generate_public_pem_string(private_pem_string=private_key, password=password)

    miner = Miner(owner_public_key=public_key, owner_message='Mined by the Miner')
    miner.start()

    wallets = []
    for i in range(10):
        wallets.append(Wallet(str(i)))
        msg="WALLET: {0} deposited 100 fiat currency".format(hashing.hash(wallets[i].public_key))
        wallets[i].issue(100, msg=msg)

    for i in range(10):
        print('ISSUE_TEST: WALLET {0}: {1} HAS BALANCE = {2}'.format(i,hashing.hash(wallets[i].public_key), get_blockchain().get_pk_balance(wallets[i].public_key)))
    print('--- TOTAL BLOCKCHAIN BALANCE IS = {0} ---'.format(get_blockchain().get_balance()))

    for i in range(0,10,2):
        msg = "WALLET: {0} transferred 25 to {1}".format(hashing.hash(wallets[i].public_key), hashing.hash(wallets[i+1].public_key))
        wallets[i].send(25, wallets[i+1].public_key, msg=msg)

    for i in range(10):
        print('SEND_TEST: WALLET {0}: {1} HAS BALANCE = {2}'.format(i,hashing.hash(wallets[i].public_key), get_blockchain().get_pk_balance(wallets[i].public_key)))
    print('--- TOTAL BLOCKCHAIN BALANCE IS = {0} ---'.format(get_blockchain().get_balance()))

    for i in range(3,8):
        msg = "WALLET: {0} exchanged 50 to fiat currency".format(hashing.hash(wallets[i].public_key))
        wallets[i].redeem(50, msg=msg)

    for i in range(10):
        print('REDEEM_TEST WALLET {0}: {1} HAS BALANCE = {2}'.format(i,hashing.hash(wallets[i].public_key), get_blockchain().get_pk_balance(wallets[i].public_key)))
    print('--- TOTAL BLOCKCHAIN BALANCE IS = {0} ---'.format(get_blockchain().get_balance()))
