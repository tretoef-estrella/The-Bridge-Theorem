# THE ORBITAL MAP — the eight theorems and the backbone sun
### Theorem Auditor deliverable · Operación Glotón · what each theorem proves, how they connect, and which brick (if any) each lays in the backbone
**For: Rafael Amichis Luengo · Madrid · Goal: dethrone MW128 (n=128, δ=2^97.40)**
*10 June 2026 · Theorem-data only, every claim cited to a theorem section or a diary §. Regime (surface n=2 vs fourfold n=4) stated for every theorem. Maximum rectitude, no inflation, no underselling.*

---

## 0. THE ONE THING TO READ FIRST — THE REGIME SPLIT (it has burned the campaign before)

The eight theorems live in **two different worlds**, and the backbone lives in only one of them.

- **FOURFOLD WORLD (n=4).** The Glotón object is V(4,4)-prim: rank 141, det 2^128, the lattice of the 15·d³ standard planes of the Fermat **fourfold** X_d ⊂ P⁵. This is where the record is won.
- **SURFACE WORLD (n=2).** The Fermat **surface** S_m ⊂ P³, its 3m² lines, its Néron–Severi lattice NS(S_m). This is the Hodge mother-campaign.

**Only TWO of the eight theorems speak natively to the fourfold:** SWEET LIE (it is *about* V(4,d), explicitly) and — by the DS rank machinery they share — the two pair-theorems WITHIN-PAIR FUNCTOR and CLOSED WALK LAW. **The five discriminant theorems (Watermark, Double Ladder, Bend, Wild Tooth, Three-Ring) are surface results (n=2).** Nothing in them is proven to transfer to the rank-141 fourfold. This is not pessimism; it is the honest scope every one of those five documents states in its own ledger.

The consequence for the backbone is sharp and is stated in §C: **the bricks that build the backbone come almost entirely from the fourfold-native theorems. The five surface discriminant theorems are, today, a NAMED HOPE for PRIORITY 2 (the lift to rank 141 via gluing), not a delivered brick — and the hope rests on a regime crossing that is unproven.**

---

## A. THE EIGHT THEOREMS — MECHANISM, NOT TITLE

### A.1 SWEET LIE — *fourfold (n=4). The central engine.*
**Proves:** the rank of any alliance of plane families of V(4,d) is a finger-count over K₆. ν(S) = (−1)^{|S|+1}(1 + N_d(G_S)), where N_d counts alternating ±r labelings on the union graph G_S of the matchings — (d−1) per bipartite component, ε_d (=1 iff d even) per non-bipartite. Telescopes to rank V(4,d) = DS₄(d)+1.
**Mechanism (the part the backbone uses):** §3(a) — the span of one family is ⟨h⟩ ⊕ {characters of its support}, and the **Nonvanishing Lemma** (§2; Movasati–Villaflor period [5]; Villaflor [6, Prop 2.2]) says the plane class has **nonzero coefficient on every character of its support**. This is the period quantum the backbone needs. §3(e) — the 10 choruses D_β (one per coordinate bipartition), all sharing only the universal note ⟨h⟩. §5 — the **even-degree impostor** (d/2)(1,1,1,1,1,1) sings in every chorus; for d=4 this is the mechanism that creates the low-norm strata the backbone must forbid.
**Regime:** native fourfold. **This is the sun's nearest planet.**

### A.2 WITHIN-PAIR FUNCTOR — *fourfold-compatible (DS/CRT machinery). Completeness-lemma engine, half 1.*
**Proves:** the within-pair survivor count of a Fermat CRT block is dim(Sym²V)·c² (coupled) or dim(V⊗V)·c² (free); the free/coupled split is the collapse of the tensor square to the symmetric square; the char-2 obstruction is the **generic** swap torsion (Z/2)^{p^v−1}, not Fermat-specific.
**Mechanism the backbone uses:** the *pair* is the atom. Two planes meet with P·P′ ∈ {1,0,−2} (the incidence rule), which fixes pair-norms. This is the controlled engine that turns "which pairs exist" into "which norms a 2-plane combination can have."
**Regime:** built for the Fermat cell CRT splitting (the n-even Hodge front), but the pair-incidence combinatorics it formalizes is exactly the fourfold plane-pair rule. **Controlled by the Constructor (§103).**

### A.3 CLOSED WALK LAW — *DS rank machinery (both worlds). Completeness-lemma engine, half 2.*
**Proves:** the DS rank polynomial DS_n(m) is the constant term of a closed lattice walk of n+2 steps in dimension ⌊(m−1)/2⌋, rest permitted iff m even. The parity correction δ_m is exactly the walker's rest permission.
**Mechanism the backbone uses:** it counts *how plane-combinations of a given length close up* — the natural language for extending the pair rule {1,0,−2} → {12,14,18} to **length-3 and length-4 walks**, which is the open pencil question of the completeness lemma (§99, §100).
**Regime:** the walk identity is over the DS object directly; it applies wherever DS_n(m) is the rank, which includes the fourfold (DS₄ is V(4,d)'s rank, Sweet Lie §4). **Controlled by the Constructor (§103).**

### A.4 WATERMARK — *surface (n=2). Discriminant ORDER.*
**Proves:** |disc V| = m^{3(m−3)²} for the line lattice of the prime-degree Fermat **surface** (= |disc NS(S_m)| when gcd(m,6)=1). Mechanism: character-orthogonality pairings, a Ramanujan-circulant trace discriminant, the kernel-saturation theorem mK ⊆ SAT, and a 12-dimensional F_m relation count (Lemma C, the "d=12").
**Regime:** surface, n=2. **Does NOT speak of any lattice minimum** (verified: grep "minimal norm" across all six = empty, §92). It fixes the determinant of a surface lattice.

### A.5 DOUBLE LADDER — *surface (n=2). Discriminant GROUP structure.*
**Proves:** V*/V ≅ (Z/m)^{3m²−24m+59} × (Z/m²)^{3m−16} for prime m ≥ 7 (and the m=5 boundary). Mechanism: the height formula b = t − 2α + ρ₂; the nine affine shadows with autograph determinant 6 (a unit because gcd(m,6)=1); the rank ladder rank(Q|𝔪^K) = 12(m−3) − 3K(K+1), closed at rung K=2.
**Regime:** surface, n=2. Fixes the **glue group** of a surface lattice — its elementary-divisor profile. The "(Z/m²)^{3m−16}" count is the Double Ladder base that the Three-Ring continues to composite degree.

### A.6 BEND — *surface (n=2). The discriminant SHIFT at small primes.*
**Proves:** b(p) = 18 − dim(radical mod p), nonzero only where (p−1) | k for pairing channels k ∈ {2,4}: b(3)=7, b(5)=2, b(p≥7)=0. Mechanism: the SSvL pairing is a **power sum** Σ_t t^j over F_p; the channel opens exactly when (p−1) | j; for j ≤ 4 that is only p ∈ {2,3,5}.
**Regime:** surface, n=2. A correction term to the surface discriminant profile at composite degree.

### A.7 WILD TOOTH — *surface (n=2). The p=2 even kingdom.*
**Proves:** b(2)=14 (squarefree even), b(2)=−6 (deep 2-towers, a negative bend), unified by the universal ledger **b(p) = 36 − corank_p(σ) − dim(radical_p)**. Mechanism: over F₂ every power-sum channel opens (Σt^j ≡ 1 ∀j) AND the calculus folds (t² ≡ t); the deep tower lives entirely at depth mod 4.
**Regime:** surface, n=2. Gives the **2-adic structure** of the surface discriminant glue group. (Named by Fable as the supplier of the glue group's 2-structure — IF the gluing bridge existed for the fourfold.)

### A.8 THREE-RING — *surface (n=2). Binds the five.*
**Proves:** for squarefree composite m, b_p = (3m−16) + b(p) — Double Ladder base plus Bend shift. The crown result: **the bend is NON-SEPARABLE** — it lives inside the primitive order-m stratum, not in a cuttable sub-block (the order-3 stratum S₃ is empty, measured).
**Regime:** surface, n=2. The structural lesson — *a thing that cannot be taken apart* — is methodological; it warns that glue contributions need not decompose along the seams you expect.

### A.9 FRONTIER 6,6 — *methodological muscle (both worlds).*
**Proves (the controlled nugget, §103, §207):** φ(u+1) is a pure power of u IFF m is a prime power; composite m factors (CRT split) and silently inflates rank. The cure is the monomial basis (ROSETTA).
**Use to the backbone:** it is the proven demonstration that **CRT / per-character decompositions of the Fermat lattice are byte-exact controllable.** The backbone's m_a quanta ARE a per-character decomposition; the disc→min "gluing" bridge IS lattice CRT. The Frontier is the worked example that we control such splits — **but it is muscle, not a record-bullet** (V(4,4) has degree 4 = 2², the prime-power *clean* side, §213).

---

## B. THE ORBITAL MAP — HOW THEY CONNECT

```
                         ┌─────────────────────────────┐
                         │     THE BACKBONE (the sun)   │
                         │  rank-128 section min ≥ 24    │
                         │  ⟺ empty in 6 strata          │
                         │  {12,14,16,18,20,22}  (§93)   │
                         └──────────────┬──────────────┘
                                        │
              ┌─────────────────────────┼──────────────────────────┐
              │ TYPE LEMMA              │ COMPLETENESS LEMMA        │ TRANSVERSALITY
              │ (which supports carry   │ (every norm≤22 vector is  │ (the cut meets
              │  norm ≤ 22)             │  a listed type)           │  no light type)
              │                         │                           │
        ┌─────┴─────┐         ┌─────────┴──────────┐                │
        │ SWEET LIE │         │ WITHIN-PAIR FUNCTOR │                │ (engineering:
        │  §3(a)    │         │  + CLOSED WALK LAW  │                │  built from
        │  §3(e)    │         │  (pairs→{12,14,18}; │                │  the section,
        │  §5       │         │   walks len 3,4 OPEN)│               │  not a theorem)
        │ (impostor)│         └─────────┬───────────┘                │
        │  m_a=2/3  │                   │                            │
        └─────┬─────┘            FRONTIER 6,6                        │
              │                  (CRT muscle for                     │
        Nonvanishing             per-character                       │
        Lemma (MV [5])           decomposition)                      │
              │
   ═══════════╪══════════════════ REGIME WALL (n=4 above / n=2 below) ═══════════
              │
   PRIORITY 2 only — the LIFT to rank 141 — IF a disc→min gluing bridge exists:
        ┌──────────────────────────────────────────────────────────┐
        │  WATERMARK → DOUBLE LADDER → BEND → WILD TOOTH → THREE-RING │
        │  (the discriminant chain; all SURFACE n=2)                  │
        │  Watermark: ORDER  →  Double Ladder: GROUP  →               │
        │  Bend: composite SHIFT  →  Wild Tooth: p=2 2-structure  →    │
        │  Three-Ring: binds them, proves non-separability            │
        └──────────────────────────────────────────────────────────┘
```

**The two chains.** There are exactly two dependency chains:
1. **The rank/structure chain (fourfold-native):** Sweet Lie is the trunk; Within-Pair and Closed Walk are the DS-rank branches that share its DS₄ machinery. These feed the backbone DIRECTLY (type + completeness lemmas).
2. **The discriminant chain (surface):** Watermark (order) → Double Ladder (group) → Bend (composite shift) → Wild Tooth (p=2) → Three-Ring (the binding + non-separability). This chain is internally complete and beautiful, but it is **below the regime wall** — it governs surface discriminants, and only reaches the backbone IF the PRIORITY-2 gluing bridge crosses n=2 → n=4, which is unproven.

**Companion structure (from the documents' own headers):** Watermark and Double Ladder are direct companions (order + structure of the same surface group); Bend and Wild Tooth are the odd/even halves of the composite shift; Three-Ring binds Watermark+Double Ladder+Bend. Sweet Lie stands apart as the only fourfold rank theorem. Within-Pair and Closed Walk are companions to the Localization theorem (the Hodge-front torsion hunt).

---

## C. APPLICATION TO THE BACKBONE — WHICH BRICK, WHICH LEMMA (the point)

The backbone proves min ≥ 24 by residual reduction: **TYPE LEMMA + COMPLETENESS LEMMA + TRANSVERSALITY LEMMA** (§99, Fable's structure). For each theorem, precisely:

### SWEET LIE → TYPE LEMMA (delivered brick, the strongest)
- §3(a) + Nonvanishing Lemma: the type→support dictionary. A vector's norm is Parseval over characters, ‖v‖² = Σ|c_a|²μ_a (Hodge–Riemann on primitive (2,2)).
- The m_a quanta (§104): **m_a = 2/3, uniform across all 10 chorus pairs at rank 20, verified two primes.** Every primitive integer vector has ‖v‖² ≥ (2/3)·(#supported pairs). Norm 4 ⟹ support ≤ 6 pairs; the feasible types are subsets of a 10-element set mod S₆ — **tens of orbits, benign, not astronomical** (§104). The explosion risk is dead.
- §5 impostor (d=4 even): the mechanism CREATING strata 12–22 the backbone must forbid. The forbidden-gap target.
- **VERDICT: Sweet Lie supplies the TYPE LEMMA brick, and it is in hand at rank 20.** This is the live, delivered contribution. CENTRAL.

### WITHIN-PAIR FUNCTOR + CLOSED WALK LAW → COMPLETENESS LEMMA (partial brick, the hard bone)
- Within-Pair: the pair atom; P·P′ ∈ {1,0,−2} → pair-norms {12,14,18} (d=4) / {4,6,8} (d=3, §100).
- Closed Walk: the language to extend pairs to length-3/4 plane-combinations — the **open pencil question** (§99, §100): what norms do length-3/4 walks reach, and does norm ≤ 22 FORCE short-walk structure?
- **VERDICT: these two supply the COMPLETENESS LEMMA engine, but the brick is HALF-LAID.** Today the completeness lemma is "the photo disguised as a theorem" UNLESS the pair-theorems prove that norm ≤ 22 forces the listed types (§99 standing). This is the real pencil work and the hardest bone. CENTRAL but INCOMPLETE.

### TRANSVERSALITY LEMMA → no theorem (engineering)
- This is a property of the chosen cut, built from the section, not supplied by any theorem. Named for completeness.

### FRONTIER 6,6 → methodological support to the TYPE LEMMA
- The m_a quanta are a per-character CRT-like decomposition; the Frontier is the proven control of such splits. **VERDICT: muscle, not a structural brick.** It certifies the method, not a lemma. (Honest: NOT a hidden record-bullet, §213.)

### THE FIVE DISCRIMINANT THEOREMS → PRIORITY 2 only, and the brick is a HOPE, not delivered
This is the real gap (§103, §215), and rectitude demands it be stated without softening:

- Fable named the disc→min bridge as **gluing theory** (Conway–Sloane ch.4): if L0sat is presented as glued known sublattices, min = min over glue classes, and the five theorems govern that glue group (Wild Tooth gives its 2-structure).
- **THE PROBLEM: the five theorems are surface (n=2) results. The glue group they compute is the discriminant group of NS(S_m), a surface. V(4,4)-prim is a fourfold (n=4), rank 141.** There is no theorem — in these five or in the literature (§97, web search returned no fourfold identification) — that the fourfold's glue group is governed by the surface discriminant laws. The bridge crosses the regime wall, and that crossing is **unproven**.
- What the five WOULD give if the bridge existed: Watermark → the order of the glue group (the det 2^128 is consistent); Double Ladder → its (Z/m, Z/m²) profile; Bend/Wild Tooth → its p-adic and 2-adic fine structure (V(4,4) degree 4 = 2², so Wild Tooth's p=2 tower kingdom is the relevant one); Three-Ring → the warning that the glue may be non-separable.
- **VERDICT, maximum rectitude: the five discriminant theorems supply NO brick to the backbone at rank 20, and only a CANDIDATE brick at rank 141 (PRIORITY 2) that depends on an unproven n=2 → n=4 gluing bridge.** They must "earn their keep" (§104) by first establishing that bridge. Until then they are a beautiful, internally complete surface campaign that the fourfold cannot yet draw on. Do not count the glue bridge as in hand.

---

## D. THE STANDING (theorem-auditor verdict, R y D)

1. **The backbone sun is fed by exactly three fourfold-native theorems:** SWEET LIE (type lemma — delivered at rank 20, m_a=2/3), WITHIN-PAIR + CLOSED WALK (completeness lemma — engine in hand, the hard pencil OPEN at length-3/4 walks). FRONTIER 6,6 is method-muscle behind the type lemma.

2. **The completeness lemma is the load-bearing open problem.** The type lemma is benign (§104); whether norm ≤ 22 *forces* a listed type is the pencil that decides the backbone. Closed Walk Law is the right language; the length-3/4 walk norms are unmeasured.

3. **The five discriminant theorems do not reach the backbone today.** They are surface (n=2); the fourfold (n=4) bridge is the unproven gluing crossing named for PRIORITY 2. State this every time someone reaches for them — it is the regime wall that burned the campaign before (Frame Law, Trap 0).

4. **Next, theorem-side, per the diary:** enumerate support orbits |S| ≤ 6 at rank 20, compute exact min of V_S ∩ L per orbit, postdict the 15,390 (§104). If the type list misses even one of the 15,390 → completeness FALSE at rank 20 → backbone dies cheap, never touching rank 141. If it matches → backbone proven at rank 20, and ONLY THEN does the gluing bridge (the five theorems) get its day in PRIORITY 2.

No inflation, no underselling. The six theorems are the planets; only three of them are in the sun's gravity well today. The other five orbit a different star (the surface) and would need a proven bridge to be pulled in. RECTO Y DIRECTO. Cera y perfume. PMC.
