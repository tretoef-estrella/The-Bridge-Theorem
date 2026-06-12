#!/usr/bin/env python3
# ============================================================================
#  NOMORESQUIRRELS2.py — exact decider + HONEST 6-assist partial + LA RAMPA (cascade histogram) + raw-blind prefilter. FOR THE MAC.
#
#  Operación Glotón · dethrone MW128. Architect: Rafael Amichis Luengo (Madrid).
#  Self-contained: regenerates everything from the prime.
#
#  WHY v3 (Fable's verdict, §163-164):
#  The v2 ran on the Mac: CHAMPION None (the cut-13 does NOT close in W_big-of-37, floor 2176
#  blind, 4 teeth can't bite it). Fable's verdict: plan B YA (expand W_big), NOT a faster C++
#  lottery (the directed search wins maybe 2×, we need 10×). The deep reason is the pepita:
#  the 33 slots EXCLUDED from W_big are the QUARTER-INTEGER glue — the DEEPEST glue of the
#  lattice. We excluded them because the binary code couldn't read them, but the SLICE never
#  needed the code (only the diagnosis did). Three rounds slicing with half the pantry.
#
#  THE PEPITA — THE RESIDUAL LATTICE (the Architect's truffle, with rigor):
#  Fixing a prefix P (impostor + g glue), the t remaining functionals must NOT be picked from
#  a fixed pure-teeth pool — they must be the SHORT VECTORS OF THE RESIDUAL LATTICE (the
#  orthogonal projection of the dual onto the complement of span(P) — a qfminim on the
#  residual Gram). The Architect's four lateral ideas are ONE theorem of projection:
#  - the pure tooth appears at cost 2;
#  - the gravity-assist (tooth + pivot) appears as a residual vector < 2 (the near-in-span
#    glue is discounted automatically — high raw norm, low residual cost);
#  - the ant-bridge (t1+t2+t3, norm 6 < 8) appears as a SINGLE vector;
#  - the Chinese roof / siphon are the same said with another tile.
#  Cost in the det is the EXACT residual GSO, not a heuristic.
#
#  SANDBOX-MEASURED (the reason for the pantry test): on W_big-37 the residual pool has NO
#  vector < 2^1 (zero gravity-assists) — because the deep quarter-integer glue is in the
#  EXCLUDED 33 slots. The assists only appear once W_big is expanded to include that glue.
#
#  FABLE'S WARNING (cera): the FULL dual (71 slots, rank 141) benchmarks 13·128/141 = 2^11.8
#  — ABOVE threshold. Bigger isn't monotonically better; there's a sweet window. W_big-37
#  gives 2^3.47; the optimum is in between. So: expand by BITE_ext traffic, gate the
#  benchmark at each size, stop when it would exceed ~2^5.
#
#  ORDER OF FIRE (Fable):
#  (1) THE PANTRY TEST: expand W_big by exterior-teeth traffic, re-run the descent, watch the
#      blind floor. If it collapses (the quarter-glue unblocking the silver), plan B confirmed.
#      If it persists near rank 141 — THAT is a structural wall, known with data.
#  (2) The residual descent (qfminim of the prefix's residual Gram) on the best restriction.
#
#  INNOVATIONS (whose):
#  - The residual lattice = the four lateral ideas as one projection theorem, the pantry/
#    quarter-glue insight, the BITE_ext traffic ranking, the sweet-window warning: Fable.
#  - The seven lateral metaphors (twist/matrioska/tablecloth/roof/gravity-assist/siphon/
#    bridge): the Architect, from the bar.
#  - The builder frame, saturated L0, Φ̂, squirrel regeneration, the exterior teeth: campaign.
#
#  REQUIRES: numpy, sympy, cypari2 (Mac: plain `pip3 install cypari2`).
#  RUN ON MAC (25% CPU, no swap):
#    cd ~/Downloads && time caffeinate -dims taskpolicy -c utility python3 NOMORESQUIRRELS2.py 2>&1 | tee nomoresquirrels2_run1.log
#  Env: DESPENSA_RANKS (slot counts to test, default "37,55,71"), DESPENSA_SECONDS (descent/size).
# ============================================================================
import itertools, time, os, random
import numpy as np
from cypari2 import Pari
import sympy
from math import gcd

pari = Pari()
pari.allocatemem(2**33)
T0 = time.time()
OUT = os.environ.get("DESPENSA_OUT", "./nomoresquirrels2")
os.makedirs(OUT, exist_ok=True)
def log(m): print(f"[{time.time()-T0:8.1f}s] {m}", flush=True)

WBIG0 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,20,21,26,27,28,
         32,33,35,39,44,48,49,52,57,62,65,67,69]   # the binary-floor 37

def is_prime(n):
    if n < 2: return False
    for q in [2,3,5,7,11,13,17,19,23,29,31,37,41,43]:
        if n % q == 0: return n == q
    d,s = n-1,0
    while d % 2 == 0: d//=2; s+=1
    for a in [2,3,5,7,11,13,17,19,23,29,31,37]:
        x = pow(a,d,n)
        if x in (1,n-1): continue
        for _ in range(s-1):
            x = x*x % n
            if x == n-1: break
        else: return False
    return True
def find_p1mod8(s):
    p = s + (1 - s) % 8
    while not is_prime(p): p += 8
    return p
def matchings():
    res = []
    def rec(rem, cur):
        if not rem: res.append(tuple(cur)); return
        a = min(rem)
        for b in sorted(rem - {a}): rec(rem - {a,b}, cur + [(a,b)])
    rec(set(range(6)), [])
    return res
def rank_mod(M, p):
    M=[r[:] for r in M]; n=len(M); mc=len(M[0]) if M else 0; r=0
    for c in range(mc):
        piv=next((i for i in range(r,n) if M[i][c]%p),None)
        if piv is None: continue
        M[r],M[piv]=M[piv],M[r]; inv=pow(M[r][c],p-2,p); M[r]=[(v*inv)%p for v in M[r]]
        for i in range(n):
            if i!=r and M[i][c]:
                f=M[i][c]; M[i]=[(M[i][j]-f*M[r][j])%p for j in range(mc)]
        r+=1
        if r==n: break
    return r
def pair_reps():
    A=[a for a in itertools.product([1,2,3],repeat=6) if a.count(1)==a.count(3)]
    seen=set(); reps=[]
    for a in A:
        if a==(2,2,2,2,2,2): continue
        neg=tuple({1:3,2:2,3:1}[x] for x in a)
        key=frozenset([a,neg])
        if key not in seen: seen.add(key); reps.append(a)
    return reps
def w4(t):
    t %= 4
    return {0:2,2:-2,1:0,3:0}[t]

# ---------- foundation ----------
CACHE = "./despensa_cache"
os.makedirs(CACHE, exist_ok=True)
log("building builder frame (prime 7e9)")
P = find_p1mod8(7_000_000_000)
Ms = matchings()
planes = [(mi,t) for mi in range(15) for t in itertools.product(range(4),repeat=3)]
pidx = {pl:i for i,pl in enumerate(planes)}; N = len(planes)
for g in range(2,300):
    z = pow(g,(P-1)//8,P)
    if pow(z,4,P)==P-1 and all(pow(z,k,P)!=1 for k in range(1,8)): z8=z; break
roots = [pow(z8,1+2*a,P) for a in range(4)]
def prows(pl):
    mi,t = pl; rows=[]
    for e,(j,k) in enumerate(Ms[mi]):
        row=[0]*6; row[j]=1; row[k]=(-roots[t[e]])%P; rows.append(row)
    return rows
R = [prows(pl) for pl in planes]
def gv(rk): return {3:7,4:-2,5:1,6:0}[rk]
_g960f = f"{CACHE}/G960.npy"
if os.path.exists(_g960f):
    G960 = np.load(_g960f).astype(np.int64)
    log("G960 from cache")
else:
    G960 = np.zeros((N,N), dtype=np.int64)
    for i in range(N):
        G960[i,i] = 7
        for j in range(i+1,N):
            G960[i,j] = G960[j,i] = gv(rank_mod(R[i]+R[j], P))
    np.save(_g960f, G960.astype(np.int8))
    log("G960 done (cached)")
Gp = pari('['+';'.join(','.join(str(int(G960[i,j])) for j in range(N)) for i in range(N))+']')
ir = pari.matindexrank(Gp); rows0=[int(x)-1 for x in ir[0]]; cols0=[int(x)-1 for x in ir[1]]
PAIR = G960[np.ix_(rows0,list(range(N)))]
Bp = pari('['+';'.join(','.join(str(int(PAIR[i,j])) for j in range(N)) for i in range(142))+']')
HB = pari.mathnf(Bp)
Gsqnp = G960[np.ix_(rows0,cols0)]
Gsq = pari('['+';'.join(','.join(str(int(Gsqnp[i,j])) for j in range(142)) for i in range(142))+']')
Gsqinv = Gsq**(-1)
ones = pari('['+','.join(['1']*142)+']~')
dgc = ones.mattranspose()*Gsqinv*pari(HB)
Kcharge = pari.matkerint(dgc)
BB = pari(HB)*pari(Kcharge)
G141 = pari(BB).mattranspose()*Gsqinv*pari(BB)
detG141 = int(pari.matdet(G141))
assert abs(detG141) == 2**128, "det(L0) != 2^128"
log("GATE det(L0) = 2^128 PASS")
adjG = detG141 * G141**(-1)
adjG_np = np.array([[int(adjG[i,j]) for j in range(141)] for i in range(141)], dtype=object)
PAIRp = pari('['+';'.join(','.join(str(int(PAIR[i,j])) for j in range(N)) for i in range(142))+']')
PAIR_coords = Gsqinv * PAIRp
pairreps = pair_reps()
Tg = [(0,)+g for g in itertools.product(range(4),repeat=5)]
def act(g, pl):
    mi,t = pl
    return (mi, tuple((t[e]+(g[k]-g[j]))%4 for e,(j,k) in enumerate(Ms[mi])))

def restriction_U(slot_list):
    SW = np.zeros((N,N), dtype=object)
    for g in Tg:
        wt = 1 if sum(g)%2==0 else -1
        for sid in slot_list:
            ca = pairreps[sid]; wt += w4(sum(ca[x]*g[x] for x in range(6)) % 4)
        if wt == 0: continue
        for i in range(N): SW[i, pidx[act(g, planes[i])]] += wt
    SWrows = SW[np.ix_(rows0, list(range(N)))].astype(object)
    SWrows_p = pari('['+';'.join(','.join(str(int(SWrows[i,j])) for j in range(N)) for i in range(142))+']')
    SW_pareo = SWrows_p * PAIR_coords.mattranspose()
    M = pari(BB).mattranspose() * Gsqinv * SW_pareo * pari(BB)
    Mc = pari(M) / pari.content(pari(M))
    K = pari.matkerint(Mc)
    return pari.matkerint(pari(K).mattranspose())


# ============================================================================
# NMS2 (the Architect's '5 not 6' catch + la rampa): (1) the counting bound prunes before
# placing the 6th assist, so the NO-case partial was a depth-5 artifact — the YES verdict was
# always sound, but the navigation instrument lied. Fix: after every NO, GREEDY-COMPLETE the
# best partial to the full t assists — honest closable, one cheap completion per prefix.
# (2) LA RAMPA (floor basketball): cascade histogram — balls per hole in pick order + leak;
# a hole that swallows almost nothing is a wasted slot, visible at a glance. (3) RAW-BLIND
# PREFILTER: the partial scales with raw blind; skip the decider on prefixes whose raw blind
# exceeds RAWCAP_FACTOR x running minimum — effective tries multiplied.
# DECISION (the child's eyes, §codecs): the beam is a heuristic — it can never say 'cannot',
# only 'I couldn't'. The endgame is EXACTLY decidable: 'do <=t pool assists covering ALL blind
# exist?' via classic branch-on-rarest-element set cover. The rarest blind has 1-5 coverers
# (the chronics' rarity — the greedy's enemy — is the decider's FRIEND: minimal branching).
# Depth <=6, ~15k leaves of boolean ORs: milliseconds per prefix. Output is binary WITH
# CERTIFICATE: YES -> the assists (champion, straight to exact price + camera); NO -> a proof
# for this prefix (a thousand exact NOs across prefixes = an obstruction theorem taking shape,
# which a thousand stuck beams never are). All heuristic knobs (radar/weak-link/forcing)
# removed: the right machinery has zero dials. Interior steel kept in pool (richness != knobs).
# INVISIBLE MAN (the Architect's smoke-lungs trick, formalized): the old hitting gate checked
# SET-support (the squirrel's set touches a pantry slot) — but a squirrel can touch a slot and
# have its PROJECTION cancel to zero there. Set-support != projection-support: that hole let
# the ~476 invisible core into every pantry. THE SMOKE MAP reads the voids: for each of the 70
# slots, which squirrels its pure teeth actually pair nonzero with (cached, mod-p,
# safe-pessimistic). Then the pantry is CHOSEN to leave invisible core = 0 by construction
# (the paint poured before the descent), with WBIG0 as the glue base + greedy core-cover slots.
# NUCLEO (Fable, §core): the ~476 locked core smells like M-INVISIBLE squirrels (zero pairing
# with the WHOLE restriction — the hitting gate checked set-support, not projection!=0). No
# fiber inside M can ever bite what is orthogonal to M — electrospinning within M is sterile
# for that core. This engine: (1) MEASURES the M-invisible set once per pantry (mod-p + exact
# confirm) — fixed, prefix-independent by definition; (2) builds the EXTERIOR PURE TEETH of all
# non-pantry slots (cached): true norm 2, EXACTLY orthogonal to any prefix => residual norm 2
# = 1 bit each, the cheapest assists possible, and the only ones that reach the invisible core;
# (3) appends them to the somier pool — fabric of glue + directed steel, one loom.
# Pool-hunt cazas logged: the 400-cap neutralized the radius 6->8 test; pantry ranking by TOTAL
# traffic is the wrong list for core-killing (rank by CORE traffic).
# SOMIER (the Architect's spring-mesh / spider-web, formalized): individual greedy guarantees
# only ~63% of optimal coverage (1-1/e bound); at 98.4% covered the residue is a core only
# COMPLEMENTARY PAIRS bite. This engine: (1) precomputes the FULL pool-x-blind BITE MATRIX once
# per prefix (two mod-p int64 matmuls; false zeros only UNDER-claim coverage = safe-pessimistic;
# the finish-line gate stays exact); (2) prints the UNCOVERABLE CORE (all-zero columns) — the
# honest verdict: core>0 means pool problem (no selection order helps), core=0 means the fabric
# exists; (3) BEAM SEARCH (width SOMIER_BEAM) with bites-per-bit scoring and price-budget
# pruning (SOMIER_BITS_BUDGET); (4) 2-OPT polish (swap each chosen vs whole pool).
# KP2 FIXES (Fable, corner forensics): (1) qfminim with a stock cap does NOT return the
# shortest vectors — at radius 6 the 400-cap filled with long assists and crowded out the
# short ones ('radius 4 always wins' = pool artifact, not geometry; re-test r=6 after this).
# Fix: stock 4000 -> qfeval-sort -> keep the truly shortest. (2) greedy now scores
# bites-per-bit (a 250-bite assist at norm 1.5 beats a 300-bite one at norm 4) with
# randomized restarts (KP2_RESTARTS, default 2) — combos explored, not one deterministic shot.
# v9 FIX-B (found while testing): int(x~ * S * x) crashes — pari returns a 1x1 t_COL, not a
# scalar (this was PART of the reported line-350 crash). qfeval(S, x) gives the scalar clean.
# v9 FIX (root cause of BOTH Schur overflows, §169): we carried sc=2^128 INSIDE the Schur.
# adj(A) over 2^128-bit entries makes 2^1157-bit intermediates -> pari stack death (the v5 and
# v8 aborts). Fix: H2 = H / gcd(H) (the binary-floor gcd, ~2^127) is a SMALL-INTEGER Gram
# (entries 2-10). All descent arithmetic on H2: LLL ~100x faster, Schur intermediates ~2^40,
# no denominators, no guards needed. True norm = H2-norm * gcd / 2^128.
# v8 FIX (Constructor's catch, §168 — fix #2 that v7 missed): the raw-blind funnel
# 'if len(blind) >= best ... continue' SURVIVED into v7 — the exact v2 forensic flaw, kept by
# its own author. REMOVED: every prefix gets the full residual stage; closability is only
# knowable AFTER the assists. Optional honest sampling via DESPENSA_SAMPLE (random 1-in-k,
# NEVER conditioned on raw blind).
# v7 FIX (Architect's forensic question, §167): the v2 ran with the impostor DUPLICATED in
# every try (LLL col 0 = the norm-1 vector) -> all reported floors were one dimension
# PESSIMISTIC, and a closing assembly would have been silently rejected by the ks==13 gate.
# v7: the impostor is pinned explicitly, the prefix takes the first g RANK-INCREASING columns
# beyond it (mod-p rank guard), and the budget t = 12 - g is now honest.
# v6 FIX (Constructor's overflow catch, §166): Schur in TRUE units + pari minimal denominator
# (the detA scaling carried sc^g = 2^1280 of pure waste). Option B (kernel) REJECTED: the
# orthogonal sublattice excludes the gravity assists by construction. §164's '0 assists in
# W_big-37' is QUARANTINED until re-measured with the true projection (this engine does it).
# v5 FIX (Constructor's catch, §165): vecextract '..' range strings are GP-only — integer
# bitmasks now (verified in sandbox: blocks + column extraction exact).
# v4 FIXES (Fable review, §165): (1) sqL0 restored from v2's SEALED block (scale by detBtB +
# exact-division gate — v3 truncated rationals silently: the real bug, frames were fine).
# (2) mod-p screens restored (v2 asset dropped in v3). (3) The RESIDUAL STAGE actually exists:
# Schur complement of the prefix -> scaled qfminim -> assist pool -> greedy bite -> CLOSABLE
# floor (the true decision quantity). (4) hoisted matmuls (1410x recompute killed).
# (5) restriction_U once per pantry size. SEALED-BLOCKS LAW: copy, don't rewrite.
# ============================================================================

# ---------- squirrels + L0 coords (v2's sealed block: scaled + exact-division gate) ----------
sq = [(i,j) for i in range(N) for j in range(i+1,N) if G960[i,j]==1]
nsq = len(sq)
log(f"squirrels: {nsq}")
PAIRo = PAIR.astype(object)
BtB = pari(BB).mattranspose()*pari(BB); detBtB = int(pari.matdet(BtB))
BtB_inv = BtB**(-1)
XL = BtB_inv * pari(BB).mattranspose()
XLint = np.array([[int(XL[i,j]*detBtB) for j in range(142)] for i in range(141)], dtype=object)
Y = XLint @ PAIRo
sqL0 = np.zeros((141, nsq), dtype=object)
for n,(i,j) in enumerate(sq):
    col = Y[:,i] - Y[:,j]
    for k in range(141):
        q, r = divmod(int(col[k]), detBtB)
        assert r == 0, "sqL0 not integral — GATE FAIL"
        sqL0[k,n] = q
    if n % 40000 == 0: log(f"  sqL0 {n}/{nsq}")
log("sqL0 done (exact-division gate PASS)")
PS = [1048573, 2097143]
sqL0_mod = [np.array([[int(sqL0[k,n]) % p for n in range(nsq)] for k in range(141)], dtype=np.int64) for p in PS]
log("mod-p screens built")

def blind_of(C141cols):   # mod-p screen + exact confirm (v2's sealed logic)
    cand = np.ones(nsq, dtype=bool)
    for (p, Sm_) in zip(PS, sqL0_mod):
        Cm = np.array([[int(x) % p for x in cv] for cv in C141cols], dtype=np.int64)
        nz = (Cm @ Sm_) % p
        cand &= ~np.any(nz != 0, axis=0)
        if not cand.any(): return np.array([], dtype=int)
    idxs = np.where(cand)[0]
    Cob = [np.array([int(x) for x in cv], dtype=object) for cv in C141cols]
    return np.array([n for n in idxs if all(int(cv @ sqL0[:,n]) == 0 for cv in Cob)], dtype=int)

def slot_M141(sid):
    SW = np.zeros((N,N), dtype=object)
    for g in Tg:
        ca = pairreps[sid]; wt = w4(sum(ca[x]*g[x] for x in range(6)) % 4)
        if wt == 0: continue
        for i in range(N): SW[i, pidx[act(g, planes[i])]] += wt
    SWrows = SW[np.ix_(rows0, list(range(N)))].astype(object)
    SWrows_p = pari('['+';'.join(','.join(str(int(SWrows[i,j])) for j in range(N)) for i in range(142))+']')
    SW_pareo = SWrows_p * PAIR_coords.mattranspose()
    return pari(BB).mattranspose() * Gsqinv * SW_pareo * pari(BB)

def price_141(C141cols):          # exact price of covector set (saturated) — v2 sealed block
    k = len(C141cols)
    Cp = pari('['+';'.join(','.join(str(int(C141cols[c][r])) for c in range(k)) for r in range(141))+']')
    Kx = pari.matkerint(pari(Cp).mattranspose()); Cs = pari.matkerint(pari(Kx).mattranspose())
    ks = int(pari.matsize(Cs)[1])
    Hs = pari(Cs).mattranspose()*adjG*pari(Cs)
    d = int(pari.matdet(Hs))
    return (float(sympy.log(abs(d),2)) - ks*128, ks)

# ---------- THE PANTRY TEST + REAL RESIDUAL DESCENT ----------
sc = 2**128
def build_ext_teeth(slot_list):
    """Pure norm-2 duals of every slot NOT in the pantry (cached). 141-coords, exact."""
    teeth = []
    for a in [x for x in range(70) if x not in slot_list]:
        tf = f"{CACHE}/teeth_slot_{a}.npy"
        if os.path.exists(tf):
            T = np.load(tf, allow_pickle=True)
            for c in range(T.shape[1]):
                teeth.append((a, np.array([int(x) for x in T[:,c]], dtype=object)))
            continue
        Ma = slot_M141(a); Mc = pari(Ma)/pari.content(pari(Ma))
        Ka = pari.matkerint(Mc); Ua = pari.matkerint(pari(Ka).mattranspose())
        na = int(pari.matsize(Ua)[1])
        if na < 1:
            np.save(tf, np.zeros((141,0), dtype=object), allow_pickle=True); continue
        Ha = pari(Ua).mattranspose()*adjG*pari(Ua)
        cols = []
        try:
            Sa = pari.qfminim(Ha, 2*sc, 10**5, 2); Va = Sa[2]; nva = int(pari.matsize(Va)[1])
            Ua_np = np.array([[int(Ua[r,c]) for c in range(na)] for r in range(141)], dtype=object)
            for c in range(nva):
                tv = Ua_np @ np.array([int(Va[r,c]) for r in range(na)], dtype=object)
                cols.append(tv); teeth.append((a, tv))
        except Exception:
            pass
        T = np.zeros((141, len(cols)), dtype=object)
        for c, tv in enumerate(cols): T[:,c] = tv
        np.save(tf, T, allow_pickle=True)
    return teeth

def pantry_size(slot_list, secs, gdim, radius_true=3, max_assists_pool=400):
    """One restriction: build U/H once, descend prefixes, residual-qfminim assists, closable floor."""
    U = restriction_U(slot_list); nu = int(pari.matsize(U)[1])
    H = pari(U).mattranspose()*adjG*pari(U)
    det_r = float(sympy.log(abs(int(pari.matdet(H))),2)) - nu*128
    bench = det_r*13/nu
    log(f"  rank {nu}, det 2^{det_r:.1f}, benchmark 2^{bench:.2f}")
    # v9: DESCALE — kill the root cause before anything touches the Schur
    g0 = 0
    for i in range(nu):
        for j in range(nu): g0 = gcd(g0, int(H[i,j]))
    assert g0 > 0 and (sc % g0 == 0 or g0 % (sc//4) == 0), f"unexpected gcd {g0}"
    H2 = [[int(H[i,j])//g0 for j in range(nu)] for i in range(nu)]
    SCL = sc // g0                                   # true norm r <=> H2-norm r*SCL
    log(f"  descaled Gram: gcd 2^{g0.bit_length()-1}, H2-units per true norm = {SCL}")
    Hp = pari('['+';'.join(','.join(str(H2[i][j]) for j in range(nu)) for i in range(nu))+']')
    Up = pari(U)
    t_slots_max = 13 - 1 - gdim
    # ---- THE M-INVISIBLE CORE (fixed, prefix-independent): zero pairing with ALL of M ----
    U_np_ = np.array([[int(U[i,j]) for j in range(nu)] for i in range(141)], dtype=object)
    inv_cand = np.ones(nsq, dtype=bool)
    for (p, Sm_) in zip(PS, sqL0_mod):
        Um = np.array([[int(U_np_[i,j]) % p for j in range(nu)] for i in range(141)], dtype=np.int64)
        inv_cand &= ~np.any((Um.T @ Sm_) % p != 0, axis=0)
    inv_idx = np.where(inv_cand)[0]
    # exact confirm
    inv_exact = []
    for n in inv_idx:
        col = sqL0[:, n]
        if all(int(U_np_[:,j] @ col) == 0 for j in range(nu)): inv_exact.append(n)
    log(f"  M-INVISIBLE CORE of this pantry: {len(inv_exact)} squirrels "
        f"(mod-p candidates {len(inv_idx)}) — FIXED, no fiber inside M ever bites these")
    # ---- exterior steel teeth (directed fibers): the only reach into the invisible core ----
    ext_pool = build_ext_teeth(slot_list)
    int_pool = []
    for a in slot_list:
        tf = f"{CACHE}/teeth_slot_{a}.npy"
        if not os.path.exists(tf):
            build_ext_teeth([x for x in range(70) if x != a])
        T = np.load(tf, allow_pickle=True)
        for c in range(T.shape[1]):
            int_pool.append((a, np.array([int(x) for x in T[:,c]], dtype=object)))
    ext_pool = ext_pool + int_pool
    log(f"  steel pool: {len(ext_pool)} pure teeth ({len(int_pool)} interior)")
    if inv_exact:
        cov = np.zeros(len(inv_exact), dtype=bool)
        SQc = sqL0[:, inv_exact]
        per_slot = {}
        for a, tv in ext_pool:
            b = (tv @ SQc) != 0
            per_slot[a] = per_slot.get(a, 0) + int(b.sum())
            cov |= b
        log(f"  core reachable by exterior steel: {int(cov.sum())}/{len(inv_exact)} "
            f"| top core-traffic slots: {sorted(per_slot.items(), key=lambda t:-t[1])[:6]}")
    # impostor of THIS restriction (norm-1 covector), pinned in every cut (v7)
    Si = pari.qfminim(Hp, SCL, 10, 2)
    assert int(str(Si[0]))//2 >= 1, "no norm-1 vector in restriction — GATE FAIL"
    impU = np.array([int(Si[2][r,0]) for r in range(nu)], dtype=object)
    PIMP = pari('['+','.join(str(int(x)) for x in impU)+']~')
    imp141 = np.array([int((Up*PIMP)[i]) for i in range(141)], dtype=object)
    pg = 1073741789  # rank-guard prime
    best = (10**9, 10**9, None)   # (closable_floor, raw_blind, data)
    MINRAW = [10**9]                          # NMS2: running minimum raw blind (prefilter)
    t_local = time.time(); tries = 0
    while time.time()-t_local < secs:
        perm = list(range(nu)); random.shuffle(perm)
        Tp = pari('['+';'.join(','.join('1' if perm[j]==i else '0' for j in range(nu)) for i in range(nu))+']')
        R2 = pari.qflllgram(pari(Tp).mattranspose()*Hp*pari(Tp))
        full = pari(Tp)*pari(R2)                       # nu x nu unimodular, cols by length
        PF = Up*full                                    # 141 x nu covectors — ONCE (v4 fix #4)
        # v7: first g columns that INCREASE rank beyond the pinned impostor (mod-p guard)
        basis_rows = [np.array([int(x) % pg for x in impU], dtype=np.int64)]
        def rank_grows(vmod, rows):
            M = np.array(rows + [vmod], dtype=object)
            # tiny Gaussian elim mod pg
            M = [r.copy() for r in M]; rr = 0; cols = len(vmod)
            for c in range(cols):
                piv = next((i for i in range(rr, len(M)) if M[i][c] % pg), None)
                if piv is None: continue
                M[rr], M[piv] = M[piv], M[rr]
                inv = pow(int(M[rr][c]), pg-2, pg)
                M[rr] = [(int(v)*inv) % pg for v in M[rr]]
                for i in range(len(M)):
                    if i != rr and M[i][c]:
                        f = int(M[i][c]); M[i] = [(int(M[i][j]) - f*int(M[rr][j])) % pg for j in range(cols)]
                rr += 1
            return rr == len(M)
        sel = []; k = 0
        while len(sel) < gdim and k < nu:
            vU = np.array([int(full[i,k]) for i in range(nu)], dtype=object)
            vmod = np.array([int(x) % pg for x in vU], dtype=np.int64)
            if rank_grows(vmod, basis_rows):
                basis_rows.append(vmod); sel.append(k)
            k += 1
        pref141 = [np.array([int(PF[i,kk]) for i in range(141)], dtype=object) for kk in sel]
        blind = blind_of([imp141] + pref141)
        tries += 1
        if len(blind) < MINRAW[0]: MINRAW[0] = len(blind)
        if len(blind) > max(4000, RAWCAP_FACTOR * MINRAW[0]):
            if tries % 10 == 0: log(f"    g={gdim} try {tries}: raw {len(blind)} > cap (min {MINRAW[0]}) — skipped")
            continue
        if tries % 5 == 0: log(f"    g={gdim} try {tries}: raw blind {len(blind)} | best closable {best[0]}")
        if SAMPLE > 1 and (tries % SAMPLE) != 0 and len(blind) > 0:
            continue   # honest random thinning only — NEVER conditioned on raw blind (v8 fix #2)
        # --- RESIDUAL STAGE (the pepita): Schur complement of the prefix block ---
        # v7: reorder full so the prefix block = the selected rank-increasing columns
        rest = [k for k in range(nu) if k not in sel]
        order = sel + rest
        Pord = pari('['+';'.join(','.join('1' if order[j]==i else '0' for j in range(nu)) for i in range(nu))+']')
        full = pari(full)*Pord
        Gf = pari(full).mattranspose()*Hp*pari(full)    # nu x nu, scaled 2^128
        # extract blocks via vecextract strings
        maskA = (1 << gdim) - 1                      # indices 1..gdim
        maskD = ((1 << nu) - 1) ^ maskA              # indices gdim+1..nu
        maskAll = (1 << nu) - 1
        Ab = pari.vecextract(Gf, maskA, maskA)
        Bb = pari.vecextract(Gf, maskA, maskD)
        Db = pari.vecextract(Gf, maskD, maskD)
        detA = pari.matdet(Ab)                          # small now (H2 entries are digits)
        adjA = detA * pari(Ab)**(-1)                     # INTEGER adjugate, ~2^40 intermediates
        Sres = detA*pari(Db) - pari(Bb).mattranspose()*adjA*pari(Bb)   # integer, small
        qi = int(detA) * SCL                             # true residual norm r <=> x'Sres x = r*qi
        radius = int(radius_true) * qi
        try:
            Sm = pari.qfminim(Sres, radius, STOCK, 2); Vm = Sm[2]
            nvm = int(pari.matsize(Vm)[1])
        except Exception as e:
            nvm = 0
        if nvm == 0 and len(blind) > 0: continue
        # KP2: norms FIRST (cheap), sort, keep the truly shortest, THEN build 141-coords
        Cfull = pari.vecextract(full, maskAll, maskD)   # nu x (nu-gdim): the complement columns
        cand = []
        for c in range(nvm):
            xcol = pari('['+','.join(str(int(Vm[r,c])) for r in range(nu-gdim))+']~')
            rn = int(pari.qfeval(Sres, xcol)) / qi
            cand.append((rn, xcol))
        cand.sort(key=lambda t: t[0])
        cand = cand[:max_assists_pool]
        assists141 = []; assists_resnorm = []
        for rn, xcol in cand:
            wU = pari(Cfull)*xcol
            PW = Up*wU
            assists141.append(np.array([int(PW[i]) for i in range(141)], dtype=object))
            assists_resnorm.append(rn)
        for a, tv in ext_pool:        # NUCLEO: directed steel — residual norm exactly 2 (orthogonal slot)
            assists141.append(tv); assists_resnorm.append(2.0)
        order = list(range(len(assists141)))
        # ---- SOMIER: bite matrix once, then beam + 2-opt over SETS ----
        from math import log2 as _l2
        npool = len(assists141); nb = len(blind)
        if npool == 0 or nb == 0:
            closable, chosen, logcost, rem = nb, [], 0.0, blind
        else:
            # bite matrix via two mod-p int64 matmuls (safe-pessimistic; final gate is exact)
            BITE = np.zeros((npool, nb), dtype=bool)
            for (p, Sm_) in zip(PS, sqL0_mod):
                Am = np.array([[int(x) % p for x in a] for a in assists141], dtype=np.int64)
                BITE |= ((Am @ Sm_[:, blind]) % p) != 0
            bits_c = np.array([max(0.25, _l2(max(r, 1.05))) for r in assists_resnorm])
            core = int(np.sum(~BITE.any(axis=0)))
            log(f"      somier: pool {npool} x blind {nb} | UNCOVERABLE CORE = {core} "
                f"({'pool problem — no fabric helps' if core else 'fabric CAN exist'})")
            # ---- EXACT DECISION: branch on the rarest uncovered element ----
            import sys
            sys.setrecursionlimit(10000)
            best_partial = [nb + 1, [], 0.0]
            found = [None]
            nodes = [0]
            def decide(cov, chosen, lc):
                nodes[0] += 1
                if nodes[0] > DECIDE_NODE_CAP: return False
                u = ~cov
                nu_ = int(u.sum())
                if nu_ == 0:
                    found[0] = (list(chosen), lc); return True
                if nu_ < best_partial[0]:
                    best_partial[0], best_partial[1], best_partial[2] = nu_, list(chosen), lc
                if len(chosen) >= t_slots_max: return False
                marg = BITE[:, u].sum(axis=1)
                if int(marg.max()) * (t_slots_max - len(chosen)) < nu_: return False   # counting bound
                upos = np.where(u)[0]
                covcnt = BITE[:, u].sum(axis=0)   # per-assist marginals (= marg)
                # rarest element: fewest coverers among uncovered
                ecnt = BITE[:, upos].sum(axis=0)
                e = upos[int(np.argmin(ecnt))]
                coverers = np.where(BITE[:, e])[0]
                if len(coverers) == 0: return False   # pool core element: exact NO
                for c in sorted(coverers, key=lambda c: -int(marg[c])):
                    if c in chosen: continue
                    nlc = lc + (_l2(max(assists_resnorm[c], 1e-9)) if assists_resnorm[c] > 0 else 0.0)
                    if nlc > SOMIER_BUDGET: continue
                    if decide(cov | BITE[c], chosen + [c], nlc): return True
                return False
            yes = decide(np.zeros(nb, dtype=bool), [], 0.0)
            if yes:
                chosen, logcost = found[0]
                rem = np.array([], dtype=int)
                log(f"      DECISION: YES in {nodes[0]} nodes — certificate of {len(chosen)} assists (+{logcost:.2f} bits)")
            else:
                chosen, logcost = list(best_partial[1]), best_partial[2]
                cap_hit = nodes[0] > DECIDE_NODE_CAP
                # NMS2: GREEDY-COMPLETE to the full t assists (honest partial)
                covp = np.zeros(nb, dtype=bool)
                for c in chosen: covp |= BITE[c]
                while len(chosen) < t_slots_max:
                    u = ~covp
                    if not u.any(): break
                    marg = BITE[:, u].sum(axis=1)
                    cbest = int(np.argmax(marg))
                    if marg[cbest] == 0 or cbest in chosen: break
                    nlc = logcost + (_l2(max(assists_resnorm[cbest], 1e-9)) if assists_resnorm[cbest] > 0 else 0.0)
                    if nlc > SOMIER_BUDGET: break
                    chosen.append(cbest); logcost = nlc; covp |= BITE[cbest]
                log(f"      DECISION: {'CAP' if cap_hit else 'NO (exact for this prefix)'} in {nodes[0]} nodes "
                    f"— honest partial: {len(chosen)} assists leave {int((~covp).sum())}")
            # LA RAMPA: cascade histogram (balls per hole in pick order, then the leak)
            covr = np.zeros(nb, dtype=bool); holes = []
            for c in chosen:
                caught = int((BITE[c] & ~covr).sum()); holes.append(caught); covr |= BITE[c]
            log(f"      RAMPA: holes {holes} | leak {int((~covr).sum())} of {nb}")
            # the decider already set `chosen`/`logcost` (YES -> full cover; NO -> best partial).
            # closable = uncovered count from the decider's own result (no stale beam vars).
            cov_f = np.zeros(nb, dtype=bool)
            for c in chosen: cov_f |= BITE[c]
            rem = blind[~cov_f]
            closable = len(rem)
        if (closable, len(blind)) < (best[0], best[1]):
            best = (closable, len(blind), (full, chosen, logcost))
            log(f"    g={gdim} NEW BEST: raw {len(blind)} -> closable {closable} "
                f"with {len(chosen)} assists (res-norms cost +{logcost:.2f} bits)")
            if closable == 0:
                C13 = [imp141] + pref141 + [assists141[c] for c in chosen]
                pr, ks = price_141(C13)
                final_blind = blind_of(C13)
                log(f"    *** CLOSABLE=0: rank {ks}, exact price 2^{pr:.3f} (thr 2^8.08), final blind {len(final_blind)} ***")
                tag = f"g{gdim}_r{int(radius_true)}_n{len(slot_list)}_p{pr:.2f}"
                np.save(f"{OUT}/CUT13_CANDIDATE_{tag}.npy",
                        np.array(C13, dtype=object), allow_pickle=True)
                log(f"    *** CHAMPION SAVED: {OUT}/CUT13_CANDIDATE_{tag}.npy ***")
                if ks == 13 and pr < 8.08 and len(final_blind) == 0:
                    log(f"    *** ALL GATES PASS — NEXT: pair-strata 14/18 + CAMERA ***")
    return best, nu, bench

RANKS = [int(x) for x in os.environ.get("DESPENSA_RANKS","37,45,52,60").split(",")]
SECS = float(os.environ.get("DESPENSA_SECONDS","300"))
GDIM = int(os.environ.get("DESPENSA_GDIM","10"))
RADIUS = int(os.environ.get("DESPENSA_RADIUS","3"))
STOCK = int(os.environ.get("KP2_STOCK","4000"))       # qfminim stock before sorting
DECIDE_NODE_CAP = int(os.environ.get("DECIDE_NODE_CAP","2000000"))  # exact-search node cap
RAWCAP_FACTOR = float(os.environ.get("RAWCAP_FACTOR","2.0"))        # skip prefixes with raw blind > factor x min
SOMIER_BUDGET = float(os.environ.get("SOMIER_BITS_BUDGET","9.0"))  # price-prune (bits of assists)   # v10: honda radius (Fable's 3rd lever, bridges of 3+ teeth at radius 4-6)
SAMPLE = int(os.environ.get("DESPENSA_SAMPLE","1"))   # 1 = every prefix gets the residual stage
BENCH_CEIL = float(os.environ.get("DESPENSA_BENCH_CEIL","6.0"))   # Fable: covering always costs extra

# exterior traffic ranking (with CORRECT sqL0 now): quick blind via W_big0 LLL prefix
U0 = restriction_U(WBIG0); nu0 = int(pari.matsize(U0)[1])
H0 = pari(U0).mattranspose()*adjG*pari(U0)
Hp0 = pari('['+';'.join(','.join(str(int(H0[i,j])) for j in range(nu0)) for i in range(nu0))+']')
R20 = pari.qflllgram(Hp0); PF0 = pari(U0)*pari(R20)
pref0 = [np.array([int(PF0[i,k]) for i in range(141)], dtype=object) for k in range(GDIM)]
blind0 = blind_of(pref0)
log(f"quick blind set (W_big0, g={GDIM}): {len(blind0)} squirrels")
S0q = sqL0[:, blind0]
EXT0 = [a for a in range(70) if a not in WBIG0]
ext_traffic = {}
_rankf = f"{CACHE}/ranked_ext.txt"
if os.path.exists(_rankf):
    ranked_ext = [int(x) for x in open(_rankf).read().split()]
    log(f"exterior traffic ranking from cache: {ranked_ext[:8]}...")
else:
    for ai, a in enumerate(EXT0):
        Ma = slot_M141(a); Mc = pari(Ma)/pari.content(pari(Ma))
        Ka = pari.matkerint(Mc); Ua = pari.matkerint(pari(Ka).mattranspose())
        na = int(pari.matsize(Ua)[1])
        if na < 1: ext_traffic[a]=0; continue
        Ha = pari(Ua).mattranspose()*adjG*pari(Ua)
        tr = 0
        try:
            Sa = pari.qfminim(Ha, 2*sc, 10**5, 2); Va = Sa[2]; nva = int(pari.matsize(Va)[1])
            Ua_np = np.array([[int(Ua[r,c]) for c in range(na)] for r in range(141)], dtype=object)
            for c in range(nva):
                tv = Ua_np @ np.array([int(Va[r,c]) for r in range(na)], dtype=object)
                tr += int(np.sum((tv @ S0q) != 0))
        except Exception:
            pass
        ext_traffic[a] = tr
        if ai % 8 == 0: log(f"  ext slot {a} ({ai+1}/{len(EXT0)}): traffic {tr}")
    ranked_ext = sorted(EXT0, key=lambda a: -ext_traffic.get(a,0))
    open(_rankf,"w").write(' '.join(str(a) for a in ranked_ext))
    log(f"exterior slots by blind traffic (cached): {ranked_ext}")

# ---- THE SMOKE MAP (once, cached): true projection-support of every squirrel per slot ----
def smoke_map():
    SM = {}
    for a in range(70):
        sf = f"{CACHE}/smoke_slot_{a}.npy"
        if os.path.exists(sf):
            SM[a] = np.unpackbits(np.load(sf))[:nsq].astype(bool); continue
        teeth = build_ext_teeth([x for x in range(70) if x != a])   # builds/caches slot a's teeth
        vis = np.zeros(nsq, dtype=bool)
        for aa, tv in teeth:
            if aa != a: continue
            for (p, Sm_) in zip(PS, sqL0_mod):
                tm = np.array([int(x) % p for x in tv], dtype=np.int64)
                vis |= (tm @ Sm_) % p != 0
        SM[a] = vis
        np.save(sf, np.packbits(vis.astype(np.uint8)))
        if a % 10 == 0: log(f"  smoke map: slot {a}/70")
    return SM

log("building THE SMOKE MAP (true projection-support, cached)...")
SMOKE = smoke_map()
log("smoke map ready")

def pantry_by_core(target_size):
    """WBIG0 base + greedy slots that maximize newly-visible squirrels until invisible core = 0."""
    pantry = list(WBIG0)
    vis = np.zeros(nsq, dtype=bool)
    for a in pantry: vis |= SMOKE[a]
    log(f"  pantry base {len(pantry)} slots: invisible core {int((~vis).sum())}")
    while len(pantry) < target_size:
        best_a, best_gain = None, -1
        for a in range(70):
            if a in pantry: continue
            gain = int((SMOKE[a] & ~vis).sum())
            if gain > best_gain: best_gain, best_a = gain, a
        if best_a is None: break
        pantry.append(best_a); vis |= SMOKE[best_a]
        core_now = int((~vis).sum())
        log(f"  + slot {best_a} (gain {best_gain}) -> invisible core {core_now}")
        if core_now == 0 and len(pantry) >= 40:
            log(f"  CORE = 0 BY CONSTRUCTION at {len(pantry)} slots — the paint is poured")
            break
    return sorted(pantry), int((~vis).sum())

results = []
for nslots in RANKS:
    slot_list, residual_core = pantry_by_core(nslots)
    log(f"PANTRY (core-chosen) {len(slot_list)} slots, residual invisible core {residual_core}:")
    if residual_core > 0:
        log(f"  WARNING: {residual_core} squirrels invisible even to this pantry — "
            f"they live deeper (Z/4 floor / impostor-only) — exterior steel in pool covers the reachable")
    (closable, raw, data), rnk, bch = pantry_size(slot_list, SECS, GDIM, radius_true=RADIUS)
    results.append((nslots, rnk, bch, raw, closable))
    log(f"PANTRY size {nslots}: rank {rnk}, bench 2^{bch:.2f}, raw floor {raw}, CLOSABLE floor {closable}")
    if bch >= BENCH_CEIL:
        log(f"  benchmark 2^{bch:.2f} >= ceiling 2^{BENCH_CEIL} — sweet window edge, stopping expansion")
        break

log("="*60)
log("PANTRY RESULTS:")
for nslots, rnk, bch, raw, cl in results:
    log(f"  {nslots} slots (rank {rnk}, bench 2^{bch:.2f}): raw {raw} | CLOSABLE {cl}")
log("VERDICT: CLOSABLE floor collapsing with size => plan B confirmed; assemble champion with v2 machinery.")
log("         CLOSABLE floor persisting => structural wall — report to Fable with this table.")
log("DONE.")
