# MUDRA Mobile Miner
import time
from consensus.pow.pow_engine import mine_block

def start_mining():
    index = 0
    previous_hash = "0"*64
    timestamp = int(time.time())
    data = "Genesis Block"
    nonce, block_hash = mine_block(index, previous_hash, timestamp, data)
    print(f"Nonce found: {nonce}")
    print(f"Hash: {block_hash}")

if __name__ == "__main__":
    start_mining()
