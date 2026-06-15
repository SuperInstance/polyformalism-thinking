⍝ APL: What array thinking reveals about conservation
⍝ Forces you to think about: Rank. Shape. Everything is an array.
⍝   The function DELTA doesn't take a number — it takes an array of numbers.
⍝ Broken assumption: That iteration is sequential. The entire n=1..100 table
⍝   is one expression. There are no agents, only shapes.
⍝ Novel insight: The conservation law is INHERENTLY PARALLEL. Computing
⍝   δ(1), δ(2), ..., δ(100) are independent operations that happen at once.
⍝   The fleet is a rank-1 array.

⍝ Run with: apl -f conservation.apl
⍝ Or tryapl.org

DELTA ← {(÷√⍵)×1-3÷2×⍵}
CCR ← {100×DELTA ⍵}

⍝ Table: n, δ(n), CCR%
N ← ⍳100
D ← DELTA N
C ← CCR N

⍝ Display (transposed for readability)
⎕←3 100⍴N,D,C

⍝ Key insight: the entire fleet computation is ONE expression.
⍝ No loops. No iteration. The array IS the computation.
