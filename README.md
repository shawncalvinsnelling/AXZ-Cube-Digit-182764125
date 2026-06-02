# AXZ Cube Digit No-Division Ordered Arithmetic Gap

This repository is a finite exact computational proof for the ordered digit sequence:

```text
1 8 2 7 6 4 1 2 5
```

Source note: Cube-derived digit string from the cube blocks 1^3, 2^3, 3^3, 4^3, 5^3 = 1, 8, 27, 64, 125, flattened into `182764125`.

The exponent notation in the source note identifies how the digit string was chosen. Powers are **not** an allowed operation in the verifier.

## Theorem

Under the stated rules, every positive integer from 1 through **4771** is representable, and the first missing positive integer is:

```text
4772
```

## Rules

- Digit sequence: `1 8 2 7 6 4 1 2 5`.
- Each digit position is used exactly once.
- Digits must remain in order.
- Concatenation is allowed.
- Allowed operations: `+`, `-`, `*`.
- Parentheses are allowed through all ordered binary expression trees.
- Subtraction is directional: left subtree minus right subtree only.
- Division, powers, factorials, square roots, decimals, logs, hidden constants, and digit reordering are forbidden.
- The exponent notation in the source note is historical notation only; powers are not an allowed operation in the verifier.

## Dynamic-programming recurrence

Let `D = 182764125`.

For each interval `D[i:j]`, define `V(i,j)` as the set that starts with the concatenation leaf `int(D[i:j])`, then combines all left/right split values using the allowed operators.

The full universe is `V(0,9)`.

## Certificate

```text
Possible cut patterns: 256
Unique integer values generated: 99,389
Positive integer values generated: 53,598
Non-positive integer values generated: 45,791
Negative integer values generated: 45,790
Zero present: true
Consecutive positive integers from 1: 4,771
First missing positive integer: 4,772
Minimum integer value: -82,764,124
Maximum integer value: 182,764,125
All-interval unique values generated: 102,815
```

## Boundary witness

```text
4771 = (1+((8+2)*(7+((6+41)*(2*5)))))
```

The integer `4772` is absent from the exact dynamic-programming value set.

## Reproduce locally

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
export PYTHONPATH="$PWD/src"      # Windows PowerShell: $env:PYTHONPATH="$PWD/src"

python scripts/verify_runtime_safety.py
python scripts/verify_challenge_7.py
python scripts/verify_data_hashes.py
python -m pytest -q
```

## Hashes

All-values SHA-256:

```text
b6cf7a413a9ba8bd212a6be91beeb499760ebde789085e06b3c7464ee4dca065
```

Positive-values SHA-256:

```text
c2e849f48da9e3921de23c3dd2a0a19e384bbd4b0702b5a55f8fe05587a97dc5
```

Non-positive-values SHA-256:

```text
1395443d3c9fbe88e2625a0f25b8a52734b95f56b4d80feb3221618e4a83ffbb
```

Negative-values SHA-256:

```text
cff3efe69cac42671b697ba2b4839e055ecd9f6c187648f00ff8fad370ef1924
```

All-interval-values SHA-256:

```text
1fb757597b9d916a2c4d533f0533830c9ace4d7c1d6edb9fbb5719ffcb787b96
```

Witness table SHA-256:

```text
542d5e6c6e0b2d9cd7d5981a1228b5127de693330fd4f4ea6e857ef87a00ca6b
```

## Truth label

```text
CERTIFIED_FINITE_EXACT_INTEGER_RESULT_UNDER_STATED_RULES
```

This repository proves only this finite ordered-expression universe under the exact stated rules.
