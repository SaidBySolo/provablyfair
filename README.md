# Provably fair

ref: <https://dicesites.com/provably-fair>

## Install

```sh
pip install provablyfair
```

## Example

### Roll

```python
from provablyfair import ProvablyFair

f = ProvablyFair("293d5d2ddd365f54759283a8097ab2640cbe6f8864adc2b1b31e65c14c999f04")
r = f.roll("ClientSeedForDiceSites.com")
print(r.roll % (10000) / 100)
```

### Verify

```py
from provablyfair import ProvablyFair, verify_roll, RolledData

f = ProvablyFair("293d5d2ddd365f54759283a8097ab2640cbe6f8864adc2b1b31e65c14c999f04")
r = f.roll("ClientSeedForDiceSites.com")
data = RolledData.from_dict()
print(r.roll == RolledData(roll=697969, nonce=0, server_seed_hash='5ac59780d512265230d5efb3cc238886dc1b457a80b54fbf1f920b99c6505801', client_seed='ClientSeedForDiceSites.com'))
``
