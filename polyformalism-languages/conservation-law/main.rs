// RUST: What ownership reveals about conservation
// Forces you to think about: Who owns n? The lifecycle of every value.
// Broken assumption: That math is "safe by default" — f64 vs f32 is explicit.
// Novel insight: Conservation law's zero-leak property mirrors ownership —
//   coupling cost is memory you can't borrow for free.

fn compute_delta(n: f64) -> f64 {
    (1.0 / n.sqrt()) * (1.0 - 3.0 / (2.0 * n))
}

fn compute_ccr(n: f64) -> f64 {
    compute_delta(n) * 100.0
}

fn main() {
    println!("{:>5}  {:>10}  {:>8}", "n", "δ(n)", "CCR%");
    println!("{}", "-".repeat(28));
    for n in 1..=100 {
        println!("{:>5}  {:>10.6}  {:>7.2}%", n, compute_delta(n as f64), compute_ccr(n as f64));
    }
}
