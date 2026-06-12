# THE KATANA STEEL — THE GENERATION METHOD (byte-exact, for φ-free replication)
### Auditor → Glotón Claude · 8 June 2026 · how the 82 dual functionals were derived, verified from files

The steel (`katana_steel_origbasis_v1.txt`, 82 functionals, original coords) was **rederived canonically by the Auditor** (diario §222), not transported from the BKZ session. Here is the exact method, each step verified byte-exact against the files. It is **φ-free by construction** — everything stays in original coordinates.

## THE FOUR ANSWERS

**1. Which Gram?** `gram_V44prim_f2.txt` **directly** (det = `2^128` exact, flint-verified). No prior float reduction of the primal. The dual was formed **exactly**: the scaled dual Gram is `32 · G⁻¹`, which is **integer** because the common denominator of `G⁻¹` is exactly `2^5 = 32` (verified: every entry of `G⁻¹` has denominator dividing 32). This integer scaled dual Gram is `dualgram_V44prim_x32.txt`. *The 2-adic world keeps its books clean — the dual integerizes at `2^5`.*

**2. How the cheap duals were enumerated — NOT blind Fincke–Pohst.** Blind FP on `G⁻¹` (or the raw dual) **explodes** on this lattice — your measurement (133/141 GSO norms < 3, 20M nodes, nothing) is **correct and expected**: the dual is round. The method that worked avoids FP entirely:
   - Reduce the **scaled integer dual lattice** (`32·G⁻¹`) by **LLL, then BKZ with blocksize 24** (`dual_claim96.log`: `LLL b0=32 → BKZ-24`, 4 sweeps, shortest basis vector stays 32 in the ×32 metric = norm 1 unscaled). **Own reduction in coordinate form** — *not* fpylll Gram-mode (its Babai step infinite-loops on this Gram, diario §260). The reduced dual basis is `dual_red_my.txt`; the transform is `dual_U_my.txt`.
   - From the reduced dual basis, read the short vectors **and their pair-combinations** (`pair-combo extraction`), weighing each candidate's exact dual-norm `cᵀ G⁻¹ c` in flint rationals. This yields the canonical count: **norm 1 ×1 · 2 ×14 · 5/2 ×14 · 41/16 ×1 · 3 ×52 = 82 functionals of norm ≤ 3** (diario §225).

**3. The norm-1 steel.** It is the **shortest BKZ-24 reduced dual basis vector** (b0 = 32 in the ×32-scaled metric ↔ dual-norm exactly 1 unscaled), re-expressed in original coordinates. Verified byte-exact: `steel[0]ᵀ G⁻¹ steel[0] = 1`. It did **not** come from blind search or from geometry — it fell straight out of the BKZ-24 reduction of the scaled dual.

**4. Geometric step? No.** The steel is **purely short-of-the-dual** (BKZ-24 + pair-combo), no Sweet Lie content. The plane/shadow geometry (Sweet Lie) names the **primal** squirrels (norm-12 = differences of standard planes meeting in a point, diario §320) — that is a different object. The dual functionals carry no proven geometric structure.

## THE RECIPE TO REPLICATE ON `gram_L0sat_141_v1.txt` (your saturated frame, det 2^128), φ-FREE

1. Load your frame Gram `G`. Compute `G⁻¹` in **exact rationals** (flint). Find its common denominator `D` — **verify it; it may NOT be 2^5 for your frame.** Form the integer scaled dual Gram `D · G⁻¹`.
2. Reduce that integer scaled dual lattice by **LLL then BKZ-24** in **coordinate form** (own BKZ or glotonv6; **not** fpylll Gram-mode, **not** blind FP). Dump the reduced dual basis.
3. From the reduced basis, take short vectors **and pairwise combos**; weigh each candidate's exact dual-norm `cᵀ G⁻¹ c` in flint rationals against **your** `G⁻¹`. Keep norm ≤ 3.
4. Everything stays in **original (your-frame) coordinates** — no transform, no φ.

## CRITICAL CAVEATS (rectitud — read before running)

- **Blind FP will explode on your round dual too** — that is not a bug, it is why the method reduces (BKZ-24) first. If you skip the reduction you will reproduce your 20M-node dead run.
- **The price floor was corrected** (diario §225): the best 13-cut price is **EXACT `4096 = 2^12`** (one norm-1 + twelve norm-2 steels, **mutually orthogonal in the dual** → det = product), **not** the earlier `2^14.2` hunt estimate. Re-derive the price on YOUR chosen 13 as the exact det of their dual Gram.
- **The {2,3} lesson (diario §423):** an LLL/BKZ-reduced basis of a saturated frame can be **mixed-norm**; do not assume a pure-norm Z-basis. Verify **every** extracted functional's exact dual-norm against your `G⁻¹` by one exact rational Gram multiply — never trust the float GSO profile.
- The denominator `D` for your saturated frame must be measured, not assumed 32. If it is not a power of 2, the 2-adic cleanliness that made V(4,4)-prim's steel integerize at `2^5` does not transfer — report that as data.

Artifacts in the Auditor sandbox (re-weighable independently): `dualgram_V44prim_x32.txt` (the scaled dual Gram), `dual_red_my.txt` (BKZ-24 reduced dual basis), `dual_U_my.txt` (transform), `katana_steel_origbasis_v1.txt` (the 82, original coords). All numbers from files; method verified byte-exact (det 2^128, denom 2^5, steel[0] dual-norm 1). PMC.

---

## DATED CORRECTION — 8 June 2026 (Constructor, post-§46)
**The price figure in this document (`4096 = 2^12`) is a SUPERSEDED WAYPOINT. Do not use it as the live seal.** The 13-cut price ladder dropped across the campaign, each step a measured improvement (lower price → lower section det → higher δ at fixed minimum):

`2^14.2` (early hunt) → `4096 = 2^12` (orthogonal optimum over the cheapest steels, §225) → `64 = 2^6` (file wide-pool, flint-verified, diario §20.2) → **`48 = 2^5.585` (QB_sat wide-pool, cera-verified, diario §46).**

**Two lessons sewn so no future Claude repeats them:**
1. The dual-norm spectrum (e.g. "82 with classes 1/2/5/2/41/16/3") is a basis-dependent pair-combo YIELD, **not** a verified census and **not** the isometry invariant. Classes like 41/16 or 45/16 with high multiplicity in one frame are REAL dual vectors (verify each by `cᵀ G⁻¹ c`), not extraction artifacts. Do NOT "clean" a wide pool down to a narrow spectrum — the wide pool reaches cheaper cuts (the 48-cut uses deep-pool steels a narrow pool would discard).
2. When mapping a reduced dual back to functionals: the reduced Gram is `Qred = U · (D·G⁻¹) · Uᵀ` with U unimodular, so the reduced basis vectors are the **ROWS of U**, not the columns. Using columns gives norms that do not match `G⁻¹` — the bug that tangled the prior steel derivation. Always cross-check each extracted functional's exact dual-norm against `G⁻¹` directly.
