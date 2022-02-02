from typing import Tuple
from secrets import token_hex
from hashlib import sha256


def generate_server_seed() -> Tuple[str, str]:
    server_seed = token_hex(20)
    server_seed_hash_object = sha256(server_seed.encode())
    server_seed_hash = server_seed_hash_object.hexdigest()
    return server_seed, server_seed_hash


def hash_server_seed(server_seed: str):
    server_seed_hash_object = sha256(server_seed.encode())
    server_seed_hash = server_seed_hash_object.hexdigest()
    return server_seed, server_seed_hash
