**Important Note:** The project is still under development!

# Digital-Twin for Fiat Currencies Based on Blockchain Technology

This is a blockchain system that I did code based on my imagination of how blockchain system should work.

## Motivation

Blockchain Technology is a type of Distributed Ledger Technology (DLT) that has vast potential to disrupt various industries. it's just a matter of getting the protocol and infrastructure in place to turn them into a reality.  The Technology unleashes value, Internet is built to exchange information, Blockchain is built to exchange value.  Transparency is the greatest benefit, Blockchain brings a trust-but-verify approach to the transactions made by the system. Moreover, The technology allows immediate and highly secured value transfer without the interference of any 3rd Party. having such solution will boost the productivity, radically reduce transfer and accounting cost, but most importantly, it will enhance the cash flow between the two parties because it allows micropayments-per-service so the money will be transferred continuously not in big bulks. Having that said, The blockchain technology bring us to another level of value exchange, where not only value transfer could occur from a human to another human, but also it allows value exchange between human-to-robot, robot-to-human and even robot-to-robot!. If Blockchain is implemented with other disruptive technologies such as Artificial Intelligence (AI) and Internet of Things (IoT), it will bring a new era of civilization and development to the humanity. 

Even with the important features provided by the blockchain, the current blockchain solutions such as bitcoin and Ethereum are a little bit hard to be adopted by the governments and even the individuals. Taxations, anti-money-laundry, inheritance after death, legalization and regulation, the ownership of the blockchain system,  and even the acceptance of replacing the fiat currency are all challenges that the current blockchain systems cannot solve. in the other hand, for end users and individuals, private keys are very important in the current blockchain systems and losing them, means losing everything in the network. Such big responsibility cannot be handled to individuals, it can be lost, or the individuals lose their memory. In order to adopt blockchain technology, it must be applicable for daily-life actions, such as simple money transfer, buy/sell items, Loans & installments, escrows, mortgage and renting. the system must have instant transactions to co-op with daily life micropayments. 

The proposed idea aims to have a blockchain economy that works in parallel and having the same strong features of the current economy system. The system's currency will be strongly backed by the used fiat currency in area, and can be easily exchanged. The system will have smart contracts that simulates the daily life actions with the ability of making instant transactions. The system must also be compatible with all  the government requirements such as taxations and anti-money-laundry.

## Project Milestones

| **Check** | **Task Description**                                         |
| :-------: | ------------------------------------------------------------ |
|     ✔     | Build the Foundation                                         |
|     ✔     | Build the mechanism of reading from file and memory optimization |
|           | Build the Application Programming Interfaces (Node.py & WalletAPI.py) |
|           | Build the Application user interfaces (Node Interface, Wallet Interface) |
|           | Build the mechanism of instantiating the Node                |
|           | Build the mechanism of fiat deposit and withdrawal using smart contracts |
|           | Build the GraphQL network between the nodes and Build the Bootstrap Server |
|           | Build the feature of creating public key based on fingerprint |
|           | Develop the concept of the smart contract and make new ones  |
|           | Develop the instant transactions feature                     |
|           | Develop a consensus mechanism                                |
|           | Enhance the security of the system                           |
|           | Enhance the performance of the system                        |

## Description of the system
**Important Note:** This part is still under development

This blockchain system is basically built to create a digital currency that are coupled with fiat currencies. In other words, the users can issue a digital currencies with an equal amount of a deposited fiat in a consolidated money reserve.
currently the system allows the user to issue digital currencies but it doesn't withdraw or deposit any fiat.

## Components and features:

**Important Note:** This part is still under development

-  SmartContracts: SmartContract is the factory of actions that can be made in the blockchain. I have made three built in SmartContracts but in the future we can add many other contracts:
    - IssueContract: the user can Issue new digital currency and deposit fiat currency in the reserve.
    - RedeemContract: the user can burn some digital currency and withdraw fiat currency in exchange.
    - SendContract: the user can do money transfer to another user.
-   Mempool: is the area where valid contracts are stored before they get indexed in the blockchain. the mempool can accept one smart contract per public key just as a short solution to eliminate double spending.
-   Miner: is the machine that works in the background and whenever the mempool has 5 SmartContracts signed, the Miner creates a new block.
-   Block: is the container that stores the SmartContracts.
-   Blockchain: is the sequence of blocks where the SmartContracts history can be traced.
-   Wallet: is the interface where the user can submit SmartContracts

## The Code:

To test the code, Clone the repo, then run the test.py script.