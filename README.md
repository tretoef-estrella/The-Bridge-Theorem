# King Pin — The Bridge Theorem

### Toppling a 24-year sphere-packing record by cutting the Fermat fourfold, on a single 8 GB laptop

> A psychologist in Madrid — no formal training as a mathematician, a thin consumer MacBook Air throttled to a quarter of one thread — set his sights on a record that has stood since 2001: Elkies' `MW128`, the densest known lattice packing in 128 dimensions, center density `δ = 2^97.40`. The plan is audacious and exact. Take the lattice the previous campaign had spent a year mapping — `V(4,4)-prim`, the primitive plane lattice of the Fermat fourfold, rank 141, determinant `2^128` — and **slice it with thirteen cuts** so that what remains, a rank-128 section, has no vector shorter than `√24` and costs less than a fixed price. If both hold, the section's center density clears `2^98.44` and the record falls, more than twice over. The campaign discovered, the hard way, that the obvious route — catch every short vector with a net of cheap detectors — is **dead by an exact theorem**: no six local teeth can ever cover the family, a `1 − 0.7⁶` leak forced by their myopia. What survives is structural. The ten *choruses* of the Sweet Lie Theorem generate exactly rank 128 in the **primal** world of shapes; the record-winning cut lives in the **dual** world of numbers; and the campaign's own steel method proved, in one line, that the dual does **not** inherit the primal's geometry for free. So the whole problem reduced to a single object that does not yet exist: a **bridge** between the two worlds — a theorem translating the primal mold into a dual cut with the minimum it needs. Two of the bridge's pillars are now proven theorems, the deck-beam is laid, and the chasm is named to the line. This is the record of that campaign: what is built, what is borrowed from the surface theory that came before, and exactly what remains to win.

This README is the map any new collaborator should read first. It tells the whole story — where the record sits, which theorems were forged on the surfaces of Fermat and carry over, which were forged here for the record itself, and the one theorem still missing that decides everything.

**Architect:** Rafael Amichis Luengo (Madrid) · [tretoef@gmail.com](mailto:tretoef@gmail.com) · [github.com/tretoef-estrella](https://github.com/tretoef-estrella)
**The record targeted:** N. Elkies, `MW128` — Mordell–Weil lattice, `n = 128`, `δ = 2^97.40`, standing since 2001.
**Lattice substrate:** `V(4,4)-prim`, the primitive plane lattice of the Fermat fourfold `x₀⁴ + ⋯ + x₅⁴ = 0`, rank 141, det `2^128`, even.
**Hardware:** MacBook Air M2 (2022), 8 GB RAM, single thread, throttled to 25% CPU. No swap. No cluster. No cloud.

---

## At a glance

| | |
|---|---|
| **The record targeted** | `MW128` (Elkies, 2001), center density `δ = 2^97.40`, unbeaten for 24 years — the densest known lattice packing in 128 dimensions |
| **The win condition** | A rank-128 section of `V(4,4)-prim` with **minimum norm ≥ 24** (equivalently: empty in the six norm strata `{12,14,16,18,20,22}`, since the lattice is even) at **price `< 2^8.08`** → `δ ≥ 2^98.44 > MW128` (×2.05) |
| **Why exactly 13 cuts** | The record-bearing section is rank 128 of a rank-141 lattice: `141 − 128 = 13` is the **codimension**, fixed. A cut of 14 functionals gives rank 127 — the wrong dimension, not the record. |
| **The price threshold** | `2^{8.08}`, from `δ = 101.44 − ½·log₂(price)`. The earlier `2^{16.2}` was a **mis-count, retired** — a contributor was stood down for ruling the vein dead on it. |
| **The governing metaphor** | **The Bridge.** Two towns across a river: the **Primal** (geometry, the shapes — planes, squirrels, the ten choruses, where the rank-128 *mold* is measured) and the **Dual** (algebra, the numbers — the 13 functionals, the price, the determinant, where the record is won). The cut that wins is built in the Dual; the mold that shapes it lives in the Primal; the theorem that translates one into the other is the **Bridge Theorem** — and it is the one piece still missing. |
| **THE STEEL THEOREM — the dual pillar, PROVEN (here)** | The dual of `V(4,4)-prim` integerizes at exactly `2^5`, with the exponent **forced** (an isometry invariant of the saturated lattice, not a measurement); its cheap functionals carry a `2`-adic denominator ladder capped at `2^4` — the depth of the Wild Tooth tower — and **the price is a determinant of that ladder**, so the floor `2^{5.585}` is *read off the ladder*, not stumbled on by a search. A clean corollary: the mod-3 / mod-5 "wolves" feared on the primal side are **dead at the root in the dual** — `det = 2^128` has no odd factor, so no dual-norm can carry an odd denominator. This promotes the campaign's *Katana Steel method* (a forging recipe) into a theorem; the dual pillar is now a theorem, not a recipe. See [THE_STEEL_THEOREM.md](THE_STEEL_THEOREM.md). |
| **THE CLOSURE THEOREM — the deck-beam, PROVEN (here)** | The catalogue of support types of `V(4,4)-prim` is **finite and closed**: every vector, of any norm and any walk-length, has a chorus-support type drawn from a fixed 11-slot universe (the ten `K₆` bipartitions plus the even-degree impostor), and **no new type is born at any norm**. This converts the King-Pin census from an intractable `~10^{17.5}`-node Fincke–Pohst enumeration into a finite, type-by-type bookkeeping — the premise that, until 11 June 2026, was the unproven tooth of the whole structural route. See [THE_CLOSURE_THEOREM.md](THE_CLOSURE_THEOREM.md). |
| **THE SWEET LIE THEOREM — the primal pillar (carried from the surface campaign)** | For the Fermat fourfold, the resonant alliances of the 15 plane families are exactly the subsets of the **ten bipartite hexads** (the `3+3` splits of `K₆`, each a `K₃,₃`), and these ten **choruses** generate exactly rank 128 in the primal — *the mold of the winning cut.* Forged in the Hodge–Fermat campaign to quantize the fourfold rank; here it is the left pillar of the bridge. See [THE_SWEET_LIE_THEOREM.md](THE_SWEET_LIE_THEOREM.md). |
| **The four reinforcing columns (carried from the surfaces)** | **Watermark** (the discriminant `m^{3(m−3)²}`, the price machinery), **Double Ladder** (the discriminant *group* structure), **Bend** (which small primes — 2, 3, 5 — open a pairing channel), **Wild Tooth** (the even-degree fold; the mod-4 tower whose depth `2^4` *caps the Steel ladder*), **Three-Ring** (non-separability — the cut is integral, not severable). Five theorems of rock from the surface theory, here load-bearing columns of the bridge. |
| **Régime caveat (sealed)** | Five of those columns are **surface results** (`n = 2`); they do not reach the fourfold core (`n = 4`) without a gluing bridge that is itself unproven. Only **Sweet Lie**, the **Within-Pair Functor**, and the **Closed Walk Law** are fourfold-native. See [THE_ORBITAL_MAP_v1.md](THE_ORBITAL_MAP_v1.md). |
| **What is measured and standing** | The ten choruses → rank 128 (primal, byte-exact). The stratum-12 hitting set = **10 ≤ 13** (ILP-exact, gate-verified). The price floor `2^{5.585} < 2^{8.08}`. The closure of types (theorem). The backbone proven in the rank-20 miniature (`V(4,3)-prim`), two primes. |
| **What is dead, with data** | Covering the squirrels with local teeth (the forge / slings / sieve): **dead by exact theorem** — no six local teeth cover, leak `1 − 0.7⁶ = 11.76%`. Par-character covering of the six strata: **14 > 13**, dead by codimension. Direct Fincke–Pohst on the full rank-141 lattice: method-blocked (`~10^{17.5}` nodes). Crossing coordinate frames without translation: garbage (`2^{99.13}` vs `2^{5.585}` on the same 13 vectors). |
| **THE BRIDGE THEOREM — the deck, OPEN (the objective)** | The one theorem still missing, the mother theorem: *the rank-128 chorus mold that Sweet Lie builds in the Primal translates, through the Steel functionals in the Dual, into a 13-functional cut whose section has minimum ≥ 24.* Proven, this **is** King Pin. It is a theorem unifying algebra and geometry — it does not exist today, and building it is the campaign's sole open front. |

---

## What this is

Sphere packing asks a question a child can state and a specialist can spend a career on: how densely can identical balls fill space? In low dimensions the answer is known and beautiful; in high dimensions it is mostly open, and the best constructions are **lattices** — perfectly periodic arrangements whose density is captured by a single number, the center density `δ`. In dimension 128 the densest lattice known is Elkies' `MW128`, built in 2001 from a Mordell–Weil lattice in characteristic 2, with `δ = 2^97.40`. No one has beaten it in 24 years.

This campaign attacks that record from an unexpected direction: the cohomology of a Fermat variety. The lattice `V(4,4)-prim` — the primitive part of the plane lattice of the Fermat fourfold — has rank 141, determinant `2^128`, and is even. Cut it down to a rank-128 **section** by imposing 13 linear conditions (the "cut," a list of 13 dual functionals), and you get a 128-dimensional lattice whose density you can compute. The center density of such a section is `δ = (min/4)^{64}/√det`: it rewards a **large minimum** and a **small determinant** at once, and the two fight each other. To beat `MW128` the section needs minimum norm **≥ 24** while its cut stays cheap — precisely, price `< 2^{8.08}`. Because the lattice is even, "minimum ≥ 24" is the same as "the section contains no vector of norm 12, 14, 16, 18, 20, or 22" — six forbidden shells, all of which must be empty.

The deep difficulty is not the price (a cheap cut was found early) but the **emptiness**: proving a concrete section has no short vector, in a 141-dimensional lattice whose direct enumeration to norm ≤ 22 costs on the order of `10^{17.5}` tree nodes — astronomically out of reach on any hardware, let alone 8 GB. The campaign's entire intellectual arc is the search for a way to certify emptiness **by structure** instead of by enumeration, the way Elkies himself certified his minimum by the height theory of his lattice rather than by counting vectors. That search produced two new theorems, retired a whole family of dead approaches by proof, and reduced the record to a single, sharply stated missing theorem — the **Bridge**.

Every number in this repository comes from a run log or a file. Nothing is from memory; nothing is rounded to flatter; and where a result is inherited from the surface theory that came before, it is named as inheritance, not as discovery.

---

## The two lineages — where the theorems came from

This is the heart of what a new collaborator needs to understand. The bridge is built from theorems of **two different origins**, and keeping them straight is what keeps the campaign honest.

### Lineage I — born on the surfaces of Fermat (the Hodge–Fermat campaign), and carried here

Before King Pin there was a different campaign: verifying the **Integral Hodge Conjecture** for high-dimensional Fermat varieties, using the Degtyarev–Shimada criterion, on the same 8 GB laptop. That campaign — recorded in its own repository — produced a collection of theorems about the discriminants and ranks of Fermat lattices. Several of them turn out to be exactly the structural facts the sphere-packing record needs. They were **not** forged for King Pin; they were forged for the conjecture, and they apply here because both problems live on the same Fermat cohomology.

- **The Sweet Lie Theorem** — the fourfold rank, quantized: the resonant alliances of the plane families are the subsets of the ten bipartite hexads of `K₆`, and the ten choruses generate rank 128. *In the bridge: the left pillar — the primal mold.* Forged to derive `rank V(4,d) = DS₄(d)+1`; here it is the geometry the record's cut must inherit.
- **The Watermark Theorem** — the discriminant `|disc NS(S_m)| = m^{3(m−3)²}`, proven for prime degree (Shioda's 1987 question, answered). *In the bridge: a column — the price machinery.*
- **The Double Ladder Theorem** — the discriminant *group* structure, `(Z/m)^{…} × (Z/m²)^{…}`. *In the bridge: a column — the group structure behind the cut.*
- **The Bend Theorem** — `b(p) = rank_{F_p}(G) − 12(m−3)`; a power sum over a finite field opens a pairing channel at `p` exactly when `p−1` divides the channel exponent, so only 2, 3, 5 bend the law. *In the bridge: a column — which primes matter.*
- **The Wild Tooth Theorem** — the even prime tamed: over `F₂` every channel opens and the calculus folds (`t² ≡ t`); the deep tower of two lives at depth mod 4. *In the bridge: a column — and the source of the cap on the Steel ladder: the dual denominator ladder tops out at `2^4` because that is the tower depth this theorem named.*
- **The Three-Ring Theorem** — the composite discriminant group, and a proof that the bend is **non-separable** from the primitive heart. *In the bridge: a column — the cut is integral, not severable.*

A sealed régime caveat travels with these: five of them (Watermark, Double Ladder, Bend, Wild Tooth, Three-Ring) are **surface theorems** (`n = 2`). They speak natively to the surfaces; reaching the fourfold core (`n = 4`) requires a gluing bridge that is itself unproven. Only Sweet Lie, the Within-Pair Functor, and the Closed Walk Law are fourfold-native. The map of which theorem lives where is [THE_ORBITAL_MAP_v1.md](THE_ORBITAL_MAP_v1.md), and it is mandatory reading before any theorem is invoked in the fourfold régime.

### Lineage II — born here, for the record

Two theorems were forged inside the King-Pin campaign itself, to build the spans the inherited theorems do not cover:

- **The Closure Theorem** *(11 June 2026)* — the deck-beam. It proves the support-type catalogue is finite and closed (no new type at any norm), turning the census from a `10^{17.5}`-node enumeration into finite bookkeeping. Forged in the campaign's dual-instance protocol: the closure question was named as the single unproven tooth of the structural route; the combinatorial half (the ten `K₆` splits, prime-independent) was forged on one side, the crack it left (does the even fold make an eleventh channel?) closed on the other with Sweet Lie §3 and Wild Tooth §1–2. See [THE_CLOSURE_THEOREM.md](THE_CLOSURE_THEOREM.md).
- **The Steel Theorem** *(12 June 2026)* — the right pillar, the dual. It proves the dual integerizes at `2^5` (forced), that the cheap dual-norms form a `2`-adic ladder capped at the Wild Tooth depth `2^4`, and that the price is a determinant of that ladder — so the floor `2^{5.585}` is structural, not a lucky search. It promotes the *Katana Steel method* (a forging recipe with a self-confessed gap — *"the dual functionals carry no proven geometric structure"*) into a theorem on the arithmetic side. See [THE_STEEL_THEOREM.md](THE_STEEL_THEOREM.md).

The honest line between the lineages: **King Pin did not re-prove the surface theorems — it discovered they were load-bearing for a problem they were never written for, and it built the two new spans (Closure, Steel) the record needs and the surfaces never required.**

---

## The bridge — the picture that holds the whole campaign

Earlier maps of this campaign used two metaphors at once — a five-floor climb (where we are) and a tank crashing a wall (how we break through) — and they tangled. The bridge is one picture, and it is exact.

```
   PUEBLO PRIMAL                  THE DECK                  PUEBLO DUAL
   (geometry, shapes)         (Bridge Theorem)           (algebra, numbers)
   ┌──────────────────┐      ╔══════ ?? ══════╗      ┌──────────────────┐
   │ ten choruses     │      ║   MISSING —    ║      │ 13-functional    │
   │  → rank 128      │──────╢  the mother    ╟──────│  cut             │
   │  (the mold) ✓    │      ║   theorem      ║      │ min ≥ 24,        │
   └──────────────────┘      ╚════════════════╝      │ price < 2^8.08   │
        PILLAR: Sweet Lie ✓      DECK-BEAM:           └──────────────────┘
                                  Closure ✓              PILLAR: Steel ✓
   ───────────────────────────────────────────────────────────────────────
   COLUMNS:  Watermark · Double Ladder · Bend · Wild Tooth · Three-Ring · Closed Walk
   ───────────────────────────────────────────────────────────────────────
   THE BANKS (bedrock):  V(4,4)-prim · rank 141 · det 2^128 · the Fermat fourfold lattice
```

- **The two banks** are the lattice itself: `V(4,4)-prim`, rank 141, det `2^128`. Bedrock, measured.
- **The Primal town** holds the geometry: the planes, the squirrels, the ten choruses. Here the *mold* of the winning cut — rank 128 — is measured exactly. Its pillar is **Sweet Lie** (proven).
- **The Dual town** holds the algebra: the 13 functionals, the price, the determinant. Here the record is won. Its pillar is **Steel** (proven).
- **The deck-beam already laid** is **Closure** (proven): the catalogue is finite, so the crossing is a finite check, not an infinite enumeration.
- **The columns** are the six inherited theorems, bracing each side.
- **The deck** — the span that actually crosses from pillar to pillar — is the **Bridge Theorem**, and it does not exist yet. Building it is the objective. The rendered figure is in [THE_BRIDGE_VISUAL.md](THE_BRIDGE_VISUAL.md) (`the_bridge_theorem.svg`).

**The exact question the deck answers:** does the rank-128 chorus mold (Primal) translate into a 13-functional dual cut whose section has minimum ≥ 24? Yes → the Bridge Theorem is written → King Pin falls. No → the chasm is the wall, and it must be crossed another way (which character realizes the mold in the dual).

---

## Where the campaign stands — the minute of the match

- ✓ **The banks** — the lattice, det `2^128`, measured.
- ✓ **Left pillar (Sweet Lie)** — proven; the ten choruses generate rank 128 in the primal.
- ✓ **Right pillar (Steel)** — proven (here); the dual integerizes at `2^5`, ladder capped at `2^4`, price a ladder determinant, floor `2^{5.585} < 2^{8.08}`.
- ✓ **Deck-beam (Closure)** — proven (here); the type catalogue is finite and closed.
- ✓ **Stratum-12** — covered by 10 ≤ 13 slots (ILP-exact). Price floor below threshold.
- ✓ **Miniature backbone** — proven at rank 20 (`V(4,3)-prim`), two primes: minimum-stratum completeness, benign quantum, full support-type table postdicting all strata byte-exact.
- ✗ **Par-character covering of all six strata** — `14 > 13`, dead by codimension (ILP-verified twice).
- ✗ **THE DECK (Bridge Theorem)** — not built. **The sole open front.**

The live work is to **build the Bridge Theorem**, standing on the two proven pillars and the laid deck-beam. Coverage and price are settled; what remains is the span that translates the primal mold into the dual cut.

---

## Dead veins — documented, not hidden (do not re-open)

- **Cover the squirrels with local teeth** (the forge, the slings, the sieve, the W33 pool): **dead by exact theorem.** No six local teeth cover the family — a branch-and-bound proof gives `H_all > 6`, forced by the 1,440 myopia witnesses; the leak is `1 − 0.7⁶ = 11.76%`, the signature of six independent ~30%-bite teeth. Not laziness — geometric impossibility, measured.
- **Par-character cover in 13 slots:** the union of strata 12∪14∪18 needs **14 > 13** (ILP-exact, verified twice). The cut must be 13 (codimension). Dead.
- **Direct Fincke–Pohst on the full rank-141 lattice:** method-blocked at `~10^{17.5}` nodes; the tree is exponentially wide at the top and never descends to a leaf (run log in repository).
- **Cross coordinate frames without translation:** garbage. The same 13 vectors price at `2^{99.13}` in the builder frame and `2^{5.585}` in the saturated frame. The saturated frame is canonical for price; the builder frame is provenance only.
- **The `2^{16.2}` threshold:** a retired mis-count. The real threshold is `2^{8.08}`.
- **mod-3 / mod-5 detectors in the dual:** dead at the root by the Steel Theorem (`det = 2^128` has no odd factor → no odd dual denominator). The wolves are a primal phenomenon, never a dual one.

---

## Discipline

- **Numbers from files only.** If a number is not in a log or a frame file, it is not claimed.
- **Two primes, every structural verdict.** Cross-prime confirmation is mandatory.
- **Bench before solder.** Every engine reproduces a known gate (the rank-20 kissing number, 15,390, byte-exact) before any virgin run is trusted.
- **One canonical frame for price.** All price measured in the saturated frame `gram_L0sat` (det `2^128`); the builder frame is provenance only; crossing frames without the translation map is forbidden.
- **Proven, measured, and open are labelled distinctly.** Closure and Steel are theorems; the ten-chorus rank-128 mold is measured (necessary, not sufficient); the Bridge Theorem is **open** and never conflated with the pillars that would support it.
- **Inheritance is named as inheritance.** The five surface columns are credited to the Hodge–Fermat campaign and carry their régime caveat (`n = 2`, not natively fourfold); only Closure and Steel are claimed as forged here.
- **Dead veins are documented, not buried** — the forge, the par-character route, the FP wall, the frame-crossing trap, the retired threshold, the wolves: all part of the record, so no successor re-walks them.

---

## Why this matters

A sphere-packing record is not a curiosity. The density of the best lattice in a given dimension underwrites error-correcting codes, lattice-based cryptography, numerical integration, and the geometry of high-dimensional data; a record-breaking construction is a reusable object across all of them. `MW128` has stood 24 years; a denser rank-128 lattice would be a genuine advance.

But the deeper prize is the method. If the **Bridge Theorem** can be built — a proof that a primal geometric mold translates into a dual cut with an inherited minimum — it is not a trick that works once for one lattice. It is a general principle for turning the geometry of a cohomology lattice into a packing bound, and it would reach records far beyond this one. That is the impractical-sounding, record-shattering kind of theorem the campaign is built to chase: a span between algebra and geometry that, once laid, carries traffic no one expected.

A clear word on scope. This campaign concerns one bounded, exact target: a rank-128 section of `V(4,4)-prim` beating `MW128`. The price is settled below threshold, the type catalogue is closed, two pillars stand as theorems, and the dead routes are proven dead. What remains is the deck — the Bridge Theorem — and it is open. The campaign does not claim the record; it has built the abutments and named the chasm to the line, and the standard that governs the crossing is the one that produced two theorems forged here, six inherited and correctly attributed, and zero false theorems.

The work continues. Cross the deck, and a record that has stood since 2001 falls.

---

## Repository map

**The bridge, the project, the visual**
- [`KING_PIN_THE_BRIDGE_PROJECT.md`](KING_PIN_THE_BRIDGE_PROJECT.md) — the project description and objectives, with the bridge figure embedded.
- [`THE_BRIDGE_VISUAL.md`](THE_BRIDGE_VISUAL.md) · [`the_bridge_theorem.svg`](the_bridge_theorem.svg) — the bridge, rendered, reproducible byte-exact.

**The theorems — Lineage II (forged here)**
- [`THE_CLOSURE_THEOREM.md`](THE_CLOSURE_THEOREM.md) — the deck-beam: the type catalogue is finite and closed.
- [`THE_STEEL_THEOREM.md`](THE_STEEL_THEOREM.md) — the dual pillar: the dual integerizes at `2^5`, ladder capped at `2^4`, price a ladder determinant.

**The theorems — Lineage I (carried from the surfaces)**
- [`THE_SWEET_LIE_THEOREM.md`](THE_SWEET_LIE_THEOREM.md) — the primal pillar: the ten choruses, the rank-128 mold.
- [`THE_WATERMARK_THEOREM.md`](THE_WATERMARK_THEOREM.md) · [`THE_DOUBLE_LADDER_THEOREM_v2.md`](THE_DOUBLE_LADDER_THEOREM_v2.md) · [`THE_BEND_THEOREM_FINAL.md`](THE_BEND_THEOREM_FINAL.md) · [`THE_WILD_TOOTH_THEOREM.md`](THE_WILD_TOOTH_THEOREM.md) · [`THE_THREE_RING_THEOREM.md`](THE_THREE_RING_THEOREM.md) — the columns.
- [`THE_ORBITAL_MAP_v1.md`](THE_ORBITAL_MAP_v1.md) — the régime map (which theorem is `n=2` surface vs `n=4` fourfold-native); mandatory before invoking any theorem.
- [`THE_KATANA_STEEL_METHOD_v1.md`](THE_KATANA_STEEL_METHOD_v1.md) — the forging recipe the Steel Theorem proves (a method, not a theorem).

**The record, the journals, the map**
- [`EL_DIARIO_DE_GLOTON_v171.md`](EL_DIARIO_DE_GLOTON_v171.md) — the full historical diary (§1–§207).
- `DIARIO_PEPITAS_DE_ORO_v40_INDICE.md` · `DIARIO_PEPITAS_DE_ORO_v40_DETALLE.md` — the distilled living index (read first) and its detail.
- [`THE_FIVE_FLOORS_AND_THE_TANK_v8.md`](THE_FIVE_FLOORS_AND_THE_TANK_v8.md) — the earlier metaphors, kept as history.
- [`GLOSARIO_PACHIPACHI.md`](GLOSARIO_PACHIPACHI.md) — the glossary.

**Frames, steel, data, engines** — the saturated frame `gram_L0sat_141_v1.txt` (canonical for price); the steel and dual files (`katana_steel_origbasis_v1.txt`, `katana_cut13_explicit_v1.txt`, `dualgram_L0sat_xD.txt`); the squirrels and support-set data (`squirrels_n141_norm12_v1.txt`, `sets_no_imp_*.txt`, `baseB_141_from_L0sat_v1.txt`); the engines (`chorus_plane_builder.cpp` — the φ-free bridge that regenerates everything in ~1 s; `census_strata.cpp`, `bench_kissing.cpp`, `tabla_tipos_d4_v2.cpp`, and the toolbox `NOMORESQUIRRELS2.py`).

---

## References

1. N. Elkies, *Mordell–Weil lattices in characteristic 2*, and the `MW128` record configuration (the standing record this campaign targets).
2. A. Degtyarev, I. Shimada, *On the topology of projective subspaces in complex Fermat varieties.* J. Math. Soc. Japan **68**:3 (2016), 975–996. arXiv:1405.4683.
3. T. Shioda, *The Hodge conjecture for Fermat varieties.* Math. Ann. **245** (1979), 175–184.
4. T. Shioda, *Some observations on Jacobi sums.* Advanced Studies in Pure Mathematics **12** (1987), 119–135.
5. J. H. Conway, N. J. A. Sloane, *Sphere Packings, Lattices and Groups.* Springer GTM 290 (the dual-lattice, discriminant-form, and center-density machinery).
6. H. Movasati, R. Villaflor, *Periods of linear algebraic cycles* (the period-quanta input behind the squirrel structure).

*The abutments stand. The chasm is named. The deck is the work. PMC.*
