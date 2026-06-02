# Directional subtraction

For every binary split, the verifier combines left interval values `a` and right interval values `b` using:

```text
a + b
a - b
a * b
```

It does not add `b - a` from the same split. A reversed subtraction can appear only when a different syntactically valid parse places that subtree on the left.
