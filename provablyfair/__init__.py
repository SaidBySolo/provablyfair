from secrets import token_hex
from hashlib import sha256
from hmac import new
from typing import Any, Optional, TypedDict
from dataclasses import asdict, dataclass


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

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, d: RolledDataDict):
        return cls(**d)


def verify_roll(server_seed: str, rolled_data: RolledData):
    instance = ProvablyFair(server_seed)
    return instance.roll(rolled_data.client_seed, rolled_data.roll) == rolled_data


class ProvablyFair:
    def __init__(self, server_seed: Optional[str] = None) -> None:
        self.server_seed = server_seed or self.generate_server_seed()
        self.server_seed_hash = self.hash_server_seed(self.server_seed)

    def generate_server_seed(self) -> str:
        server_seed = token_hex(20)
        return server_seed

    def hash_server_seed(self, server_seed: str):
        server_seed_hash_object = sha256(server_seed.encode())
        server_seed_hash = server_seed_hash_object.hexdigest()
        return server_seed_hash

    def roll(self, client_seed: str, nonce: int = 0) -> RolledData:
        hmac_object = new(
            self.server_seed.encode(),
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

        return RolledData(roll_number, nonce, self.server_seed_hash, client_seed)
