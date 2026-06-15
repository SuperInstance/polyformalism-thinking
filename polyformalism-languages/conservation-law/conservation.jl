# JULIA: What multiple dispatch reveals about conservation
# Forces you to think about: Mathematical notation IS syntax. Why should δ(n) look
#   different in code than in a paper? It shouldn't.
# Broken assumption: That scalar and vector operations are categorically different.
# Novel insight: δ.(1:100) — the dot broadcast makes "apply to all fleet sizes"
#   syntactically invisible. The fleet is an array primitive.

δ(n) = (1 / √n) * (1 - 3 / (2n))
ccr(n) = δ(n) * 100

println("    n       δ(n)     CCR%")
println("-" ^ 28)
for n in 1:100
    println(lpad(n, 5), "  ", lpad(round(δ(n), digits=6), 10), "  ", lpad(round(ccr(n), digits=2), 7), "%")
end
