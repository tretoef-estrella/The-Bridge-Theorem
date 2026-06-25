#!/usr/bin/env python3
"""
W_obstruction_test_scout.py  (SANDBOX SCOUT, float)
Confirms/kills the v109-PART65 explanation.

v109 claim: best_cut's lever is e96-tuned, ORTHOGONAL to the chorus-blind core
            which lives in 'e32+e48 puro'; the method is e96-blind.
Scout already showed: best_cut is 65% in e32+e48 (NOT e96-tuned). So the
explanation is suspect. This script pins the REAL obstruction:

  W := span of the chorus-blind (8,4,0,0) squirrels that survive best_cut.
  If the 26 covectors' e32+e48 weight lands in W^perp (not W), THEN the
  obstruction is "duals avoid W", NOT "duals can't reach e32+e48".
"""
import numpy as np
from itertools import permutations, product
np.set_printoptions(suppress=True)

# ---------- eigenspace machinery (same as scout) ----------
P=17; Z8=2
def zpow(k): return pow(Z8,k%8,P)
seen=set(); Mtab=[]
for perm in permutations([1,2,3,4,5]):
    e=[0,*perm]; pairs=sorted((min(e[2*t],e[2*t+1]),max(e[2*t],e[2*t+1])) for t in range(3))
    c=tuple(x for p in pairs for x in p)
    if c not in seen: seen.add(c); Mtab.append(c)
def pidx(mi,ph): return mi*64+ph[0]*16+ph[1]*4+ph[2]
chars=[a for a in product([1,2,3],repeat=6) if sum(a)%4==0]
def supp(M):
    edges=[(M[0],M[1]),(M[2],M[3]),(M[4],M[5])]
    return set(a for a in chars if all((a[x]+a[y])%4==0 for (x,y) in edges))
supps=[supp(M) for M in Mtab]
IPOW={0:(1.,0.),1:(0.,1.),2:(-1.,0.),3:(0.,-1.)}
def isovec(a):
    mi=next((i for i,s in enumerate(supps) if a in s),None)
    M=Mtab[mi]; edges=[(M[0],M[1]),(M[2],M[3]),(M[4],M[5])]
    re=np.zeros(960); im=np.zeros(960)
    for s in product(range(4),repeat=6):
        ph=tuple((s[y]-s[x])%4 for (x,y) in edges)
        r,ii=IPOW[(-sum(a[t]*s[t] for t in range(6)))%4]
        idx=pidx(mi,ph); re[idx]+=r; im[idx]+=ii
    return re,im
def _frac(x):
    if '/' in x: a,b=x.split('/'); return float(a)/float(b)
    return float(x)
def load_mat(path):
    rows=[]
    with open(path) as fh:
        for ln in fh:
            ln=ln.strip()
            if not ln or ln.startswith('#'): continue
            p=ln.split()
            if len(p)==1: continue
            rows.append([_frac(x) for x in p])
    return np.array(rows)
G=load_mat('gram_L0sat_141_v1.txt'); Ginv=np.linalg.inv(G)
Dp=[]
with open('dump_planes_L0sat_960x141_v1.txt') as fh:
    for ln in fh:
        ln=ln.strip()
        if not ln or ln.startswith('#'): continue
        p=ln.split()
        if len(p)==141: Dp.append([float(x) for x in p])
Dp=np.array(Dp)
def push(coeff): return coeff@Dp
def eig_of(a): return {0:240,3:96,1:48,2:32}[a.count(1)]
real=[a for a in chars if a.count(1)==a.count(3)]
buckets={32:[],48:[],96:[],240:[]}
for a in real:
    re,im=isovec(a)
    if a==(2,2,2,2,2,2): buckets[240].append(push(re)); continue
    lam=eig_of(a); buckets[lam].append(push(re)); buckets[lam].append(push(im))
def g_ob(vecs):
    Mt=np.array(vecs).T; Gm=Mt.T@G@Mt; w,U=np.linalg.eigh(Gm)
    keep=w>1e-7*max(1.0,w.max()); return Mt@U[:,keep]/np.sqrt(w[keep])
Bs={l:g_ob(v) for l,v in buckets.items()}
print("[eig] ranks", {l:Bs[l].shape[1] for l in Bs})
def proj_eig(l,x): B=Bs[l]; return B@(B.T@(G@x))
def comp_3248(x): return proj_eig(32,x)+proj_eig(48,x)   # component in e32+e48

# ---------- load cuts, reconstruct wall, build W ----------
def load_cut(path):
    rows=[]
    with open(path) as fh:
        for ln in fh:
            ln=ln.strip()
            if not ln or ln.startswith('#'): continue
            p=ln.split()
            if len(p)==141: rows.append([_frac(x) for x in p])
    return np.array(rows)
BEST=load_cut('gabrieloak_best_cut_v1.txt')   # 13 x 141 covectors
KAT =load_cut('katana_cut13_explicit_v1.txt')

# wall: i j e32 e48 e96 e240
wall=[]
with open('pitbull_TRUE_RESIDUAL_1935_v1__1_.txt') as fh:
    for ln in fh:
        ln=ln.strip()
        if not ln or ln.startswith('#'): continue
        p=ln.split(); i,j=int(p[0]),int(p[1]); prof=tuple(int(x) for x in p[2:6])
        wall.append((i,j,prof))
print(f"[wall] {len(wall)} squirrels")
# reconstruct each squirrel v = d_i - d_j ; gate norm 12 + energy profile matches file
def squ(i,j): return Dp[i]-Dp[j]
bad=0
for (i,j,prof) in wall[:50]:
    v=squ(i,j); n=v.T@G@v
    e=tuple(round(proj_eig(l,v).T@G@proj_eig(l,v)) for l in (32,48,96,240))
    if abs(n-12)>1e-5 or e!=prof: bad+=1
print(f"[gate] first 50 squirrels: norm-12 & profile match -> mismatches={bad}")

# chorus-blind = profile (8,4,0,0)
cb=[(i,j) for (i,j,prof) in wall if prof==(8,4,0,0)]
print(f"[wall] chorus-blind (8,4,0,0): {len(cb)}")
# survivors of best_cut: Phi v = 0 for all 13 covectors
def alive(cut,v): return np.all(np.abs(cut@v)<1e-6)
cb_surv=[(i,j) for (i,j) in cb if alive(BEST,squ(i,j))]
print(f"[wall] chorus-blind surviving best_cut: {len(cb_surv)}")

W_vecs=np.array([squ(i,j) for (i,j) in cb_surv]).T   # 141 x N
# rank of W in G-metric
Gm=W_vecs.T@G@W_vecs; wv=np.linalg.eigvalsh(Gm); rW=int((wv>1e-6*max(1,wv.max())).sum())
print(f"[W] span of chorus-blind survivors: rank = {rW}")
# is W inside e32+e48 ? measure leakage into e96+e240
leak=0.0; tot=0.0
for c in range(W_vecs.shape[1]):
    v=W_vecs[:,c]; tot+=v.T@G@v
    leak+=proj_eig(96,v).T@G@proj_eig(96,v)+proj_eig(240,v).T@G@proj_eig(240,v)
print(f"[W] energy leakage into e96+e240: {100*leak/tot:.4f}%  (want ~0 => W subset e32+e48)")

# G-orthonormal basis of W
Bw=g_ob([W_vecs[:,c] for c in range(W_vecs.shape[1])])
def proj_W(x): return Bw@(Bw.T@(G@x))

# ---------- THE TEST: where does the 26 covectors' e32+e48 weight land? ----------
print("\n===== covectors' e32+e48 component: fraction in W vs W^perp =====")
for name,CUT in [('best_cut',BEST),('katana',KAT)]:
    print(f"--- {name} ---")
    agg_inW=0.0; agg_e=0.0
    for r in range(CUT.shape[0]):
        phi=Ginv@CUT[r]
        c=comp_3248(phi)                 # e32+e48 part of primal rep
        e_c=c.T@G@c
        if e_c<1e-9:
            print(f" cov{r:>2}: e32+e48 energy ~0 (pure e96/e240)"); continue
        inW=proj_W(c); e_inW=inW.T@G@inW
        agg_inW+=e_inW; agg_e+=e_c
        print(f" cov{r:>2}: e32+e48 energy={e_c:6.3f}  in W={e_inW:6.3f} ({100*e_inW/e_c:5.1f}%)  in W^perp={100*(1-e_inW/e_c):5.1f}%")
    print(f"  >>> {name} TOTAL e32+e48 weight in W: {100*agg_inW/agg_e:.2f}%  (if ~0 => duals AVOID W, the real obstruction)")
print("\n[dim] e32+e48 = 120-dim ; W =",rW,"; W^perp within e32+e48 =",120-rW,
      "; #covectors with e32+e48 weight bounded by that complement.")
