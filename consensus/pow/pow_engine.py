# MUDRA Proof of Work Engine (Python)
import hashlib
import time

DIFFICULTY_BITS = 20

def mine_block(index, previous_hash, timestamp, data, nonce_start=0):
    nonce = nonce_start
    target = 2 ** (256 - DIFFICULTY_BITS)
    while True:
        block_header = f"{index}{previous_hash}{timestamp}{data}{nonce}".encode()
        hash_result = hashlib.sha256(block_header).hexdigest()
        if int(hash_result, 16) < target:
            return nonce, hash_result
        nonce += 1
