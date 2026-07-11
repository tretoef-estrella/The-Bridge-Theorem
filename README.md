# The Bridge Theorem
### Structural theorems on the Fermat quartic fourfold lattice, from an attempt on the dimension-128 sphere-packing record

This repository collects the theorems proven during **Operación Glotón**, an attempt to beat the densest known sphere packing in dimension 128 — the Mordell–Weil lattice **MW128** of Elkies, unbeaten since 2001 (centre density `δ = 2⁹⁷·⁴⁰`). The attempt works entirely inside one highly symmetric object: `V(4,4)-prim`, the primitive middle-cohomology lattice of the Fermat quartic fourfold `x₀⁴ + ··· + x₅⁴ = 0` — positive definite, even, **rank 141**, **determinant 2¹²⁸**. The target is a rank-128 sublattice dense enough to give `δ ≥ 2⁹⁸·⁴⁴`.

**The record is open.** The work fully controls one half of the problem — the *price*, a `2`-adic quantity understood down to a proven floor — and runs into a precise, identified wall on the other half — the lattice *minimum*, an archimedean condition that no structural invariant determines. That wall is now mapped in closed form: the norm-12 vectors obstructing the minimum are classified, counted, and their symmetric attack routes are sealed with certificates — yet the minimum itself remains archimedean and open. The full accounting is in **[THE_OPEN_PROBLEM.md](THE_OPEN_PROBLEM.md)**.

Independent of the record, what this repository offers is the rigorous structural mathematics the attempt produced: a connected body of theorems about `V(4,4)-prim`, each established in exact integer (or Gaussian-integer) arithmetic on a single 8 GB laptop and independently re-checkable. The keystone is the **Bridge Theorem** — the identity proving that the lattice's arithmetic (Hodge) norm and its geometric intersection form are one and the same. Several of these results are of interest beyond the packing problem.

**New to the subject?** Start with the **[Guide for everyone](GUIDE_FOR_EVERYONE.md)**.

**Author:** Rafael Amichis Luengo · Madrid · [github.com/tretoef-estrella](https://github.com/tretoef-estrella)
**Hardware:** MacBook Air M2 (2022), 8 GB RAM, single thread, throttled to 25% CPU. No swap, no cluster, no cloud. Exact arithmetic throughout.

---

## The object and the problem

Fix the Fermat quartic fourfold `X : x₀⁴ + ··· + x₅⁴ = 0 ⊂ P⁵`. Its `960` linear planes (`15` perfect matchings of six coordinates × `64` phases) span a rank-`142` lattice; the **primitive** part `V(4,4)-prim = ⟨h⟩^⊥` is the rank-`141` sublattice orthogonal to the hyperplane class, even and positive definite with `det = 2¹²⁸`.

A **section** is a primitive `S ⊆ V(4,4)-prim` of **rank 128** (codimension 13). With `min(S)` its squared shortest length and `pr(S) = det(S)/2¹²⁸` its **price**, the centre density obeys `log₂ δ = 64·log₂(min/4) − 64 − ½·log₂ pr`. The problem is whether a section exists with **`min ≥ 24`** and **`pr < 2⁸·⁰⁸`** (which yields `δ ≥ 2⁹⁸·⁴⁴`, beating MW128). The two conditions oppose — price pulls the section together, the minimum pushes its vectors apart — and a record section is their equilibrium. Status: **open** ([THE_OPEN_PROBLEM.md](THE_OPEN_PROBLEM.md)).

---

## The keystone

### [The Bridge Theorem](THE_BRIDGE_THEOREM.md)
Two forms live on the plane lattice: the **geometric** intersection form `Γ` (plane self-intersection `7`; pairwise incidences `+1 / 0 / −2` for planes meeting in a point, disjoint, or sharing a line) and the **Hodge** norm computed from Movasati–Villaflor periods as a sum of eighth roots of unity. The theorem proves they are one form: `G = 4Γ − J` (with `J` the all-ones matrix), hence `‖v‖²_Hodge = (v·v)_geom − N(v)²/4`, coinciding exactly on the primitive sublattice (`N = 0`). As a corollary the minimum is **closed**: positive-definiteness makes the vectors below any bound a finite, explicit set, replacing an infinite eighth-root-of-unity minimisation with finite integer linear algebra. This identity is what makes the whole structural route computable.

---

## The structural theorems

These are the results original to this work, all about `V(4,4)-prim`, all byte-exact.

| Theorem | What it establishes |
|---|---|
| **[The Spectrum Theorem](THE_SPECTRUM_THEOREM.md)** | A complete diagonalisation of the intersection form by `K₆` symmetry: exactly **four** nonzero eigenvalues `16·{15,6,3,2} = {240, 96, 48, 32}`, multiplicities `2·{1,10,15,45}`, governed by the eigenvalue law `λ(a) = 16·N_a` (`N_a` = matchings carrying character `a`). The exact shape of the form, with a structural law for it. |
| **[The Parity Theorem](THE_PARITY_THEOREM.md)** | The span of any set of plane families has **odd** primitive rank — complex conjugation acts on each support with a single fixed point (the impostor `χ* = (2,2,2,2,2,2)`), forcing `rank = 1 + 2·(#conjugate pairs)`. Hence no rank-128 family span exists: the section must be **cut**, not assembled. An entire construction route closed by proof. |
| **[The Star Theorem](THE_STAR_THEOREM.md)** | A two-faced reading of the lattice: every lattice-theoretic invariant is `2`-adic (arithmetic face), while the geometry of its minimal vectors is governed by `S₆` acting on `K₆` (geometric face), the two being independent constraints on the cut. It finitizes the **price** side but proves the **minimum** side archimedean and irreducible (Remark 5.3′) — the open core of the record. |
| **[The Steel Theorem](THE_STEEL_THEOREM.md)** | The dual of `V(4,4)-prim` integerizes at exactly `2⁵`, and its cheap functionals carry a `2`-adic denominator ladder **capped at `2⁴`** (the Wild Tooth tower depth at 2). The price of a cut is a determinant over that ladder, with floor `2⁵·⁵⁸⁵` — read from structure, not stumbled on by search. |
| **[The Closure Theorem](THE_CLOSURE_THEOREM.md)** | The catalogue of chorus **support-types** of lattice vectors is **finite and closed** — no new type is born at any norm, the same finite set across every stratum (rooted in the ten `3+3` bipartitions of `K₆`). This turns an intractable `~10¹⁷·⁵`-node enumeration into finite, type-by-type bookkeeping. |
| **[The Katana Steel Method](THE_KATANA_STEEL_METHOD.md)** | The generation recipe underlying Steel: reduce the scaled integer dual (`32·G⁻¹`) by LLL then BKZ-24 in coordinate form, read short vectors and their pair-combinations, weigh each exact dual-norm. A method (`φ`-free, byte-exact), promoted to structure by the Steel Theorem. |

---

## The lineage it builds on

`V(4,4)-prim`'s determinant `2¹²⁸` and the Steel ladder's `2⁴` cap come from a family of **discriminant theorems** proven in the sister campaign on Fermat **surfaces** ([the Hodge–Fermat campaign](https://github.com/tretoef-estrella)). They are included here, with attribution, because Operación Glotón rests on them; their native home is the surface campaign.

| Theorem | What it establishes (regime) |
|---|---|
| **[The Sweet Lie Theorem](THE_SWEET_LIE_THEOREM.md)** | The rank of any alliance of plane families of `V(4,d)` is a finger-count over `K₆`; telescopes to `rank V(4,d) = DS₄(d)+1`. *(fourfold — the engine the structural theorems above run on.)* |
| **[The Watermark Theorem](THE_WATERMARK_THEOREM.md)** | `|disc| = m^{3(m−3)²}` for the prime-degree Fermat surface line lattice — Shioda's 1987 determinant question, proven for prime degree. *(surface)* |
| **[The Double Ladder Theorem](THE_DOUBLE_LADDER_THEOREM.md)** | The discriminant **group** `(Z/m)^a × (Z/m²)^b` for prime degree — the complete elementary-divisor profile. *(surface)* |
| **[The Bend Theorem](THE_BEND_THEOREM.md)** | The discriminant **shift** at small primes: `b(3)=7`, `b(5)=2`, flat for every prime `≥ 7`, by a power-sum channel criterion. *(surface)* |
| **[The Wild Tooth Theorem](THE_WILD_TOOTH_THEOREM.md)** | The `p = 2` even kingdom — `b(2)=14` (squarefree), `b(2)=−6` (deep towers) — and the universal ledger `b(p) = 36 − corank(σ) − radical`. *(surface; supplies the Steel `2⁴` cap.)* |
| **[The Three-Ring Theorem](THE_THREE_RING_THEOREM.md)** | The composite-degree discriminant group `b_p = (3m−16) + b(p)`, with a proven non-separability of the bend. *(surface)* |

### The map
**[The Orbital Map](THE_ORBITAL_MAP.md)** — how the theorems connect, and which regime (surface `n=2` vs fourfold `n=4`) each one speaks to. Read it to see the whole ecosystem at once and to keep the surface/fourfold scope straight.

---

## Status, in one line

The price side is solved (a cut at price `2⁷·⁹⁰⁶⁹ < 2⁸·⁰⁸` exists, byte-exact); the minimum side (`min ≥ 24`) is archimedean and **open**. The obstruction to the minimum — the norm-12 wall — is now understood as an object: classified in closed form, censused exactly, and its most symmetric attack routes sealed with certificates; the minimum itself nonetheless remains archimedean, decided only by exact computation, not by any structural invariant. Full accounting: **[THE_OPEN_PROBLEM.md](THE_OPEN_PROBLEM.md)**.

## Discipline

- **Numbers from files only.** No quantity is claimed that is not read from an exact-arithmetic frame file.
- **Byte-exact, atom by atom.** Every determinant, every eigenvalue, every dual-norm in exact integer or Gaussian-integer / `flint`-rational arithmetic — no floating point in any load-bearing claim.
- **Proven, and scoped honestly.** Each document states what it proves and what it does not; the record itself is never claimed.
- **Commodity hardware.** A single 8 GB laptop, one thread, throttled, no swap. The constraint is part of the result.

## Repository contents

| File | |
|---|---|
| [`README.md`](README.md) | this overview |
| [`GUIDE_FOR_EVERYONE.md`](GUIDE_FOR_EVERYONE.md) | plain-language introduction |
| [`THE_OPEN_PROBLEM.md`](THE_OPEN_PROBLEM.md) | the honest status of the record |
| [`THE_BRIDGE_THEOREM.md`](THE_BRIDGE_THEOREM.md) | keystone — Hodge norm = geometric form |
| [`THE_SPECTRUM_THEOREM.md`](THE_SPECTRUM_THEOREM.md) | the form, fully diagonalised |
| [`THE_PARITY_THEOREM.md`](THE_PARITY_THEOREM.md) | odd-rank obstruction |
| [`THE_STAR_THEOREM.md`](THE_STAR_THEOREM.md) | the two-faced reading and the open core |
| [`THE_STEEL_THEOREM.md`](THE_STEEL_THEOREM.md) | the dual `2`-adic ladder and the price floor |
| [`THE_CLOSURE_THEOREM.md`](THE_CLOSURE_THEOREM.md) | finite, closed support-type catalogue |
| [`THE_KATANA_STEEL_METHOD.md`](THE_KATANA_STEEL_METHOD.md) | the dual-functional generation method |
| [`THE_SWEET_LIE_THEOREM.md`](THE_SWEET_LIE_THEOREM.md) | the fourfold rank engine *(shared)* |
| [`THE_WATERMARK_THEOREM.md`](THE_WATERMARK_THEOREM.md) | surface discriminant order *(shared)* |
| [`THE_DOUBLE_LADDER_THEOREM.md`](THE_DOUBLE_LADDER_THEOREM.md) | surface discriminant group *(shared)* |
| [`THE_BEND_THEOREM.md`](THE_BEND_THEOREM.md) | small-prime discriminant shift *(shared)* |
| [`THE_WILD_TOOTH_THEOREM.md`](THE_WILD_TOOTH_THEOREM.md) | the `p=2` kingdom *(shared)* |
| [`THE_THREE_RING_THEOREM.md`](THE_THREE_RING_THEOREM.md) | composite-degree group *(shared)* |
| [`THE_ORBITAL_MAP.md`](THE_ORBITAL_MAP.md) | how the theorems connect |
| [`NOMORESQUIRRELS2.py`](NOMORESQUIRRELS2.py) | a verification / search script |

## License

Released under the MIT License (see [`LICENSE`](LICENSE)).

---

## References

1. A. Degtyarev, I. Shimada, *On the topology of projective subspaces in complex Fermat varieties.* J. Math. Soc. Japan **68**:3 (2016), 975–996. arXiv:1405.4683.
2. N. Elkies, *Mordell–Weil lattices in characteristic 2.* (the MW128 record packing.)
3. N. Aoki, T. Shioda, *Generators of the Néron–Severi group of a Fermat surface.* Progress in Mathematics **35**, Birkhäuser (1983), 1–12.
4. H. Movasati, R. Villaflor, *Periods of linear algebraic cycles.* (the period formula behind the Bridge.)
5. T. Shioda, *Some observations on Jacobi sums.* Advanced Studies in Pure Mathematics **12** (1987), 119–135.
