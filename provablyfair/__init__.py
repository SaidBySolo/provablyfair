from typing import Tuple
from secrets import token_hex
from hashlib import sha256
from hmac import new


def generate_server_seed() -> Tuple[str, str]:
    server_seed = token_hex(20)
    server_seed_hash_object = sha256(server_seed.encode())
    server_seed_hash = server_seed_hash_object.hexdigest()
    return server_seed, server_seed_hash


def hash_server_seed(server_seed: str):
    server_seed_hash_object = sha256(server_seed.encode())
    server_seed_hash = server_seed_hash_object.hexdigest()
    return server_seed, server_seed_hash


def roll(server_seed: str, client_seed: str, nonce: int = 0):
    hmac_object = new(
        server_seed.encode(),
        f"{client_seed}-{nonce}".encode(),
        sha256,
    )
    hmac_hash = hmac_object.hexdigest()

    count = 0

    while True:
        roll_number_str = hmac_hash[count : count + 5]
        roll_number = int(roll_number_str, 16)
        if roll_number > 999_999:
            count += 5
        else:
            break

    return roll_number
