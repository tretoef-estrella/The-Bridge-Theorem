# The Open Problem — where the dimension-128 record stands

*An honest, file-backed statement of what Operación Glotón solved, what it did not, and exactly what a future attempt must overcome. Every quantity below is read from the project's exact-arithmetic frame files; nothing is asserted from memory.*

---

## 1. The problem, precisely

Let `Λ = V(4,4)-prim` be the primitive middle-cohomology lattice of the degree-4 Fermat fourfold — positive definite, even, **rank 141**, **determinant 2¹²⁸**. A **section** is a primitive sublattice `S ⊆ Λ` of **rank 128** (codimension 13). Write

- `min(S)` = the squared length of the shortest nonzero vector of `S`;
- `pr(S)` = `det(S) / 2¹²⁸`, the **price**.

These two control the centre density of the resulting 128-dimensional packing through

```
log₂ δ(S) = 64·log₂(min(S)/4) − 64 − ½·log₂ pr(S).
```

> **The King Pin problem.** Does `Λ` contain a rank-128 section `S` with **`min(S) ≥ 24`** and **`pr(S) < 2⁸·⁰⁸`**?

A positive answer gives `δ ≥ 2⁹⁸·⁴⁴`, beating the Mordell–Weil record of Elkies (`δ = 2⁹⁷·⁴⁰`, unbeaten since 2001). **No such section has been exhibited, and none has been ruled out. The problem is open.**

## 2. Two opposing constraints — the "star"

The two conditions pull against each other. The **price** pulls the section together (compactness); the **minimum** pushes its vectors apart (no short vector). A King Pin section is their equilibrium. The two constraints are not two readings of one invariant — they are **two independent demands on one object**, the cut `Φ` whose kernel is `S`:

- the **price** is a `2`-adic quantity (a determinant of the cut against the inverse Gram);
- the **minimum** is an **archimedean** quantity (a shortest-vector condition).

This separation is the content of the [Star Theorem](THE_STAR_THEOREM.md), and it is why the two halves of the problem behave so differently.

## 3. What is solved — the price side

The price side is, for practical purposes, **closed**:

- **The dual integerizes at `2⁵`** and the squared dual-norms of the cheap functionals form a `2`-adic denominator ladder **capped at `2⁴`** — the depth of the Wild Tooth tower at the prime 2. No odd prime can ever appear. The price of a cut is a determinant over that ladder, with a proven floor of `2⁵·⁵⁸⁵`. This is the [Steel Theorem](THE_STEEL_THEOREM.md); the ladder converts the price from a number found by search into a number forced by structure.
- A concrete **rank-13 cut at price `2⁷·⁹⁰⁶⁹`** — comfortably **below the `2⁸·⁰⁸` budget** — has been constructed and verified byte-exact.

So the price is **not** the barrier. A cut of acceptable price exists.

## 4. What is open — the minimum side

The same constructed cuts **do not reach `min(S) ≥ 24`**: short vectors survive inside the section. And the difficulty is structural, not a matter of more search:

> **The minimum is archimedean and irreducible.** It is **not** recoverable from the `2`-adic price data, nor from the representation-theoretic (`S₆ × T`) position of the section. The [Star Theorem](THE_STAR_THEOREM.md) (Remark 5.3′) states this as a limit of the method: two sections with the same spectral fingerprint and the same isotypic position can have **different** minima. The minimum is decided by integer arithmetic *inside* the lattice, and must be certified directly — it cannot be inferred from any of the invariants this work controls.

In short: the price toolkit is complete; the missing piece is a section that simultaneously clears the **archimedean** minimum bar.

## 5. What the supporting theorems do, and do not, settle

The structural theorems in this repository **map** the problem; they do not close it:

- The [Bridge Theorem](THE_BRIDGE_THEOREM.md) makes the minimum a *finite, explicit* enumeration (positive-definiteness bounds the **count** of short vectors, not their length) — it removes an infinite obstruction, leaving a finite one.
- The [Closure Theorem](THE_CLOSURE_THEOREM.md) makes the catalogue of vector "support types" finite and closed — so the section census terminates.
- The [Spectrum Theorem](THE_SPECTRUM_THEOREM.md) gives the exact shape of the intersection form.
- The [Parity Theorem](THE_PARITY_THEOREM.md) closes one entire family of constructions (the section cannot be assembled from plane families; it must be cut).

Each is proven and byte-exact. None of them, alone or together, produces a section meeting `min ≥ 24` at price `< 2⁸·⁰⁸`.

## 6. What a future attempt must overcome

The frontier is sharp:

> **Exhibit a rank-128 primitive `S ⊆ V(4,4)-prim` with `min(S) ≥ 24` and `pr(S) < 2⁸·⁰⁸` — or prove that none exists.**

The price half is in hand. The open half is the **archimedean minimum**: a construction (or an impossibility proof) that controls the shortest vector directly, since no structural invariant in this work determines it. That is the whole of the remaining problem, stated without slack.
