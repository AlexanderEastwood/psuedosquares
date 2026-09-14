# Pseudosquares

The smallest survivor from our completed search is

$$
N = 12299505549823064272744801.
$$

It is a nonsquare satisfying $N \equiv 1 \pmod{8}$ and

$$
\left(\frac{N}{p}\right)=1
\quad\text{for every odd prime }p\le389.
$$

Here the parentheses denote the Legendre symbol. Its first failing prime is $397$.

**Independent exhaustive-search review is pending.** Candidate arithmetic establishes the upper bounds

$$
L_{379}\le N,\qquad L_{383}\le N,\qquad L_{389}\le N.
$$

Exact equality remains conditional on accepting the GPU enumeration/exclusions and Sorenson’s published bound $L_{379}>10^{25}$. Under those assumptions, the proposed results are

$$
L_{379}=L_{383}=L_{389}=N,
\qquad L_{397}>2\times10^{25}.
$$

This repository does not assert an independently certified minimum or record priority.

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

[A002189](https://oeis.org/A002189) indexes by the number of odd primes tested. The proposed indices $74,75,76$ correspond to primes $379,383,389$. Each has verified upper bound $N$: $a(74)\le N$, $a(75)\le N$, and $a(76)\le N$. Do not add these as unconditional b-file terms before the minimum claims are accepted. No OEIS submission has been made.

Prior work: Jonathan P. Sorenson, [Sieving for Pseudosquares and Pseudocubes in Parallel Using Doubly-Focused Enumeration and Wheel Datastructures](https://arxiv.org/abs/1001.3316); D. J. Bernstein, [Doubly focused enumeration](https://cr.yp.to/focus.html).

The repository name `psuedosquares` follows the requested spelling.
