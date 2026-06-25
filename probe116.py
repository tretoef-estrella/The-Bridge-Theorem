#!/usr/bin/env python3
"""Probe the dual-norm^2=2 W-reacher basis[116]: real determinant cost (D-orthogonal
residual vs best_cut's 13 covectors) and coverage of the 162 chorus-blind + 1935 wall."""
import numpy as np, flint
from fractions import Fraction
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

# recover basis[116]
L,T=flint.fmpz_mat(Drows).lll(transform=True, rep='gram', gram='exact')
T=np.array([[int(T[r,c]) for c in range(141)] for r in range(141)],dtype=object)
L=np.array([[int(L[r,c]) for c in range(141)] for r in range(141)],dtype=object)
f=T[116]
print(f"basis[116] dual-norm^2 = {Fraction(int(L[116,116]),32)}")
print(f"basis[116] reaches W (M_W f != 0): {bool(np.any((MW@f)!=0))}")

# ---- coverage: how many chorus-blind survivors does f pair nonzero with? ----
pair=MW @ f                         # length 162
killed=int(np.count_nonzero(pair))
print(f"\n[coverage] chorus-blind survivors f pairs NONZERO with: {killed}/162")
# full wall: does f disturb / pair with all 1935? (count nonzero pairings)
WALLv=np.array([squ(i,j) for (i,j,_) in wall],dtype=object)
pw=WALLv @ f
print(f"[coverage] full wall squirrels f pairs nonzero with: {int(np.count_nonzero(pw))}/1935")
# how many of the 162 does best_cut+f TOGETHER kill (best_cut kills 0 of these by def)
print(f"[coverage] chorus-blind survivors KILLED by best_cut alone: 0/162 (by construction)")
print(f"[coverage] chorus-blind survivors KILLED by adding f: {killed}/162")

# ---- determinant cost: D-orthogonal residual of f against best_cut's 13 covectors ----
# residual dnorm^2 = f^T D f - (Phi D f)^T (Phi D Phi^T)^-1 (Phi D f), exact rationals
Phi=BEST
PhiD = (Phi @ Dnp)                       # 13 x 141
G13  = (PhiD @ Phi.T)                     # 13 x 13  (= Phi D Phi^T)
PhiDf= (PhiD @ f)                         # 13
fDf  = int(f @ Dnp @ f)
G13q = flint.fmpq_mat([[int(G13[a,b]) for b in range(13)] for a in range(13)])
bq   = flint.fmpq_mat([[int(PhiDf[a])] for a in range(13)])
xq   = G13q.solve(bq)                      # (Phi D Phi^T)^-1 (Phi D f)
quad = sum(Fraction(int(PhiDf[a]),1)*Fraction(int(xq[a,0].numer()),int(xq[a,0].denom())) for a in range(13))
resid = Fraction(fDf,1) - quad
print(f"\n[det cost] f total dual-norm^2 (x32 num)= {fDf}  -> {Fraction(fDf,32)}")
print(f"[det cost] D-orthogonal residual of f vs best_cut's 13 covectors = {resid/32} = {float(resid/32):.4f}")
print(f"           (memory's Cobertura-perp claimed this MUST be >= 5.33 for any W-reacher)")
