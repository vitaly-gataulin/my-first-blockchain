import hashlib
import datetime as date

"""
A simple blockchain, just to understand how does it work/
"""


class Block:
    # Structure of block contains: number of block, time when block was created,
    # data which block contains and hash of previous block.
    # Hash of current block consists of sum all the parameters

    def __init__(self, index, time_stamp, data, previous_hash):
        self.index = index
        self.timestamp = time_stamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        # Find the hash of current block

        sha = hashlib.sha256()
        sha.update((str(self.index) +
                    str(self.timestamp) +
                    str(self.data) +
                    str(self.previous_hash)).encode('utf-8'))
        return sha.hexdigest()

    def __repr__(self):
        #Block representation

        return '\nBlock #{}\nData:\n\t{}\nHash: {}\n'.format(self.index, self.data, self.hash)

def create_genesis_block():
    # Create the genesis block

    return Block(0, date.datetime.now(), "Genesis Block", "0")


def next_block(last_block):
    # Create new block using data from last block

    index = last_block.index + 1
    time_stamp = date.datetime.now()
    data = "I`m block! number - " + str(index)
    previous_hash = last_block.hash
    return Block(index, time_stamp, data, previous_hash)

def blockchain_example(count):
    # Create blockchain with certain number of blocks

    blockchain = [create_genesis_block()]
    for i in range(1, count):
        blockchain.append(next_block(blockchain[i - 1]))
    print(*blockchain)


blockchain_example(30)


