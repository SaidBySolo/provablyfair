from dataclasses import asdict, dataclass
from hashlib import sha256, sha512
from hmac import new
from secrets import token_hex
from typing import Any, Dict, Optional, TypedDict


class RolledDataDict(TypedDict):
    roll: int
    nonce: int
    server_seed_hash: str
    client_seed: str


@dataclass
class RolledData:
    roll: int
    nonce: int
    server_seed_hash: str
    client_seed: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, d: RolledDataDict):
        return cls(**d)


def verify_roll(server_seed: str, rolled_data: RolledData):
    instance = ProvablyFair(server_seed)
    return instance.roll(rolled_data.client_seed, rolled_data.nonce) == rolled_data


class ProvablyFair:
    def __init__(self, server_seed: Optional[str] = None) -> None:
        self.server_seed = server_seed or self.generate_server_seed()
        self.server_seed_hash = self.hash_server_seed(self.server_seed)

    def generate_server_seed(self) -> str:
        server_seed = token_hex(32)
        return server_seed

    def hash_server_seed(self, server_seed: str):
        server_seed_hash_object = sha256(server_seed.encode())
        server_seed_hash = server_seed_hash_object.hexdigest()
        return server_seed_hash

    def roll(self, client_seed: str, nonce: int = 0) -> RolledData:
        hmac_object = new(
            self.server_seed.encode(),
            f"{client_seed}-{nonce}".encode(),
            sha512,
        )
        hmac_hash = hmac_object.hexdigest()

        count = 0

        while True:
            roll_number_str = hmac_hash[count : count + 5]
            roll_number = int(roll_number_str, 16)
            if roll_number > 999999:
                count += 5
            else:
                break

        return RolledData(roll_number, nonce, self.server_seed_hash, client_seed)
