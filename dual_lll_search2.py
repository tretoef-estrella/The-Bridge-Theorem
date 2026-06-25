#!/usr/bin/env python3
import numpy as np, flint, itertools
from fractions import Fraction
from itertools import combinations, product

def load_int_mat(path):
    rows=[]
    for ln in open(path):
        ln=ln.strip()
        if not ln or ln.startswith('#'): continue
        p=ln.split()
        if len(p)==1: continue
        rows.append([int(x) for x in p])
    return rows
Drows=load_int_mat('dualgram_L0sat_xD.txt'); Dnp=np.array(Drows,dtype=object)
Dp=[]
for ln in open('dump_planes_L0sat_960x141_v1.txt'):
    p=ln.split()
    if len(p)==141: Dp.append([int(x) for x in p])
Dp=np.array(Dp,dtype=object)
BEST=np.array(load_int_mat('gabrieloak_best_cut_v1.txt'),dtype=object)
wall=[]
for ln in open('pitbull_TRUE_RESIDUAL_1935_v1__1_.txt'):
    ln=ln.strip()
    if not ln or ln.startswith('#'): continue
    p=ln.split(); wall.append((int(p[0]),int(p[1]),tuple(int(x) for x in p[2:6])))
cb=[(i,j) for (i,j,pr) in wall if pr==(8,4,0,0)]
def squ(i,j): return Dp[i]-Dp[j]
cb_surv=[(i,j) for (i,j) in cb if np.all((BEST @ squ(i,j))==0)]
MW=np.array([squ(i,j) for (i,j) in cb_surv],dtype=object)
def reaches_W(f):
    fv=np.array(f,dtype=object); return bool(np.any((MW @ fv)!=0))

# CORRECT Gram-LLL
L,T=flint.fmpz_mat(Drows).lll(transform=True, rep='gram', gram='exact')
T=np.array([[int(T[r,c]) for c in range(141)] for r in range(141)],dtype=object)
L=np.array([[int(L[r,c]) for c in range(141)] for r in range(141)],dtype=object)
assert np.all((T@Dnp@T.T)==L)
rows=[T[r] for r in range(141)]
norms=[int(L[r,r]) for r in range(141)]            # dual-norm^2 * 32

order=sorted(range(141), key=lambda r: norms[r])
print("[reduced basis] cheapest 14 vectors: dnorm2  reachesW")
for r in order[:14]:
    print(f"  basis[{r:>3}] dnorm2={Fraction(norms[r],32)!s:>6}  reachesW={reaches_W(rows[r])}")

single=[(norms[r],r) for r in order if reaches_W(rows[r])]
print(f"\n[single] cheapest basis W-reacher: dnorm2={Fraction(single[0][0],32)} (basis row {single[0][1]})")

# enumerate small combos of the K cheapest basis vectors, find cheapest W-reacher
K=30
idx=order[:K]
B=np.array([rows[r] for r in idx],dtype=object)
GK=(B @ Dnp @ B.T)                                  # K x K, numerators
def cnorm(c):
    cv=np.array(c,dtype=object); return int(cv @ GK @ cv)
best_num=single[0][0]; best_c=None
short=list(range(min(18,K)))
tested=0
for k in range(1,6):
    for combo in combinations(short,k):
        for signs in product((-1,1),repeat=k):
            c=[0]*K
            for t,a in enumerate(combo): c[a]=signs[t]
            num=cnorm(c)
            if num>=best_num: continue
            f=np.zeros(141,dtype=object)
            for a in range(K):
                if c[a]!=0: f=f+c[a]*B[a]
            tested+=1
            if reaches_W(f):
                best_num=num; best_c=c[:]
print(f"\n[combo] cheaper candidates evaluated for W-reach: {tested}")
mu=Fraction(best_num,32)
print(f"\n===== VERDICT NUMBER (upper bound on min dual-norm^2 of a W-reacher) =====")
print(f"  mu_W <= {mu} = {float(mu):.4f}")
print(f"  calibration: best_cut covectors dual-norm^2 in [2.0, 5.0]; chi* = 1.0")
print(f"  Cobertura-perp memory quoted irreducible extra cost >= 5.33")
