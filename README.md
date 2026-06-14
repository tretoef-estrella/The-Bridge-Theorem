# King Pin — The Bridge Theorem

### Toppling a 24-year sphere-packing record by cutting the Fermat fourfold, on a single 8 GB laptop

> A psychologist in Madrid — no formal training as a mathematician, a thin consumer MacBook Air throttled to a quarter of one thread — set his sights on a record that has stood since 2001: Elkies' `MW128`, the densest known lattice packing in 128 dimensions, center density `δ = 2^97.40`. The plan is audacious and exact. Take the lattice the previous campaign had spent a year mapping — `V(4,4)-prim`, the primitive plane lattice of the Fermat fourfold, rank 141, determinant `2^128` — and **slice it with thirteen cuts** so that what remains, a rank-128 section, has no vector shorter than `√24` and costs less than a fixed price. If both hold, the section's center density clears `2^98.44` and the record falls, more than twice over. The campaign discovered, the hard way, that the obvious route — catch every short vector with a net of cheap detectors — is **dead by an exact theorem**: no six local teeth can ever cover the family, a `1 − 0.7⁶` leak forced by their myopia. What survives is structural. The ten *choruses* of the Sweet Lie Theorem generate exactly rank 128 in the **primal** world of shapes; the record-winning cut lives in the **dual** world of numbers; and the campaign's own steel method proved, in one line, that the dual does **not** inherit the primal's geometry for free. So the whole problem reduced to a single object that does not yet exist: a **bridge** between the two worlds — a theorem translating the primal mold into a dual cut with the minimum it needs. Two of the bridge's pillars are now proven theorems, the deck-beam is laid, the metric span across the deck is proven, and the chasm is named to the line. This is the record of that campaign: what is built, what is borrowed from the surface theory that came before, and exactly what remains to win.

This README is the map any new collaborator should read first. It tells the whole story — where the record sits, which theorems were forged on the surfaces of Fermat and carry over, which were forged here for the record itself, and the one theorem still missing that decides everything.

**Architect:** Rafael Amichis Luengo (Madrid) · [tretoef@gmail.com](mailto:tretoef@gmail.com) · [github.com/tretoef-estrella](https://github.com/tretoef-estrella)
**The record targeted:** N. Elkies, `MW128` — Mordell–Weil lattice, `n = 128`, `δ = 2^97.40`, standing since 2001.
**Lattice substrate:** `V(4,4)-prim`, the primitive plane lattice of the Fermat fourfold `x₀⁴ + ⋯ + x₅⁴ = 0`, rank 141 (the 960 planes span rank 142 = primitive ⊕ ⟨h⟩, with 818 relations; the primitive part is 141), det `2^128`, even.
**Hardware:** MacBook Air M2 (2022), 8 GB RAM, single thread, throttled to 25% CPU. No swap. No cluster. No cloud.

---

> ## Status update — 14 June 2026
>
> Since the body of this README was written, two things changed, and both are recorded here in full — nothing flattered, nothing buried.
>
> **First, the metric half of the deck is now a theorem.** The **Bridge Identity** `G = 4Γ − J` proves that on the primitive lattice the dual Hodge norm *is* the primal geometric intersection form (up to the charge term), so on the section the minimum is a finite, computable quantity — algebra equals geometry, on the metric. This is a genuine span across the chasm, and a real tool: it makes "is the section empty below `√24`?" a finite question. It is **not** the record. It does not build the cut; it certifies that, once a cut is named, its minimum is decidable by structure rather than by a `10^{17.5}`-node enumeration.
>
> **Second, a structural probe of the first forbidden shell reopened a front the campaign had marked closed.** The stratum-12 covering — believed sealed by a ten-slot `Z/4` hitting set — was computed over the **point-pair census alone** (the 143,520 squirrels). The norm-12 shell is strictly larger: it contains genuinely new, non-point-pair vectors (a distinct count `≥ 143,521`, established by a fingerprint invariant, not by enumeration). The *six-plane* family among them is still covered — 2,000 sampled, all hit by the ten slots. But a *four-plane* witness, `w = P₀ + P₁ − P₆ − P₇`, norm 12, is invisible to **every one of the 70 `Z/4` pair-characters and every one of the ten choruses** (`max|χ| = 0`, verified independently on two sides). Stratum-12 is therefore **not empty** under that cut. The "covered" verdict is downgraded — honestly, with a named witness — to **reopened**.
>
> This does not move the record further away; it replaces a false floor with a real one, named to the vector. The missing detector is now concrete: a `mod-3 / mod-5` character, exactly the arithmetic the `2^5·3^4·5` factorisation of the chorus-blind wolves had predicted — now required for a four-plane vector, not only the wolves. Whether such a detector can be cheap, and how it reconciles with the Steel Theorem's proof that the *dual price* carries no odd denominator, is the campaign's sharpest open question. **Coverage is no longer "settled"; it is a live, exact front again — and that is progress, because the wall is now a vector you can write down.** Full detail: [`DIARIO_PEPITAS_DE_ORO_v49`](DIARIO_PEPITAS_DE_ORO_v49_INDICE.md), `§SESIÓN-14JUN-PART2`.

---

## At a glance

| | |
|---|---|
| **The record targeted** | `MW128` (Elkies, 2001), center density `δ = 2^97.40`, unbeaten for 24 years — the densest known lattice packing in 128 dimensions |
| **The win condition** | A rank-128 section of `V(4,4)-prim` with **minimum norm ≥ 24** (equivalently: empty in the six norm strata `{12,14,16,18,20,22}`, since the lattice is even) at **price `< 2^8.08`** → `δ ≥ 2^98.44 > MW128` (×2.05) |
| **Why exactly 13 cuts** | The record-bearing section is rank 128 of the rank-141 primitive lattice: `141 − 128 = 13` is the **codimension**, fixed. A cut of 14 functionals gives rank 127 — the wrong dimension, not the record. |
| **The price threshold** | `2^{8.08}`, from `δ = 101.44 − ½·log₂(price)`. The earlier `2^{16.2}` was a **mis-count, retired** — a contributor was stood down for ruling the vein dead on it. |
| **The governing metaphor** | **The Bridge.** Two towns across a river: the **Primal** (geometry, the shapes — planes, squirrels, the ten choruses, where the rank-128 *mold* is measured) and the **Dual** (algebra, the numbers — the 13 functionals, the price, the determinant, where the record is won). The cut that wins is built in the Dual; the mold that shapes it lives in the Primal; the theorem that translates one into the other is the **Bridge Theorem** — and it is the one piece still missing. |
| **THE STEEL THEOREM — the dual pillar, PROVEN (here)** | The dual of `V(4,4)-prim` integerizes at exactly `2^5`, with the exponent **forced** (an isometry invariant of the saturated lattice, not a measurement); its cheap functionals carry a `2`-adic denominator ladder capped at `2^4` — the depth of the Wild Tooth tower — and **the price is a determinant of that ladder**, so the floor `2^{5.585}` is *read off the ladder*, not stumbled on by a search. A clean corollary: no **dual-norm** can carry an odd denominator (`det = 2^128` has no odd factor). *(Note — the wolves and the new witness `w` are a **primal** covering phenomenon; the detector that must see them is a primal character, and reconciling its arithmetic with this dual corollary is now an open question, not a closed door — see the status update.)* See [THE_STEEL_THEOREM.md](THE_STEEL_THEOREM.md). |
| **THE CLOSURE THEOREM — the deck-beam, PROVEN (here)** | The catalogue of **chorus-support types** of `V(4,4)-prim` is **finite and closed**: every vector, of any norm and any walk-length, has a chorus-support type drawn from a fixed 11-slot universe (the ten `K₆` bipartitions plus the even-degree impostor), and **no new type is born at any norm**. This stands — `w` has the *empty* chorus-type, which is already in the universe (the wolves' home). *(What `w` reopens is not the closure of chorus-types but the finer point-pair–derived support catalogue the hitting set was built on — see the status update.)* See [THE_CLOSURE_THEOREM.md](THE_CLOSURE_THEOREM.md). |
| **THE BRIDGE IDENTITY — the metric span, PROVEN (here, 14 Jun)** | `G = 4Γ − J`: on the primitive (`N=0`) lattice the dual Hodge norm equals the primal geometric form; with Hodge–Riemann definiteness this closes the census (the minimum is finite and decidable). The **metric** half of the deck — geometry = algebra. A tool toward King Pin, not King Pin: it does not build the cut. See [THE_BRIDGE_THEOREM_PAPER_RANKFIX_v1.md](THE_BRIDGE_THEOREM_PAPER_RANKFIX_v1.md). |
| **THE SWEET LIE THEOREM — the primal pillar (carried from the surface campaign)** | For the Fermat fourfold, the resonant alliances of the 15 plane families are exactly the subsets of the **ten bipartite hexads** (the `3+3` splits of `K₆`, each a `K₃,₃`), and these ten **choruses** generate exactly rank 128 in the primal — *the mold of the winning cut.* Forged in the Hodge–Fermat campaign to quantize the fourfold rank; here it is the left pillar of the bridge. See [THE_SWEET_LIE_THEOREM.md](THE_SWEET_LIE_THEOREM.md). |
| **The reinforcing columns (carried from the surfaces)** | **Watermark** (the discriminant `m^{3(m−3)²}`, the price machinery), **Double Ladder** (the discriminant *group* structure), **Bend** (which small primes — 2, 3, 5 — open a pairing channel), **Wild Tooth** (the even-degree fold; the mod-4 tower whose depth `2^4` *caps the Steel ladder*), **Three-Ring** (non-separability — the cut is integral, not severable). Theorems of rock from the surface theory, here load-bearing columns of the bridge. |
| **Régime caveat (sealed)** | Five of those columns are **surface results** (`n = 2`); they do not reach the fourfold core (`n = 4`) without a gluing bridge that is itself unproven. Only **Sweet Lie**, the **Within-Pair Functor**, and the **Closed Walk Law** are fourfold-native. See [THE_ORBITAL_MAP_v1.md](THE_ORBITAL_MAP_v1.md). |
| **What is measured and standing** | The ten choruses → rank 128 (primal, byte-exact). The price floor `2^{5.585} < 2^{8.08}` (Steel). The closure of chorus-types (theorem). The metric Identity `G = 4Γ − J` (theorem). The backbone proven in the rank-20 miniature (`V(4,3)-prim`), two primes. |
| **What just reopened, with a witness** | **Stratum-12 covering.** The ten-slot `Z/4` cut covers the 143,520 point-pairs and the six-plane non-point-pairs, but the four-plane witness `w = P₀+P₁−P₆−P₇` escapes all 70 `Z/4` characters and all ten choruses. The census it was built on was point-pair-only; the missing detector is `mod-3 / mod-5`. The covering must be re-derived over a **complete** norm-12 census (point-pairs + 4-plane + 6-plane + higher, + coefficients `> ±1`), and the same caution applies to strata 14–22. |
| **What is dead, with data** | Covering the squirrels with local teeth (the forge / slings / sieve): **dead by exact theorem** — no six local teeth cover, leak `1 − 0.7⁶ = 11.76%`. Par-character covering of the six strata: **14 > 13**, dead by codimension. Direct Fincke–Pohst on the full rank-141 lattice: method-blocked (`~10^{17.5}` nodes). Crossing coordinate frames without translation: garbage (`2^{99.13}` vs `2^{5.585}` on the same 13 vectors). Reading a shell-count timeout as a vector count: an illegitimate inference (the grind is tree-bound, not count-bound). |
| **THE BRIDGE THEOREM — the deck (the cut), OPEN (the objective)** | The one theorem still missing, the mother theorem: *the rank-128 chorus mold that Sweet Lie builds in the Primal translates, through the Steel functionals in the Dual, into a 13-functional cut whose section has minimum ≥ 24.* The metric Identity gave the half that says the minimum is decidable; this gives the half that says a concrete cheap cut empties all six shells. Proven, this **is** King Pin. It does not exist today, and building it — now with stratum-12's covering reopened beneath it — is the campaign's open front. |

---

## What this is

Sphere packing asks a question a child can state and a specialist can spend a career on: how densely can identical balls fill space? In low dimensions the answer is known and beautiful; in high dimensions it is mostly open, and the best constructions are **lattices** — perfectly periodic arrangements whose density is captured by a single number, the center density `δ`. In dimension 128 the densest lattice known is Elkies' `MW128`, built in 2001 from a Mordell–Weil lattice in characteristic 2, with `δ = 2^97.40`. No one has beaten it in 24 years.

This campaign attacks that record from an unexpected direction: the cohomology of a Fermat variety. The lattice `V(4,4)-prim` — the primitive part of the plane lattice of the Fermat fourfold — has rank 141, determinant `2^128`, and is even. Cut it down to a rank-128 **section** by imposing 13 linear conditions (the "cut," a list of 13 dual functionals), and you get a 128-dimensional lattice whose density you can compute. The center density of such a section is `δ = (min/4)^{64}/√det`: it rewards a **large minimum** and a **small determinant** at once, and the two fight each other. To beat `MW128` the section needs minimum norm **≥ 24** while its cut stays cheap — precisely, price `< 2^{8.08}`. Because the lattice is even, "minimum ≥ 24" is the same as "the section contains no vector of norm 12, 14, 16, 18, 20, or 22" — six forbidden shells, all of which must be empty.

The deep difficulty is not the price (a cheap cut was found early) but the **emptiness**: proving a concrete section has no short vector, in a 141-dimensional lattice whose direct enumeration to norm ≤ 22 costs on the order of `10^{17.5}` tree nodes — astronomically out of reach on any hardware, let alone 8 GB. The campaign's entire intellectual arc is the search for a way to certify emptiness **by structure** instead of by enumeration, the way Elkies himself certified his minimum by the height theory of his lattice rather than by counting vectors. That search produced three new theorems, retired a whole family of dead approaches by proof, and reduced the record to a sharply stated objective — the **Bridge** — with one of its forbidden shells now re-opened to a concrete, written-down witness.

Every number in this repository comes from a run log or a file. Nothing is from memory; nothing is rounded to flatter; and where a result is inherited from the surface theory that came before, it is named as inheritance, not as discovery. Where a verdict was wrong — as the first "stratum-12 covered" was — it is corrected in place, with the witness that broke it.

---

## The two lineages — where the theorems came from

This is the heart of what a new collaborator needs to understand. The bridge is built from theorems of **two different origins**, and keeping them straight is what keeps the campaign honest.

### Lineage I — born on the surfaces of Fermat (the Hodge–Fermat campaign), and carried here

Before King Pin there was a different campaign: verifying the **Integral Hodge Conjecture** for high-dimensional Fermat varieties, using the Degtyarev–Shimada criterion, on the same 8 GB laptop. That campaign — recorded in its own repository — produced a collection of theorems about the discriminants and ranks of Fermat lattices. Several of them turn out to be exactly the structural facts the sphere-packing record needs. They were **not** forged for King Pin; they were forged for the conjecture, and they apply here because both problems live on the same Fermat cohomology.

- **The Sweet Lie Theorem** — the fourfold rank, quantized: the resonant alliances of the plane families are the subsets of the ten bipartite hexads of `K₆`, and the ten choruses generate rank 128. *In the bridge: the left pillar — the primal mold.*
- **The Watermark Theorem** — the discriminant `|disc NS(S_m)| = m^{3(m−3)²}`, proven for prime degree (Shioda's 1987 question, answered). *In the bridge: a column — the price machinery.*
- **The Double Ladder Theorem** — the discriminant *group* structure, `(Z/m)^{…} × (Z/m²)^{…}`. *In the bridge: a column.*
- **The Bend Theorem** — `b(p) = rank_{F_p}(G) − 12(m−3)`; a power sum over a finite field opens a pairing channel at `p` exactly when `p−1` divides the channel exponent, so only 2, 3, 5 bend the law. *In the bridge: a column — which primes matter. (It is exactly these primes — and the open `mod-3/5` detector for `w` — that the reopened stratum-12 now turns on.)*
- **The Wild Tooth Theorem** — the even prime tamed: over `F₂` every channel opens and the calculus folds (`t² ≡ t`); the deep tower of two lives at depth mod 4. *In the bridge: a column — and the source of the cap on the Steel ladder.*
- **The Three-Ring Theorem** — the composite discriminant group, and a proof that the bend is **non-separable** from the primitive heart. *In the bridge: a column — the cut is integral, not severable.*

A sealed régime caveat travels with these: five of them (Watermark, Double Ladder, Bend, Wild Tooth, Three-Ring) are **surface theorems** (`n = 2`). Reaching the fourfold core (`n = 4`) requires a gluing bridge that is itself unproven. Only Sweet Lie, the Within-Pair Functor, and the Closed Walk Law are fourfold-native. The map of which theorem lives where is [THE_ORBITAL_MAP_v1.md](THE_ORBITAL_MAP_v1.md), mandatory reading before any theorem is invoked in the fourfold régime.

### Lineage II — born here, for the record

Three theorems were forged inside the King-Pin campaign itself, to build the spans the inherited theorems do not cover:

- **The Closure Theorem** *(11 June 2026)* — the deck-beam. It proves the chorus-support-type catalogue is finite and closed (no new chorus-type at any norm), turning the census from a `10^{17.5}`-node enumeration into finite bookkeeping. See [THE_CLOSURE_THEOREM.md](THE_CLOSURE_THEOREM.md).
- **The Steel Theorem** *(12 June 2026)* — the right pillar, the dual. It proves the dual integerizes at `2^5` (forced), that the cheap dual-norms form a `2`-adic ladder capped at the Wild Tooth depth `2^4`, and that the price is a determinant of that ladder — so the floor `2^{5.585}` is structural, not a lucky search. See [THE_STEEL_THEOREM.md](THE_STEEL_THEOREM.md).
- **The Bridge Identity** *(14 June 2026)* — the metric span across the deck. `G = 4Γ − J` proves the dual Hodge norm equals the primal geometric form on the primitive lattice, closing the minimum as a finite, decidable quantity. The metric half of the mother theorem — geometry = algebra — but not yet the cut. See [THE_BRIDGE_THEOREM_PAPER_RANKFIX_v1.md](THE_BRIDGE_THEOREM_PAPER_RANKFIX_v1.md).

The honest line between the lineages: **King Pin did not re-prove the surface theorems — it discovered they were load-bearing for a problem they were never written for, and it built the three new spans (Closure, Steel, the Identity) the record needs and the surfaces never required.**

---

## The bridge — the picture that holds the whole campaign

```
   PUEBLO PRIMAL                  THE DECK                  PUEBLO DUAL
   (geometry, shapes)         (Bridge Theorem)           (algebra, numbers)
   ┌──────────────────┐      ╔═ metric span ═╗      ┌──────────────────┐
   │ ten choruses     │      ║  Identity ✓   ║      │ 13-functional    │
   │  → rank 128      │──────╢  G = 4Γ − J   ╟──────│  cut             │
   │  (the mold) ✓    │      ║  — the CUT    ║      │ min ≥ 24,        │
   └──────────────────┘      ║   still ?? ── ║      │ price < 2^8.08   │
        PILLAR: Sweet Lie ✓  ╚═══════════════╝      └──────────────────┘
                               DECK-BEAM: Closure ✓     PILLAR: Steel ✓
   ───────────────────────────────────────────────────────────────────────
   COLUMNS:  Watermark · Double Ladder · Bend · Wild Tooth · Three-Ring · Closed Walk
   ───────────────────────────────────────────────────────────────────────
   THE BANKS (bedrock):  V(4,4)-prim · rank 141 · det 2^128 · the Fermat fourfold lattice
```

- **The two banks** are the lattice itself: `V(4,4)-prim`, rank 141, det `2^128`. Bedrock, measured.
- **The Primal town** holds the geometry: the planes, the squirrels, the ten choruses. Its pillar is **Sweet Lie** (proven).
- **The Dual town** holds the algebra: the 13 functionals, the price, the determinant. Its pillar is **Steel** (proven).
- **The deck-beam** is **Closure** (proven): the chorus-type catalogue is finite. The **metric span** across the deck is the **Identity** (proven): geometry = algebra on the metric.
- **The columns** are the inherited theorems, bracing each side.
- **The deck itself — the cut** — the span that names 13 functionals emptying all six shells, is the **Bridge Theorem**, and it does not exist yet. Beneath it, the **stratum-12 covering** — its first plank — has just been reopened by the witness `w`. Building the deck, and re-laying that plank with a detector that sees `w`, is the objective. Figure in [THE_BRIDGE_VISUAL.md](THE_BRIDGE_VISUAL.md).

**The exact question the deck answers:** does the rank-128 chorus mold (Primal) translate into a 13-functional dual cut whose section has minimum ≥ 24? Yes → the Bridge Theorem is written → King Pin falls. No → the chasm is the wall, and it must be crossed another way (which character realizes the mold in the dual). The reopened stratum-12 sharpens the first sub-question to a single arithmetic: **is there a cheap `mod-3/5` detector that sees `w`?**

---

## Where the campaign stands — the minute of the match

- ✓ **The banks** — the lattice, det `2^128`, measured (primitive 141, span 142, 818 relations).
- ✓ **Left pillar (Sweet Lie)** — proven; the ten choruses generate rank 128 in the primal.
- ✓ **Right pillar (Steel)** — proven (here); the dual integerizes at `2^5`, ladder capped at `2^4`, price a ladder determinant, floor `2^{5.585} < 2^{8.08}`.
- ✓ **Deck-beam (Closure)** — proven (here); the chorus-type catalogue is finite and closed.
- ✓ **Metric span (Bridge Identity)** — proven (here, 14 Jun); `G = 4Γ − J`, geometry = algebra, the minimum is finite and decidable.
- ✓ **Miniature backbone** — proven at rank 20 (`V(4,3)-prim`), two primes.
- ⚠ **Stratum-12 covering — REOPENED (14 Jun).** The ten-slot `Z/4` cut covers the 143,520 point-pairs and the six-plane non-point-pairs (2,000 sampled, all hit). But the four-plane witness `w = P₀+P₁−P₆−P₇` escapes all 70 `Z/4` characters and all ten choruses → stratum-12 is not empty under that cut. The census was point-pair-only; the catalogue undercounts. Missing detector: `mod-3 / mod-5`.
- ✗ **Par-character covering of all six strata** — `14 > 13`, dead by codimension (ILP-verified twice).
- ✗ **THE DECK (Bridge Theorem, the cut)** — not built. **The open front.**

The live work, in order: (1) enumerate the **complete** non-point-pair norm-12 census (four-plane and six-plane families, then coefficients `> ±1`); (2) test a `mod-3 / mod-5` detector directly against `w` — does a 3- or 5-adic character see it, and at what price, reconciled with Steel's dual corollary?; (3) re-derive the hitting set over the complete census, and apply the same audit to strata 14–22 (their point-pair catalogues, 210 and 45, are equally incomplete). The price and the rank-128 mold are settled; what reopened is the **emptiness** — exactly the campaign's deepest difficulty, now wearing a concrete face.

---

## Dead veins — documented, not hidden (do not re-open)

- **Cover the squirrels with local teeth** (the forge, the slings, the sieve, the W33 pool): **dead by exact theorem.** No six local teeth cover the family — leak `1 − 0.7⁶ = 11.76%`. Geometric impossibility, measured.
- **Par-character cover in 13 slots:** the union of strata 12∪14∪18 needs **14 > 13** (ILP-exact, verified twice). Dead.
- **Direct Fincke–Pohst on the full rank-141 lattice:** method-blocked at `~10^{17.5}` nodes.
- **Cross coordinate frames without translation:** garbage. The same 13 vectors price at `2^{99.13}` (builder frame) and `2^{5.585}` (saturated frame). The saturated frame is canonical for price; the builder frame is provenance only.
- **The `2^{16.2}` threshold:** a retired mis-count. The real threshold is `2^{8.08}`.
- **Reading a shell-count timeout as a headwind:** illegitimate. A 17-minute `qfminim` grind is tree-bound (basis quality), not count-bound; it says nothing about how many vectors exist. The norm-12 question was settled instead by a fingerprint invariant, in seconds.
- **mod-3 / mod-5 in the *dual*:** the *dual price* carries no odd denominator (Steel: `det = 2^128` has no odd factor). **But note (14 Jun):** the wolves *and* the witness `w` are a **primal covering** phenomenon, invisible to every 2-adic detector; the `mod-3/5` character they need is a primal object, and whether it exists cheaply is **open**, not dead. The old line "the wolves are never a dual problem" is right; it does not close the primal question `w` just reopened.

---

## Discipline

- **Numbers from files only.** If a number is not in a log or a frame file, it is not claimed.
- **Two primes, every structural verdict.** Cross-prime confirmation is mandatory.
- **Bench before solder.** Every engine reproduces a known gate (the rank-20 kissing number, 15,390; the stratum-12 point-pair gate, 143,520) before any virgin run is trusted.
- **One canonical frame for price.** All price measured in the saturated frame `gram_L0sat` (det `2^128`); the builder frame is provenance only; crossing frames without the translation map is forbidden.
- **Proven, measured, and open are labelled distinctly.** Closure, Steel, and the Identity are theorems; the ten-chorus rank-128 mold is measured (necessary, not sufficient); the Bridge Theorem (the cut) is **open**; the stratum-12 covering is **reopened**, never conflated with the pillars.
- **Sweep every parity before claiming emptiness.** A norm-12 vector with `±1` coefficients has an even plane-count `k`; covering the `k = 6` family is not covering the shell. The witness `w` lives at `k = 4`. (The verdict it broke was a single-parity sweep — a corrected, documented error, kept in the record.)
- **Dead veins are documented, not buried** — and a *reopened* vein is flagged as reopened, with the witness that reopened it.

---

## Why this matters

A sphere-packing record is not a curiosity. The density of the best lattice in a given dimension underwrites error-correcting codes, lattice-based cryptography, numerical integration, and the geometry of high-dimensional data; a record-breaking construction is a reusable object across all of them. `MW128` has stood 24 years; a denser rank-128 lattice would be a genuine advance.

But the deeper prize is the method. If the **Bridge Theorem** can be built — a proof that a primal geometric mold translates into a dual cut with an inherited minimum — it is not a trick that works once for one lattice. It is a general principle for turning the geometry of a cohomology lattice into a packing bound. The metric half of that principle is now proven; the cut is the remaining half.

A clear word on scope. This campaign concerns one bounded, exact target: a rank-128 section of `V(4,4)-prim` beating `MW128`. The price is settled below threshold, the chorus-type catalogue is closed, three pillars-and-spans stand as theorems, and the dead routes are proven dead. What remains is the deck — the cut — and beneath its first plank, the stratum-12 covering reopened to a named witness. The campaign does not claim the record; it has built the abutments, laid the metric span, named the chasm to the line, and — when a plank proved rotten — said so, with the vector that broke it. The standard that governs the crossing is the one that produced three theorems forged here, six inherited and correctly attributed, zero false theorems, and one false "covered" caught and corrected with data.

The work continues. Cross the deck, and a record that has stood since 2001 falls.

---

## Repository map

**The bridge, the project, the visual**
- [`KING_PIN_THE_BRIDGE_PROJECT_v2.md`](KING_PIN_THE_BRIDGE_PROJECT_v2.md) — the project description and objectives (minute-and-second state), with the bridge figure embedded.
- [`THE_BRIDGE_VISUAL.md`](THE_BRIDGE_VISUAL.md) · [`the_bridge_theorem.svg`](the_bridge_theorem.svg) — the bridge, rendered, reproducible byte-exact.

**The theorems — Lineage II (forged here)**
- [`THE_CLOSURE_THEOREM.md`](THE_CLOSURE_THEOREM.md) — the deck-beam: the chorus-type catalogue is finite and closed.
- [`THE_STEEL_THEOREM.md`](THE_STEEL_THEOREM.md) — the dual pillar: the dual integerizes at `2^5`, ladder capped at `2^4`, price a ladder determinant.
- [`THE_BRIDGE_THEOREM_PAPER_RANKFIX_v1.md`](THE_BRIDGE_THEOREM_PAPER_RANKFIX_v1.md) — the metric span: the Identity `G = 4Γ − J`, geometry = algebra, the closed census.

**The theorems — Lineage I (carried from the surfaces)**
- [`THE_SWEET_LIE_THEOREM.md`](THE_SWEET_LIE_THEOREM.md) — the primal pillar: the ten choruses, the rank-128 mold.
- [`THE_WATERMARK_THEOREM.md`](THE_WATERMARK_THEOREM.md) · [`THE_DOUBLE_LADDER_THEOREM__2_.md`](THE_DOUBLE_LADDER_THEOREM__2_.md) · [`THE_BEND_THEOREM__1_.md`](THE_BEND_THEOREM__1_.md) · [`THE_WILD_TOOTH_THEOREM__1_.md`](THE_WILD_TOOTH_THEOREM__1_.md) · [`THE_THREE_RING_THEOREM__1_.md`](THE_THREE_RING_THEOREM__1_.md) — the columns.
- [`THE_ORBITAL_MAP_v1.md`](THE_ORBITAL_MAP_v1.md) — the régime map (`n=2` surface vs `n=4` fourfold-native); mandatory before invoking any theorem.
- [`THE_KATANA_STEEL_METHOD_v1.md`](THE_KATANA_STEEL_METHOD_v1.md) — the forging recipe the Steel Theorem proves.

**The record, the journals, the map**
- [`EL_DIARIO_DE_GLOTON_v171.md`](EL_DIARIO_DE_GLOTON_v171.md) — the full historical diary (§1–§207), **frozen** (not edited; superseded entries are flagged in the living diary).
- `DIARIO_PEPITAS_DE_ORO_v49_INDICE.md` · `DIARIO_PEPITAS_DE_ORO_v49_DETALLE.md` — the living index (read first) and its detail; `§SESIÓN-14JUN-PART2` carries the reopened stratum-12 and the witness `w`.
- [`GLOSARIO_PACHIPACHI.md`](GLOSARIO_PACHIPACHI.md) — the glossary.

**Frames, steel, data, engines** — the saturated frame `gram_L0sat_141_v1.txt` (canonical for price); the steel and dual files (`katana_steel_origbasis_v1.txt`, `katana_cut13_explicit_v1.txt`, `dualgram_L0sat_xD.txt`); the squirrels and support-set data (`squirrels_n141_norm12_v1.txt`, `sets_no_imp_*.txt`, `baseB_141_from_L0sat_v1.txt`); the engines (`chorus_plane_builder.cpp` — the φ-free bridge that regenerates the planes, the choruses, the 143,520 and the 70 `Z/4` pair-characters; `CAZALOBOS.cpp` — the wolf/`w` detector search; `tabla_tipos_d4_v2.cpp`; the toolbox `NOMORESQUIRRELS2.py`).

---

## References

1. N. Elkies, *Mordell–Weil lattices in characteristic 2*, and the `MW128` record configuration.
2. A. Degtyarev, I. Shimada, *On the topology of projective subspaces in complex Fermat varieties.* J. Math. Soc. Japan **68**:3 (2016), 975–996. arXiv:1405.4683.
3. T. Shioda, *The Hodge conjecture for Fermat varieties.* Math. Ann. **245** (1979), 175–184.
4. T. Shioda, *Some observations on Jacobi sums.* Advanced Studies in Pure Mathematics **12** (1987), 119–135.
5. J. H. Conway, N. J. A. Sloane, *Sphere Packings, Lattices and Groups.* Springer GTM 290.
6. H. Movasati, R. Villaflor, *Periods of linear algebraic cycles* (the period-quanta input behind the squirrel structure, and equation (6) behind the Bridge Identity).

*The abutments stand. The metric span is laid. One plank of the deck is reopened to a named witness, and the deck is the work. PMC.*
