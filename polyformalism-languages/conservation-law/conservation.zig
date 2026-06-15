// ZIG: What memory layout reveals about conservation
// Forces you to think about: Integer types, exact width, explicit conversion.
//   u32 for counting, f64 for computing — these are different mathematical objects.
// Broken assumption: That domain violations (n=0) are runtime problems.
//   Zig forces confronting the mathematical domain at the type level.
// Novel insight: comptime vs runtime — the domain of δ(n) can be checked at compile time.

const std = @import("std");
const math = std.math;

fn delta(n: f64) f64 {
    return (1.0 / math.sqrt(n)) * (1.0 - 3.0 / (2.0 * n));
}

pub fn main() void {
    std.debug.print("    n       δ(n)     CCR%\n", .{});
    std.debug.print("{s}\n", .{"-" ** 28});
    var i: u32 = 1;
    while (i <= 100) : (i += 1) {
        const d = delta(@floatFromInt(i));
        std.debug.print("{d:>5}  {d:>10.6}  {d:>7.2}%\n", .{ i, d, d * 100.0 });
    }
}
