# a blockchain system to create crypto-twin for fiat currencies

This is is a blockchain system that I did code based on my imagination of how blockchain system should work and based on what I have learned from the lectures.

## Description of the system
This blockchain system is basically built to create a digital currency that are coupled with fiat currencies. In other words, the users can issue a digital currencies with an equal amount of a deposited fiat in a consildated money reserve.
currently the system allows the user to issue digital currencies but it doesn't withdraw or deposit any fiat.

## Components and features:
-  SmartContracts: SmartContract is the factory of actions that can be made in the blockchain. I have made three built in SmartContracts but in the future we can add many other contracts:
    - IssueContract: the user can Issue new digital currency and deposit fiat currency in the reserve.
    - RedeemContract: the user can burn some digital currency and withdraw fiat currency in exchange.
    - SendContract: the user can do money transfer to another user.
-   Mempool: is the area where valid contracts are stored before they get indexed in the blockchain. the mempool can accept one smart contract per public key just as a short solution to elemenate double spending.
-   Miner: is the machine that works in the background and whenever the mempool has 5 SmartContracts signed, the Miner creates a new block.
-   Block: is the container that stores the SmartContracts.
-   Blockchain: is the sequence of blocks where the SmartContracts history can be traced.
-   Wallet: is the interface where the user can submit SmartContracts

## The Code:

To test the code, Clone the repo, then run the test.py script.