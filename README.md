# Provably fair

ref: <https://dicesites.com/provably-fair>

## Example

```python
from provablyfair import ProvablyFair

f = ProvablyFair("293d5d2ddd365f54759283a8097ab2640cbe6f8864adc2b1b31e65c14c999f04")
r = f.roll("ClientSeedForDiceSites.com")
print(r.roll % (10000) / 100)
```
