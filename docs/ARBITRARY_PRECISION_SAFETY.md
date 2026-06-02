# Arbitrary precision safety

The verifier runs with Python integer arithmetic, which is arbitrary precision subject to memory.

For this final universe:

```text
minimum final value: -82764124
maximum final value: 182764125
maximum absolute final value: 182764125
bit length: 28
```

The package still includes `scripts/verify_runtime_safety.py`, which checks arithmetic above `2^64`.
