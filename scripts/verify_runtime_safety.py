from __future__ import annotations

def main() -> None:
    a = 2 ** 80
    b = 2 ** 79 + 123456789
    c = a * b + 1
    assert c > 2 ** 128
    assert isinstance(c, int)
    assert c - a * b == 1
    print("PASS: ARBITRARY_PRECISION_RUNTIME_GUARD")

if __name__ == "__main__":
    main()
