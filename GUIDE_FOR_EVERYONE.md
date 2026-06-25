# A Guide for Everyone

*No advanced mathematics needed. This page explains, in plain language, what this repository is about, what was proved, and — honestly — what was not.*

---

## The problem: stacking balls in 128 dimensions

How do you stack identical balls so they fill space as tightly as possible? In three dimensions the answer is the orange-stack you see at a grocery store (it fills about 74% of space). The same question makes sense in higher dimensions, and there it stops being intuitive and starts being useful: the densest packings in high dimensions are the same objects that give the best **error-correcting codes** — the mathematics that lets a scratched disc still play and a weak signal still arrive intact.

In **dimension 128**, the densest packing anyone has ever found was constructed by the mathematician Noam Elkies around 2001. It is called **MW128**, and it has stood as the record for over two decades. Beating it is hard precisely because it has stood so long.

## The plan: borrow a shape from geometry

Searching 128-dimensional space blindly is hopeless. So instead of hunting, this project borrows a beautiful, extremely symmetric object from pure geometry: the **Fermat quartic fourfold** — the set of solutions to

```
x₀⁴ + x₁⁴ + x₂⁴ + x₃⁴ + x₄⁴ + x₅⁴ = 0.
```

Attached to this shape is a **lattice** — think of a perfectly regular grid of points, like graph paper, but living in many dimensions and not necessarily square. This particular lattice (the project calls it `V(4,4)-prim`) lives in **141 dimensions**, and it inherits the exquisite symmetry of the equation. The idea: carve a **128-dimensional slice** out of this 141-dimensional grid — a slice chosen so that it is an even *denser* packing than MW128.

## A few words, so the rest reads easily

- **Lattice** — a regular grid of points in many dimensions.
- **Minimum** — the distance between the two closest points of the grid. A bigger minimum means the balls centred on the grid can be bigger.
- **Price** — how compact the grid is. There is a tug-of-war: pushing the points apart (a big minimum) fights against keeping the grid compact (a low price). You win only when both are balanced.
- **The star** (the project's guiding image) — a real star is a balance of two opposing forces: outward pressure against inward gravity. A record-breaking packing is the same kind of balance — the minimum pushes the points apart, the price pulls them together — and it exists only at the exact equilibrium point.

## What was actually proved — each in one sentence

- **The Bridge Theorem** *(the keystone)* — two completely different ways of measuring this lattice, one from deep complex geometry (periods, Hodge theory) and one from plain counting of how flat planes cross each other, turn out to be **secretly the same measurement**. This is what turns an impossible, never-ending calculation into a finite one you can actually run.
- **The Spectrum Theorem** — the lattice's "ruler" has exactly **four** distinct readings (the numbers 240, 96, 48, 32), and which reading you get is decided entirely by the symmetry of six points. The shape of the lattice, fully mapped.
- **The Parity Theorem** — you **cannot** build the 128-dimensional slice the obvious way (by gluing the planes together): a parity rule forbids it. An honest dead end, closed with proof.
- **The Star Theorem** — the lattice has two "faces," an arithmetic one and a geometric one; the record needs both to balance at once, and the theorem pins down exactly which of the two is the hard one.
- **The Steel, Closure, and Katana results** — the toolkit: how the cutting tools behave, *why the list of cases is finite* (so a search can finish instead of running forever), and the recipe that forges the tools.

The repository also stands on a family of earlier results about Fermat **surfaces** — the *Sweet Lie, Watermark, Double Ladder, Bend, Wild Tooth* and *Three-Ring* theorems — which come from a sister project and are credited as such throughout.

## Did it beat the record?

**Not yet — and the repository says so plainly.** The attempt completely solved one half of the problem (the *price*: it is understood all the way down to a proven floor) and then hit a precise wall on the other half (the *minimum*). Crucially, that wall is now **mapped exactly**: a future attempt knows precisely what it has to overcome, and why no shortcut through the easy half can do it. Mapping an obstruction this sharply is itself a result. And the theorems above are true and useful regardless of whether the record ever falls.

## Who did this, and on what

**Rafael Amichis Luengo** — a psychologist by training and a self-taught mathematician — in Madrid, working on a single **MacBook Air** (8 GB of memory, one processor core, deliberately throttled to a quarter of its speed, never touching swap). No cluster, no cloud. Every number in every theorem is exact arithmetic and is independently checkable from the files.
