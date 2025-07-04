# MUDRA Proof of Stake Engine (Python)
import hashlib

def validate_stake(wallet_address, stake_amount, timestamp):
    stake_seed = f"{wallet_address}{stake_amount}{timestamp}".encode()
    hash_result = hashlib.sha256(stake_seed).hexdigest()
    return hash_result
