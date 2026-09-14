"""Verify published survivor arithmetic only; does not prove minimality."""
from pathlib import Path
from math import isqrt
import json

def main() -> None:
    rows = json.loads((Path(__file__).parent / "data/survivors.json").read_text())
    primes = [p for p in range(3, 1000, 2) if all(p % d for d in range(2, isqrt(p) + 1))]
    for row in rows:
        n = int(row["n"])
        if n % 8 != 1 or isqrt(n) ** 2 == n:
            raise ValueError("Invalid nonsquare or residue modulo 8")
        first = next(p for p in primes if pow(n, (p - 1) // 2, p) != 1)
        if first != row["first_failing_prime"] or first <= 379:
            raise ValueError("Quadratic residue check failed")
        print(f"PASS {n}: first failing odd prime {first}")
    print("Candidate arithmetic PASS. Minimality and exhaustive coverage NOT verified by this script.")

if __name__ == "__main__":
    main()
