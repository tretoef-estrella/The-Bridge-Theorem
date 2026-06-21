# King Pin — Cutting the Fermat Fourfold to Beat a 24-Year Sphere-Packing Record

### One rank-128 section of a Fermat cohomology lattice, sought on a single 8 GB laptop, that would beat Elkies' `MW128` — and the exact structure that decides whether it exists

> A psychologist in Madrid — no formal training as a mathematician, working on a thin consumer MacBook Air throttled to a quarter of one thread — set out to beat a record standing since 2001: Elkies' `MW128`, the densest known lattice packing in 128 dimensions, centre density `δ = 2^97.40`. The plan is exact. Take the lattice a prior campaign had spent a year mapping — `V(4,4)-prim`, the primitive cohomology of the Fermat quartic fourfold, rank 141, determinant `2^128`, even — and impose **thirteen linear conditions** so that what remains, a rank-128 section `S`, has no vector shorter than `√24` and stays below a fixed price. If both hold, `δ(S) ≥ 2^98.44` and the record falls by more than a factor of two. The campaign's intellectual arc is a long, disciplined narrowing of *why this is hard*. The answer is now sharp and proven: the problem splits into **two independent forces on one cut**. One force — the **price**, a 2-adic determinant — is solved: a cheap cut exists, well under budget. The other — the **minimum**, an archimedean short-vector condition — is the lock, and three theorems forged here prove it cannot be opened by the algebraic machinery that opens the price. This README is the map of that structure: what is proven, what is borrowed from the surface theory that came before, what is dead with data, and the one open proposition that decides everything.

This is the document a new collaborator — or a mathematician arriving cold — should read first. It states where the record sits, which theorems were forged on the Fermat surfaces and carry over, which were forged here for the record, and the exact open core that remains.

**Architect:** Rafael Amichis Luengo (Madrid) · [tretoef@gmail.com](mailto:tretoef@gmail.com) · [github.com/tretoef-estrella](https://github.com/tretoef-estrella)
**Record targeted:** N. Elkies, `MW128` — a Mordell–Weil lattice, `n = 128`, `δ = 2^97.40`, unbeaten since 2001.
**Lattice substrate:** `V(4,4)-prim`, the primitive part `H⁴_prim(X, ℤ)` of the middle cohomology of the Fermat fourfold `X : x₀⁴ + ⋯ + x₅⁴ = 0 ⊂ ℙ⁵`. The 960 plane classes span a rank-142 lattice (`primitive ⊕ ⟨h⟩`, 818 relations); the primitive part has rank **141**, determinant `det = 2^128`, and is even.
**Hardware:** MacBook Air M2 (2022), 8 GB RAM, single thread, throttled to 25% CPU. No swap, no cluster, no cloud.

---

## At a glance

| | |
|---|---|
| **The record targeted** | `MW128` (Elkies, 2001) — centre density `δ = 2^97.40`, the densest known lattice packing in 128 dimensions, unbeaten for 24 years. |
| **The win condition** | A rank-128 primitive section `S ⊆ V(4,4)-prim` with **minimum `≥ 24`** (equivalently, since the lattice is even, empty in the six norm strata `{12, 14, 16, 18, 20, 22}`) at **price `pr(S) = det(S)/2^128 < 2^8.08`**, giving `δ(S) ≥ 2^98.44` — a factor `2.05` over `MW128`. |
| **The density law** | `log₂ δ(S) = 64·log₂(min(S)/4) − 64 − ½·log₂ pr(S)`. The minimum and the price pull in opposite directions; the record is their equilibrium. |
| **Why exactly 13 conditions** | The section has rank 128 inside the rank-141 lattice: `141 − 128 = 13` is the **codimension**, fixed. A cut of 14 functionals gives rank 127 — the wrong dimension, not the record. |
| **The governing structure — the Star dichotomy (PROVEN)** | Every *lattice-theoretic* invariant of the lattice is supported at the prime 2 (the **arithmetic face**); the geometry of its minimal vectors is governed by `S₆` acting on `K₆` (the **geometric face**). A King Pin section is the **joint feasibility of two independent constraints on one cut `Φ`**: a 2-adic price bound *and* an archimedean minimum bound. The Architect's image is a star — the equilibrium of two opposing forces, not the value of one quantity. See [`THE_STAR_THEOREM.md`](THE_STAR_THEOREM.md). |
| **The price (2-adic) — SOLVED** | The dual integerizes at exactly `2^5` (forced, an isometry invariant); the cheap dual-norm denominators form a 2-adic ladder `{2^0, 2^1, 2^4}`; the price is a determinant of that ladder, so the floor `2^5.585 < 2^8.08` is *read off the ladder*, not stumbled on by search. **The price is below budget.** See [`THE_STEEL_THEOREM.md`](THE_STEEL_THEOREM.md). |
| **The minimum (archimedean) — THE LOCK, open** | The minimum `≥ 24` condition is **not reducible** to 2-adic or representation-theoretic data: two sections with identical 2-adic data and identical isotypic position can have different minima (Star, Remark 5.3′). It is decided by the full integral arithmetic of the section, not its completion. This is the true open core. |
| **The section is irreducibly dual (PROVEN)** | Every span of plane families has **odd** primitive rank (`χ* = (2,2,2,2,2,2)` is the unique self-conjugate character and lies in all 15 supports; supports are conjugation-closed, so `|⋃supports| = 1 + 2·(#pairs)` is odd). Rank 128 is even → **no King Pin section is family-spanned.** The earlier "primal mould" cannot exist; the winning section is the kernel of a dual cut, not a primal span. See [`THE_PARITY_THEOREM.md`](THE_PARITY_THEOREM.md). |
| **The form is completely diagonalised (PROVEN)** | The intersection form on the plane span has exactly **four** nonzero eigenvalues `λ(a) = 16·N_a`, namely `{32, 48, 96, 240}` with multiplicities `{90, 30, 20, 1}` (the `K₆` character types `1²2²3²`, `1·2⁴·3`, `1³3³`, `2⁶`). Realisation holds iff `#{aᵢ=1} = #{aᵢ=3}`. See [`THE_SPECTRUM_THEOREM.md`](THE_SPECTRUM_THEOREM.md). |
| **The forced dark room (PROVEN)** | By the Grassmann dimension count, every rank-128 section meets the eigenspaces in dimensions `≥ (77, 17, 7, 0)` for `(E₃₂, E₄₈, E₉₆, E₂₄₀)`. The `E₂₄₀` overlap is forced to **0**: the impostor `χ*` is expelled from every section, so all vectors outside the `E₂₄₀`-vanishing locus are killed **for free**. Every short-vector survivor lives in one forced corner — the `e240 = 0` "dark room" (Star, Proposition 4.2). |
| **The winning cut must be asymmetric** | Codimension 13 is odd; the conjugation involution `M_σ` (verified byte-exact as an integral isometry) splits the lattice into `+1` (dim 70) and `−1` (dim 71), and `χ*` lives in the odd part. No conjugation-symmetric cut of odd codimension exists, so any winning cut must break the symmetry of the lattice — it is structurally *detuned*. |
| **What is measured and standing** | The four-eigenvalue spectrum and the forced overlaps (byte-exact). The price floor `2^5.585 < 2^8.08` (Steel). The chorus-support catalogue, finite and closed (Closure). The metric identity `G = 4Γ − J` — the dual Hodge norm equals the primal intersection form, making the minimum a finite, decidable quantity (Bridge Identity). The backbone proven in the rank-20 miniature `V(4,3)-prim`, two primes. |
| **What is dead, with data** | The primal mould (dead by Parity). Covering the short vectors with local detectors (a `1 − 0.7⁶ = 11.76%` leak, dead by exact theorem). Par-character covering of the six strata (`14 > 13`, dead by codimension). Direct Fincke–Pohst on the full rank-141 lattice (`~10^{17.5}` nodes, method-blocked). A symmetric (`χ*`-twist / association-scheme / automorphism-magnet) handle on the minimum (dead by *type* — symmetric machinery is blind to an asymmetric winner). The cheap directed search is jammed at an exact, steep frontier (below). |
| **The open core** | **Proposition 5.4 (Star):** is there an integral corank-13 section whose 2-adic price stays within budget *while* the induced form carries minimum `≥ 24`? The price half is finitizable; the minimum half is archimedean and not finitized by those means. Proving it affirmatively exhibits a record; the lattice is not sealed (`γ = 11.49`, only 49% of the Hermite ceiling `16.77`), so room remains — but the construction is a genuinely new object, not a search the current machinery can finish. |

---

## What this is

Sphere packing asks a question a child can state and a specialist can spend a career on: how densely can identical balls fill space? In low dimensions the answer is known and beautiful; in high dimensions it is mostly open, and the best constructions are **lattices** — perfectly periodic arrangements whose density is captured by a single number, the centre density `δ`. In dimension 128 the densest lattice known is Elkies' `MW128`, built in 2001 from a Mordell–Weil lattice in characteristic 2, with `δ = 2^97.40`. No one has beaten it in 24 years.

This campaign attacks that record from an unexpected direction: the cohomology of a Fermat variety. The lattice `V(4,4)-prim` — the primitive part of the plane lattice of the Fermat quartic fourfold — has rank 141, determinant `2^128`, and is even. Impose 13 linear conditions (a **cut**: a list of 13 integral dual functionals) and what survives is a rank-128 **section** whose density you can compute. The centre density of such a section, `δ = (min/4)^{64}/√det`, rewards a **large minimum** and a **small determinant** at once, and the two fight: to beat `MW128` the section needs minimum `≥ 24` while its cut stays cheap — precisely, price `< 2^8.08`. Because the lattice is even, "minimum `≥ 24`" is exactly "the section contains no vector of norm 12, 14, 16, 18, 20, or 22" — six forbidden shells, all of which must be empty.

The deep difficulty is not the price — a cheap cut was found early and proven cheap by structure — but the **emptiness**: certifying that a concrete section has no short vector, in a 141-dimensional lattice whose direct enumeration to norm `≤ 22` costs on the order of `10^{17.5}` tree nodes, astronomically out of reach on any hardware, let alone 8 GB. The campaign's entire arc is the search for a way to certify emptiness **by structure** rather than enumeration — the way Elkies himself certified his minimum through the height theory of his lattice instead of by counting vectors. That search produced three new theorems, retired a whole family of dead approaches by proof, and reduced the record to one sharply stated open proposition.

Every number in this repository comes from a run log or a frame file. Nothing is from memory; nothing is rounded to flatter; and where a result is inherited from the surface theory that came before, it is named as inheritance, not as discovery. Where a verdict was wrong, it is corrected in place, with the object that broke it.

---

## The governing structure — the Star dichotomy

The campaign's central theorem is a **dichotomy** that organises everything else. The lattice `Λ = V(4,4)-prim` has two faces, and they are not separate theories but two readings of one object:

- **The arithmetic face is 2-adic.** The determinant `2^128`, the dual ladder, the Jordan scales, the section rank — every lattice-theoretic invariant is a power of 2, with no odd prime (Star, Theorem 2.1). This is the home of the **price**.
- **The geometric face is `S₆`-combinatorial.** The covariance of the minimal vectors is block-scalar on four `S₆`-isotypic blocks of dimensions `(90, 30, 20, 1)`, and its eigenvalues carry the odd primes `3, 5, 7` of `K₆` (Star, Theorem 3.2). This is the home of the **minimum**.

A cut `Φ ∈ ℤ^{13×141}` is read by both faces through **two different invariants**:

> **Price** `pr(S) = det(Φ D Φᵀ) / 32^{13}` with `D = 32 G⁻¹` — a function of `Φ`, supported at 2, **bounded below budget** (`2^5.585`, Steel).
>
> **Forced minimum energy** — a *constant*, independent of `Φ`: every rank-128 section retains a fixed quantity of covariance energy against the short vectors, because its kernel must overlap the high-eigenvalue blocks in dimensions `≥ (77, 17, 7, 0)`.

These are **not the same invariant** — a constant cannot equal a `Φ`-dependent determinant — and **nothing proven forces them compatible or incompatible.** The two faces are two independent constraints on one cut: `Φ` must keep its price below budget *and* position its kernel so the forced overlap does not produce a vector of norm `< 24`. A King Pin section is the **joint feasibility** of the two. This is the Architect's star read correctly — the equilibrium of two opposing forces, not the value of one.

**Why this is the right frame.** The campaign once pictured the missing piece as a *bridge* translating a primal geometric "mould" into a dual cut. The **Parity Theorem** then proved no such mould exists: every span of plane families has odd rank, so a rank-128 section is irreducibly dual. That did not weaken the problem — it sharpened it to its true core. The bridge was never a missing transfer between two theories; it is the still-open question of whether the two constraints on one cut are jointly satisfiable. That question is **Proposition 5.4**, and its hard half is the **archimedean minimum**, exactly where the campaign's evidence has always placed the lock.

---

## The two lineages — where the theorems came from

Keeping these straight is what keeps the campaign honest. The structure is built from theorems of **two different origins**.

### Lineage I — born on the surfaces of Fermat, and carried here

Before King Pin there was a different campaign: verifying the **Integral Hodge Conjecture** for high-dimensional Fermat varieties via the Degtyarev–Shimada criterion, on the same laptop. It produced theorems about the discriminants and ranks of Fermat lattices — forged for the conjecture, not for sphere packing — that turn out to be exactly the structural facts this record needs, because both problems live on the same Fermat cohomology.

- **The Sweet Lie Theorem** — the resonant alliances of the 15 plane families are the subsets of the ten bipartite hexads of `K₆`, and they generate exactly rank 128. *Here: the rank quantizer.* (It is precisely this theorem, combined with the conjugation parity, that the Parity Theorem turns against the primal mould.) See [`THE_SWEET_LIE_THEOREM.md`](THE_SWEET_LIE_THEOREM.md).
- **The Watermark Theorem** — the discriminant `|disc NS(S_m)| = m^{3(m−3)²}`, proven for prime degree (answering Shioda's 1987 question). *Here: the price machinery.* See [`THE_WATERMARK_THEOREM.md`](THE_WATERMARK_THEOREM.md).
- **The Double Ladder Theorem** — the discriminant *group* structure, `(ℤ/m)^{…} × (ℤ/m²)^{…}`. *Here: the 2-adic group behind the price.* See [`THE_DOUBLE_LADDER_THEOREM.md`](THE_DOUBLE_LADDER_THEOREM.md).
- **The Bend Theorem** — a power sum over a finite field opens a pairing channel at `p` exactly when `p − 1` divides the channel exponent, so only `2, 3, 5` bend the law. *Here: which primes matter.* See [`THE_BEND_THEOREM.md`](THE_BEND_THEOREM.md).
- **The Wild Tooth Theorem** — over `F₂` every channel opens and the calculus folds (`t² ≡ t`); the deep 2-tower lives at depth mod 4 — the cap on the Steel ladder. See [`THE_WILD_TOOTH_THEOREM.md`](THE_WILD_TOOTH_THEOREM.md).
- **The Three-Ring Theorem** — the composite discriminant group, with a proof that the bend is **non-separable** from the primitive heart: the cut is integral, not severable. See [`THE_THREE_RING_THEOREM.md`](THE_THREE_RING_THEOREM.md).

A sealed régime caveat travels with these: five of them (Watermark, Double Ladder, Bend, Wild Tooth, Three-Ring) are **surface theorems** (`n = 2`); reaching the fourfold core (`n = 4`) requires a gluing bridge that is itself unproven. Only **Sweet Lie**, the **Within-Pair Functor**, and the **Closed Walk Law** are fourfold-native. The map of which theorem lives where is [`THE_ORBITAL_MAP_v1.md`](THE_ORBITAL_MAP_v1.md) — mandatory reading before any theorem is invoked in the fourfold régime.

### Lineage II — born here, for the record

Five theorems were forged inside the King Pin campaign. Three map the structure; two prove the cut machinery.

- **The Spectrum Theorem** *(14 June 2026)* — the complete, byte-exact diagonalisation: four eigenvalues `λ = 16·N_a ∈ {32, 48, 96, 240}`, multiplicities `{90, 30, 20, 1}`, with the exact realisation law `#1 = #3`. The scaffold every equivariant cut stands on. See [`THE_SPECTRUM_THEOREM.md`](THE_SPECTRUM_THEOREM.md).
- **The Parity Theorem** *(14 June 2026)* — the conjugation-parity obstruction: every family-span has odd rank, so the rank-128 section is never family-spanned. It closes the primal-mould route with a one-line invariant and proves the section is irreducibly dual. See [`THE_PARITY_THEOREM.md`](THE_PARITY_THEOREM.md).
- **The Closure Theorem** *(11 June 2026)* — the chorus-support-type catalogue is finite and closed: no new support type is born at any norm, turning the census from a `10^{17.5}`-node enumeration into finite bookkeeping. See [`THE_CLOSURE_THEOREM.md`](THE_CLOSURE_THEOREM.md).
- **The Steel Theorem** *(12 June 2026)* — the dual integerizes at `2^5` (forced), the cheap dual-norms form a 2-adic ladder capped at the Wild Tooth depth `2^4`, and the price is a determinant of that ladder, so the floor `2^5.585` is structural. A clean corollary: no dual-norm carries an odd denominator. See [`THE_STEEL_THEOREM.md`](THE_STEEL_THEOREM.md).
- **The Bridge Identity** *(14 June 2026)* — `G = 4Γ − J`: on the primitive lattice the dual Hodge norm equals the primal geometric intersection form, so the minimum is a finite, decidable quantity (algebra equals geometry, on the metric). A genuine tool toward the record, not the record: it certifies that, once a cut is named, its minimum is decidable by structure rather than by enumeration. See [`THE_BRIDGE_THEOREM_PAPER.md`](THE_BRIDGE_THEOREM_PAPER.md).

The **Star Theorem** *(16 June 2026)* unifies the five: it proves the two-faced dichotomy, the block-scalar covariance, and the forced-overlap lemma, and it isolates the single open proposition (5.4) that would close the problem — while stating honestly that the criterion finitizes the *price* and **not** the *minimum*. See [`THE_STAR_THEOREM.md`](THE_STAR_THEOREM.md).

The honest line between the lineages: **King Pin did not re-prove the surface theorems — it discovered they were load-bearing for a problem they were never written for, and it forged the five new spans (Spectrum, Parity, Closure, Steel, the Bridge Identity, unified by the Star) the record needs and the surfaces never required.**

---

## The anatomy of the wall

The structure above turns the abstract obstacle into a sharply located one.

**1. One forced corner.** Every rank-128 section expels the impostor `χ*` (Star, Prop 4.2: the `E₂₄₀` overlap is forced to 0). The expulsion is a *free* knife: the dual functional detecting `E₂₄₀ ≠ 0` is in every cut, and it kills every short vector outside the `E₂₄₀`-vanishing locus at no cost to the price. The consequence is geometrically decisive: **all short-vector survivors live in a single forced corner**, the `e240 = 0` locus. Among the `143,520` norm-12 minimal vectors, `28,800` carry `E₂₄₀ ≠ 0` (killed free) and `114,720` live in the corner. The remaining problem is entirely inside that corner.

**2. The wall is symmetric; the key is not.** The forced corner is invariant under the conjugation involution `M_σ`. So the residual obstacle is *symmetric* — and by the Parity Theorem, any winning cut must be *asymmetric* (codimension 13 is odd; no symmetric odd-codimension cut exists). This is why every symmetric instrument the campaign built — covering designs, the squirrel association scheme, the automorphism magnet — confirms the wall but cannot open it: symmetric machinery describing a symmetric object is structurally blind to the asymmetric winner.

**3. The frontier is measured, exact, and steep.** A directed search engine, with an exact GMP-rational price oracle, maps the price↔survivor frontier byte-exact:

| survivors (norm-12) | price |
|---|---|
| `56,352` | `2^5.585` (the cheap floor) |
| `14,240` | `2^7.907` (the best cut found — jammed `0.17` bits under budget) |
| `~13,400` | `2^8.322` (just over budget) |
| `1,158` | `2^18.764` |
| `0` | `2^137` |

The frontier is nearly vertical at the floor and the zero-survivor regime sits far above budget. This is **data that the zero-survivor section is outside the reachable cheap frontier — not a proof that none exists.** The cheapest survivor-reducing move from the best cut, across every move class tested, costs `2^8.322` — `0.24` bits over budget — confirmed from independent faces. The cheap directed route is mapped to its wall.

**4. The covering route is exhausted.** Covering every `e240 = 0` short vector within the price budget would require on the order of `20` functionals, not 13; the covering price floor is `2^25.76`. The covering family is closed with data across roughly two dozen independent angles.

What remains live is a **construction**, not a search: build the 13 asymmetric functionals directly as a separator of the forced corner (a native Sidon / asymmetric-separator object over the `e240 = 0` locus), pencil-first. The lattice is not sealed — `γ = 11.49`, only 49% of the Hermite ceiling `16.77`, so the room exists — but the object is genuinely new, in the spirit of an extremal-lattice construction rather than a finite search the present machinery can complete.

---

## Where the campaign stands — the minute of the match

- ✓ **The substrate** — `V(4,4)-prim`, rank 141, `det 2^128`, even; measured byte-exact (primitive 141, span 142, 818 relations).
- ✓ **Spectrum** — proven; four eigenvalues `{32, 48, 96, 240}`, multiplicities `{90, 30, 20, 1}`, law `λ = 16·N_a`.
- ✓ **Parity** — proven; the section is irreducibly dual (no family-span is rank 128).
- ✓ **Forced dark room** — proven; every section expels `χ*`, all survivors live in the `e240 = 0` corner.
- ✓ **Price (Steel)** — proven and **below budget**; floor `2^5.585 < 2^8.08`, a ladder determinant.
- ✓ **Closure** — proven; the chorus-support catalogue is finite and closed.
- ✓ **Bridge Identity** — proven; `G = 4Γ − J`, the minimum is finite and decidable.
- ✓ **Miniature backbone** — proven at rank 20 (`V(4,3)-prim`), two primes.
- ✓ **The frontier** — mapped exact (best cut `14,240` survivors at `2^7.907`); the cheap directed route is at its wall.
- ✗ **Symmetric handles on the minimum** (`χ*`-twist, Delsarte/association-scheme LP, automorphism magnet) — dead by type.
- ✗ **The cheap directed search to zero survivors** — outside the reachable frontier with data; the construction must be asymmetric.
- ✗ **Proposition 5.4 (the joint feasibility)** — **open.** The price half is solved; the archimedean minimum is the lock. This is the front.

The live work, in order: (1) construct the asymmetric separator of the forced corner directly (pencil-first), and certify its minimum with the production microscope (lattice reduction, engine `pitbullmarinero`) and its price with the exact oracle (engine `puerta2`) — both figures, or nothing; (2) in parallel, run the **MW128-embedding test** (below), the one route that imports a known minimum rather than searching for one.

### The one route that sidesteps the lock — and an honest accounting of it

The archimedean obstruction dissolves for exactly one candidate: `MW128` itself. If `MW128` embeds primitively as a rank-128 section of `Λ`, its minimum is **imported**, not searched, and the geometric constraint is settled by the embedding. The test is purely arithmetic (compare the discriminant form of `MW128` against `q_Λ` on `Λ*/Λ` via Nikulin's primitive-embedding criterion) and lives entirely on the arithmetic face.

Two cautions, stated plainly, because they matter for any reader who picks up this route:

- **It would tie, not beat, at `MW128`'s own minimum.** `MW128` has minimum `22` in its natural normalisation; embedding it realises the dimension-128 record *inside the primitive cohomology of the Fermat quartic* — a result in its own right — but reproduces `δ = 2^97.40` exactly, a tie. The value `24` enters only in the rescaled-to-tie normalisation, where the price sits at exactly `2^8.08` — the tie boundary, not a strict improvement. A strict beat still requires a section that improves on `MW128`, which returns to the open minimum.
- **It needs one datum not in the project files.** `MW128` is defined implicitly as the Mordell–Weil lattice of an elliptic curve over a function field in characteristic 2; no explicit `128×128` Gram is published. Reconstructing it is a research-grade computation over function fields, and it is the gating step for this route.

Realising `MW128` as an explicit section of `V(4,4)-prim` would nonetheless be a genuine result — the Fermat quartic realising the dimension-128 record in its cohomology — and the explicit tie structure is the most promising place to look for the `ε` that would push strictly below the record line.

---

## Dead veins — documented, not hidden (do not re-open)

- **The primal mould** (a rank-128 sublattice spanned by plane families): **dead by the Parity Theorem.** Every family-span has odd rank; 128 is even.
- **Covering the short vectors with local detectors** (the forge / slings / sieve / pool families): **dead by exact theorem** — no six local teeth cover the family, leak `1 − 0.7⁶ = 11.76%`; and within budget, covering the forced corner needs `~20` functionals (price floor `2^25.76`), not 13.
- **Par-character covering of the six strata:** `14 > 13`, dead by codimension (ILP-verified twice).
- **Direct Fincke–Pohst on the full rank-141 lattice:** method-blocked at `~10^{17.5}` nodes.
- **Crossing coordinate frames without translation:** garbage — the same 13 vectors price at `2^{99.13}` (builder frame) and `2^5.585` (saturated frame). The saturated frame is canonical for price; the builder frame is provenance only.
- **The `2^{16.2}` threshold:** a retired mis-count. The real threshold is `2^8.08`.
- **Reading a shell-count timeout as a vector count:** illegitimate — a long `qfminim` grind is tree-bound (basis quality), not count-bound, and says nothing about how many vectors exist.
- **Symmetric handles on the minimum** — the `χ*`-twist (26 integral twists leave the survivor count unchanged), a Delsarte/association-scheme LP (the price is a determinant, not a trace, and the count is already settled), the automorphism magnet (since `G·D = 32·I`, every integral isometry preserves both count and price): **dead by type.** Symmetric machinery is blind to the asymmetric winner.
- **The cheap directed search beyond its frontier:** the best cut is the budget-frontier optimum from five independent faces; the cheapest survivor-reducing move costs `2^8.322`. The directed route is mapped to its wall — the obstacle is the global frontier `det(S) = 2^128 · price`, not a local trap.

---

## Discipline

- **Numbers from files only.** If a number is not in a log or a frame file, it is not claimed.
- **Two primes, every structural verdict.** Cross-prime confirmation is mandatory.
- **Bench before solder.** Every engine reproduces a known gate (the rank-20 kissing number `15,390`; the norm-12 census `143,520`; the cheap-cut price `2^5.585`) before any virgin run is trusted.
- **One canonical frame for price.** All price is measured in the saturated frame `gram_L0sat` (`det 2^128`); the builder frame is provenance only; crossing frames without the translation map is forbidden.
- **Proven, measured, and open are labelled distinctly.** Spectrum, Parity, Closure, Steel, the Bridge Identity, and the Star dichotomy are theorems; the price floor and the frontier are measured; the joint feasibility (Proposition 5.4) is **open** — never conflated.
- **Per-vector data never decides a section.** A spectral or isotypic fingerprint of a vector cannot certify the minimum of a section (Star, Remark 5.3′): the minimum is archimedean, decided by integer arithmetic inside the forced blocks. This rule is enforced on every claim about a section's minimum.
- **Sweep every parity before claiming emptiness.** A norm-12 vector with `±1` coefficients has an even plane-count `k`; covering one parity class is not covering the shell.
- **Dead veins are documented, not buried.** Each is kept in the record with the object that closed it, so no future effort re-opens a closed street.

---

## Why this matters

A sphere-packing record is not a curiosity. The density of the best lattice in a given dimension underwrites error-correcting codes, lattice-based cryptography, numerical integration, and the geometry of high-dimensional data; a record-breaking construction is a reusable object across all of them. `MW128` has stood 24 years; a denser rank-128 lattice would be a genuine advance.

The deeper prize is the method. The campaign turns "is this section empty below `√24`?" — a `10^{17.5}`-node enumeration, hopeless — into a question about *structure*: a 2-adic price that is already solved, an archimedean minimum localised to one forced corner, and a single open proposition that decides the record. If a section beating `MW128` is constructed, it is not a one-off trick; it is a demonstration that the geometry of a cohomology lattice can be cut into a packing bound. The price half of that principle is settled and the structure is mapped to the line; the minimum is the remaining half.

A clear word on scope. This campaign concerns one bounded, exact target: a rank-128 section of `V(4,4)-prim` beating `MW128`. The price is settled below threshold, the spectrum and the forced corner are proven, the chorus-support catalogue is closed, six theorems stand, and the dead routes are proven dead. What remains is the archimedean minimum — the construction of an asymmetric separator of the forced corner — and, sidestepping it, the embedding test that would at least realise the record inside the Fermat quartic. The campaign does not claim the record. It has proven the dichotomy, mapped the wall to the line, and — when a route proved closed — said so, with the object that closed it.

---

## Repository map

**Read first**
- `README.md` — this map.
- [`THE_STAR_THEOREM.md`](THE_STAR_THEOREM.md) — the governing dichotomy: two faces, the joint-feasibility criterion, and the one open proposition. Start here.
- [`THE_ORBITAL_MAP_v1.md`](THE_ORBITAL_MAP_v1.md) — the régime map (`n = 2` surface vs `n = 4` fourfold-native); mandatory before invoking any theorem in the fourfold régime.

**The theorems — Lineage II (forged here)**
- [`THE_SPECTRUM_THEOREM.md`](THE_SPECTRUM_THEOREM.md) — the complete diagonalisation: `{32, 48, 96, 240}`, multiplicities `{90, 30, 20, 1}`, law `λ = 16·N_a`.
- [`THE_PARITY_THEOREM.md`](THE_PARITY_THEOREM.md) — the conjugation-parity obstruction: the section is irreducibly dual.
- [`THE_CLOSURE_THEOREM.md`](THE_CLOSURE_THEOREM.md) — the chorus-support catalogue is finite and closed.
- [`THE_STEEL_THEOREM.md`](THE_STEEL_THEOREM.md) — the dual ladder, the price floor `2^5.585`.
- [`THE_BRIDGE_THEOREM_PAPER.md`](THE_BRIDGE_THEOREM_PAPER.md) — the metric identity `G = 4Γ − J`, geometry = algebra, the closed census.

**The theorems — Lineage I (carried from the surfaces)**
- [`THE_SWEET_LIE_THEOREM.md`](THE_SWEET_LIE_THEOREM.md) — the rank quantizer (the ten choruses).
- [`THE_WATERMARK_THEOREM.md`](THE_WATERMARK_THEOREM.md) · [`THE_DOUBLE_LADDER_THEOREM.md`](THE_DOUBLE_LADDER_THEOREM.md) · [`THE_BEND_THEOREM.md`](THE_BEND_THEOREM.md) · [`THE_WILD_TOOTH_THEOREM.md`](THE_WILD_TOOTH_THEOREM.md) · [`THE_THREE_RING_THEOREM.md`](THE_THREE_RING_THEOREM.md) — the columns.
- [`THE_KATANA_STEEL_METHOD_v1.md`](THE_KATANA_STEEL_METHOD_v1.md) — the forging recipe the Steel Theorem proves.

**Frames, data, engines**
- `gram_L0sat_141_v1.txt` — the saturated frame, canonical for price (`det 2^128`); `dualgram_L0sat_xD.txt` — the dual `D = 32 G⁻¹` (`G·D = 32·I`).
- `katana_cut13_explicit_v1.txt`, `gabrieloak_best_cut_v1.txt` — the cheapest cut and the best cut found (`14,240` survivors at `2^7.907`).
- `squirrels_n141_norm12_v1.txt`, `sets_no_imp_*.txt`, `baseB_141_from_L0sat_v1.txt` — the short-vector and support data.
- `chorus_plane_builder.cpp` — regenerates the 960 planes, the choruses, the `143,520` census and the `K₆` characters; `NOMORESQUIRRELS2.py` — the analysis toolbox.
- `pitbullmarinero.py` — the minimum certifier (the production microscope: lattice reduction + exact `qfminim`); the price oracle certifies any candidate cut byte-exact in the saturated frame.

**Glossary**
- `GLOSARIO_PACHIPACHI.md` — the project glossary.

---

## References

1. N. Elkies, *Mordell–Weil lattices in characteristic 2*, and the `MW128` record configuration.
2. A. Degtyarev, I. Shimada, *On the topology of projective subspaces in complex Fermat varieties.* J. Math. Soc. Japan **68**:3 (2016), 975–996. arXiv:1405.4683.
3. T. Shioda, *The Hodge conjecture for Fermat varieties.* Math. Ann. **245** (1979), 175–184.
4. T. Shioda, *Some observations on Jacobi sums.* Adv. Stud. Pure Math. **12** (1987), 119–135.
5. V. V. Nikulin, *Integral symmetric bilinear forms and some of their applications.* Izv. Akad. Nauk SSSR Ser. Mat. **43** (1979).
6. J. H. Conway, N. J. A. Sloane, *Sphere Packings, Lattices and Groups.* Springer GTM 290.
7. H. Movasati, R. Villaflor, *Periods of linear algebraic cycles* — the character description of the primitive cohomology and the period input behind equation (6) of the Bridge Identity.

*The dichotomy is proven. The price is solved. The wall is mapped to the line, and the minimum is the work.*
