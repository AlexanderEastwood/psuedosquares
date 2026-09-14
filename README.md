# Pseudosquares

**12299505549823064272744801** is the smallest survivor from our completed search. It is a nonsquare, is 1 modulo 8, and is a nonzero quadratic residue at every odd prime through 389. Its first failing prime is 397.

**Independent exhaustive-search review is pending.** This number is a verified upper bound for L379, L383 and L389. Exact equality remains conditional on accepting the GPU enumeration/exclusions and Sorenson’s published L379 > 10^25 bound. The conditional L397 > 2×10^25 bound has the same dependencies. This repository does not assert an independently certified minimum or record priority.

## Documents and data

- [Review certificate (PDF)](docs/certificate.pdf)
- [Styled certificate (HTML; download to view)](docs/certificate.html)
- [Machine-readable draft claims](docs/certificate.json)
- [All five survivors](data/survivors.json)
- [Proposed conditional terms](data/proposed-terms.csv)
- [OEIS submission preparation](oeis-submission.html)

## Verify candidate arithmetic

Python 3.10+, standard library only:

```sh
python3 verify.py
```

This independently checks nonsquareness, congruence modulo 8, and Euler’s criterion at every odd prime up to the first failure for each survivor. It does not rerun the GPU search or prove minimality.

The certificate describes a frozen full review packet whose 7,716,406 serialized batch records passed consistency checks. That operational packet, production sources and full ledgers are retained separately and are **not included in this public repository**. References within the certificate to its bundle verifier and evidence files refer to that separate packet. The public script above checks candidate arithmetic only. Full search reproducibility and independent review require the separate evidence packet.

## OEIS preparation

[A002189](https://oeis.org/A002189) indexes by the number of odd primes tested. The proposed indices 74, 75, 76 correspond to primes 379, 383, 389. Each has verified upper bound 12299505549823064272744801. Do not add these as unconditional b-file terms before the minimum claims are accepted. No OEIS submission has been made.

Prior work: Jonathan P. Sorenson, [Sieving for Pseudosquares and Pseudocubes in Parallel Using Doubly-Focused Enumeration and Wheel Datastructures](https://arxiv.org/abs/1001.3316); D. J. Bernstein, [Doubly focused enumeration](https://cr.yp.to/focus.html).

The repository name `psuedosquares` follows the requested spelling.
