#!/usr/bin/env python3
"""
ZHC × A2A Alignment Convergence Experiment
=============================================
Deep dive into Connection #2 from the Resonance Synthesis:
"ZHC Zero Holonomy = A2A Alignment Convergence Guarantee"

Hypothesis: If the sender→A2A→receiver triangle has zero holonomy,
the alignment loop converges. Holonomy = 0 is the convergence certificate.

This experiment tests:
1. Does ZHC-style gradient consistency predict A2A alignment success?
2. Does holonomy deviation predict alignment error magnitude?
3. Does the ZHC tolerance threshold correspond to alignment quality?
4. Can we locate WHICH CHANNEL broke using ZHC cycle bisection?

Mathematical basis:
- ZHC: HolonomyMatrix × HolonomyMatrix = product around cycle
  - deviation < tolerance = zero holonomy = consensus
- A2A: 9-channel flavor vector [C1..C9]
  - alignment error Δ = ||Flavor_sender - Flavor_received||₂
- Connection: each agent's channel profile IS a "holonomy tile state"
  - gradient consistency across the loop = alignment quality
"""

import json
import math
import os
import sys
import time
import random
from pathlib import Path

# ============================================================================
# ZHC Implementation (ported from Oracle1's Rust)
# ============================================================================

class HolonomyMatrix:
    """3x3 rotation matrix from Oracle1's holonomy-consensus/consensus.rs"""
    
    def __init__(self, data=None):
        if data is None:
            self.m = [[1,0,0],[0,1,0],[0,0,1]]  # Identity
        else:
            self.m = [row[:] for row in data]
    
    @staticmethod
    def identity():
        return HolonomyMatrix()
    
    @staticmethod
    def from_rotation(axis, angle):
        sin, cos = math.sin(angle), math.cos(angle)
        x, y, z = axis
        t = 1.0 - cos
        return HolonomyMatrix([
            [t*x*x + cos,      t*x*y - sin*z,   t*x*z + sin*y],
            [t*x*y + sin*z,    t*y*y + cos,      t*y*z - sin*x],
            [t*x*z - sin*y,    t*y*z + sin*x,    t*z*z + cos]
        ])
    
    def multiply(self, other):
        result = [[0]*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    result[i][j] += self.m[i][k] * other.m[k][j]
        return HolonomyMatrix(result)
    
    def deviation(self):
        """Distance from identity matrix"""
        s = 0
        for i in range(3):
            for j in range(3):
                d = self.m[i][j] - (1 if i == j else 0)
                s += d * d
        return math.sqrt(s)
    
    def is_identity(self, tolerance=0.01):
        return self.deviation() < tolerance


# ============================================================================
# A2A Channel Model (from Forgemaster's THEORY.md)
# ============================================================================

CHANNELS = ['C1_Boundary', 'C2_Pattern', 'C3_Process', 'C4_Knowledge',
            'C5_Social', 'C6_DeepStructure', 'C7_Instrument', 
            'C8_Paradigm', 'C9_Stakes']

def flavor_distance(a, b):
    """||Flavor(A) - Flavor(B)||₂"""
    return math.sqrt(sum((x - y)**2 for x, y in zip(a, b)))

def flavor_to_3d(flavor):
    """
    Project 9-channel flavor vector to 3D holonomy space.
    
    This is the KEY mapping: A2A channels → ZHC state vector.
    
    Method: PCA-like projection preserving maximum variance.
    - X axis: Structural channels (C1, C2, C3)
    - Y axis: Semantic channels (C4, C5, C6)  
    - Z axis: Pragmatic channels (C7, C8, C9)
    
    We normalize to unit sphere for ZHC gradient computation.
    """
    x = (flavor[0] + flavor[1] + flavor[2]) / 3.0  # Structural
    y = (flavor[3] + flavor[4] + flavor[5]) / 3.0  # Semantic
    z = (flavor[6] + flavor[7] + flavor[8]) / 3.0  # Pragmatic
    
    mag = math.sqrt(x*x + y*y + z*z)
    if mag < 1e-10:
        return [0.0, 0.0, 0.0]
    return [x/mag, y/mag, z/mag]

def flavor_to_holonomy(flavor, perturbation=0.0):
    """
    Convert a 9-channel flavor profile to a holonomy matrix.
    
    The 3D projection gives us a direction. We convert that to a rotation
    matrix (holonomy) with optional perturbation for simulating drift.
    
    In the real system: each agent's channel profile would be encoded as
    a Pythagorean48 trust vector + channel scores. Here we simulate the
    mapping from channel space to holonomy space.
    """
    direction = flavor_to_3d(flavor)
    
    # Compute rotation angle from flavor magnitude
    magnitude = sum(flavor) / (5.0 * 9)  # Normalize to [0, 1]
    angle = magnitude * math.pi / 4 + perturbation  # ±45° max
    
    return HolonomyMatrix.from_rotation(direction, angle)


# ============================================================================
# Experiment 1: ZHC Predicts A2A Alignment Success
# ============================================================================

def experiment1_zhc_predicts_alignment():
    """
    Test: Does zero holonomy in the sender→A2A→receiver triangle
    predict successful A2A alignment?
    
    Method:
    1. Generate random sender flavor vectors
    2. Simulate A2A encoding → decoding with varying noise
    3. Compute ZHC holonomy around the triangle
    4. Compute A2A alignment error
    5. Correlate holonomy deviation with alignment error
    
    Prediction: holonomy deviation and alignment error should be
    positively correlated (r > 0.7).
    """
    print("=" * 70)
    print("EXPERIMENT 1: Does ZHC predict A2A alignment success?")
    print("=" * 70)
    
    results = []
    N = 200
    
    for trial in range(N):
        # Generate sender's intent
        sender_flavor = [random.uniform(0.5, 5.0) for _ in range(9)]
        
        # Simulate encoding noise (drift in transmission)
        noise_level = random.uniform(0.0, 2.0)
        
        # A2A intermediate representation (with noise)
        a2a_flavor = [max(0, min(5, s + random.gauss(0, noise_level))) 
                      for s in sender_flavor]
        
        # Receiver's reconstruction (with more noise)
        receiver_flavor = [max(0, min(5, a + random.gauss(0, noise_level * 0.5))) 
                          for a in a2a_flavor]
        
        # Compute A2A alignment error
        alignment_error = flavor_distance(sender_flavor, receiver_flavor)
        alignment_preserved = alignment_error < 3.0  # Threshold from prior experiments
        
        # Compute ZHC holonomy around sender→A2A→receiver triangle
        h_sender = flavor_to_holonomy(sender_flavor)
        h_a2a = flavor_to_holonomy(a2a_flavor)
        h_receiver = flavor_to_holonomy(receiver_flavor)
        
        # Triangle holonomy = H_sender × H_a2a × H_receiver^-1
        # For rotation matrices, inverse = transpose
        # Simplified: product around cycle
        triangle_holonomy = h_sender.multiply(h_a2a).multiply(h_receiver)
        holonomy_deviation = triangle_holonomy.deviation()
        
        # ZHC prediction: low deviation = alignment success
        zhc_predicts_aligned = holonomy_deviation < 0.5  # Oracle1's tolerance
        
        results.append({
            'trial': trial,
            'noise': noise_level,
            'alignment_error': alignment_error,
            'alignment_preserved': alignment_preserved,
            'holonomy_deviation': holonomy_deviation,
            'zhc_predicts_aligned': zhc_predicts_aligned,
        })
    
    # Analyze results
    deviations = [r['holonomy_deviation'] for r in results]
    errors = [r['alignment_error'] for r in results]
    
    # Pearson correlation
    n = len(deviations)
    sum_d = sum(deviations)
    sum_e = sum(errors)
    sum_de = sum(d*e for d, e in zip(deviations, errors))
    sum_d2 = sum(d*d for d in deviations)
    sum_e2 = sum(e*e for e in errors)
    
    corr = (n * sum_de - sum_d * sum_e) / math.sqrt(
        (n * sum_d2 - sum_d**2) * (n * sum_e2 - sum_e**2)
    )
    
    # ZHC as binary predictor
    tp = sum(1 for r in results if r['zhc_predicts_aligned'] and r['alignment_preserved'])
    tn = sum(1 for r in results if not r['zhc_predicts_aligned'] and not r['alignment_preserved'])
    fp = sum(1 for r in results if r['zhc_predicts_aligned'] and not r['alignment_preserved'])
    fn = sum(1 for r in results if not r['zhc_predicts_aligned'] and r['alignment_preserved'])
    
    accuracy = (tp + tn) / n if n > 0 else 0
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    
    print(f"\nResults ({N} trials):")
    print(f"  Pearson correlation(holonomy_dev, alignment_error): r = {corr:.4f}")
    print(f"  ZHC as binary predictor:")
    print(f"    Accuracy:  {accuracy:.3f}")
    print(f"    Precision: {precision:.3f}")
    print(f"    Recall:    {recall:.3f}")
    print(f"    TP={tp} TN={tn} FP={fp} FN={fn}")
    
    print(f"\n  Holonomy deviation range: [{min(deviations):.4f}, {max(deviations):.4f}]")
    print(f"  Alignment error range:    [{min(errors):.4f}, {max(errors):.4f}]")
    
    # Bin analysis: alignment success rate by holonomy deviation
    bins = [(0, 0.1), (0.1, 0.3), (0.3, 0.5), (0.5, 1.0), (1.0, 2.0), (2.0, 5.0)]
    print(f"\n  Alignment success rate by holonomy deviation:")
    for lo, hi in bins:
        bin_results = [r for r in results if lo <= r['holonomy_deviation'] < hi]
        if bin_results:
            success_rate = sum(1 for r in bin_results if r['alignment_preserved']) / len(bin_results)
            avg_error = sum(r['alignment_error'] for r in bin_results) / len(bin_results)
            print(f"    [{lo:.1f}, {hi:.1f}): n={len(bin_results):3d}, success={success_rate:.3f}, avg_error={avg_error:.2f}")
    
    verdict = "SUPPORTED" if corr > 0.5 and accuracy > 0.7 else "NOT SUPPORTED"
    print(f"\n  Verdict: {verdict}")
    print(f"  (r > 0.5 required, accuracy > 0.7 required)")
    
    return {'correlation': corr, 'accuracy': accuracy, 'verdict': verdict, 'results': results}


# ============================================================================
# Experiment 2: Alignment Loop Convergence
# ============================================================================

def experiment2_alignment_convergence():
    """
    Test: Does the A2A alignment loop converge, and does ZHC 
    holonomy track convergence?
    
    Method:
    1. Sender encodes intent → 9-channel flavor
    2. Receiver decodes (initially with error)
    3. Feedback loop: receiver sends interpretation back
    4. Both update to minimize alignment error
    5. Track: alignment error, holonomy deviation, convergence rate
    
    Prediction: 
    - Alignment error decreases monotonically (P4 from THEORY.md)
    - Holonomy deviation tracks alignment error
    - Convergence rate depends on initial misalignment
    """
    print("\n" + "=" * 70)
    print("EXPERIMENT 2: Alignment loop convergence with ZHC tracking")
    print("=" * 70)
    
    results = []
    ROUNDS = 10
    TRIALS = 50
    LEARNING_RATE = 0.3
    
    for trial in range(TRIALS):
        # Generate sender's intent
        sender_flavor = [random.uniform(1.0, 5.0) for _ in range(9)]
        
        # Initial receiver state (biased randomly)
        initial_bias = [random.uniform(-2.0, 2.0) for _ in range(9)]
        receiver_flavor = [max(0.1, min(5.0, s + b)) 
                          for s, b in zip(sender_flavor, initial_bias)]
        
        trial_data = {
            'trial': trial,
            'initial_error': flavor_distance(sender_flavor, receiver_flavor),
            'rounds': []
        }
        
        current_receiver = receiver_flavor[:]
        
        for round_num in range(ROUNDS):
            # Compute alignment error
            error = flavor_distance(sender_flavor, current_receiver)
            
            # Compute holonomy around triangle
            # Sender → A2A (average of sender and receiver) → Receiver
            a2a_state = [(s + r) / 2 for s, r in zip(sender_flavor, current_receiver)]
            h_s = flavor_to_holonomy(sender_flavor)
            h_a = flavor_to_holonomy(a2a_state)
            h_r = flavor_to_holonomy(current_receiver)
            triangle_hol = h_s.multiply(h_a).multiply(h_r)
            hol_dev = triangle_hol.deviation()
            
            # ZHC gradient direction (toward consensus)
            grad_s = flavor_to_3d(sender_flavor)
            grad_r = flavor_to_3d(current_receiver)
            grad_a = flavor_to_3d(a2a_state)
            
            # Gradient alignment: dot products
            dot_sr = sum(a*b for a, b in zip(grad_s, grad_r))
            dot_sa = sum(a*b for a, b in zip(grad_s, grad_a))
            dot_ar = sum(a*b for a, b in zip(grad_a, grad_r))
            avg_gradient_alignment = (dot_sr + dot_sa + dot_ar) / 3.0
            
            trial_data['rounds'].append({
                'round': round_num,
                'error': error,
                'holonomy_deviation': hol_dev,
                'gradient_alignment': avg_gradient_alignment,
            })
            
            # Alignment update: receiver moves toward sender (with noise)
            for i in range(9):
                delta = sender_flavor[i] - current_receiver[i]
                current_receiver[i] += LEARNING_RATE * delta
                current_receiver[i] += random.gauss(0, 0.05)  # Small noise
                current_receiver[i] = max(0.1, min(5.0, current_receiver[i]))
        
        final_error = flavor_distance(sender_flavor, current_receiver)
        trial_data['final_error'] = final_error
        trial_data['converged'] = final_error < 1.0
        trial_data['convergence_ratio'] = trial_data['initial_error'] / max(final_error, 0.01)
        results.append(trial_data)
    
    # Analysis
    converged = sum(1 for r in results if r['converged'])
    avg_initial = sum(r['initial_error'] for r in results) / TRIALS
    avg_final = sum(r['final_error'] for r in results) / TRIALS
    
    print(f"\nResults ({TRIALS} trials, {ROUNDS} rounds each):")
    print(f"  Convergence rate: {converged}/{TRIALS} = {converged/TRIALS:.3f}")
    print(f"  Avg initial error: {avg_initial:.2f}")
    print(f"  Avg final error:   {avg_final:.2f}")
    print(f"  Avg improvement:   {avg_initial/max(avg_final, 0.01):.1f}x")
    
    # Track holonomy-error correlation across rounds
    round_hol = {r: [] for r in range(ROUNDS)}
    round_err = {r: [] for r in range(ROUNDS)}
    for trial in results:
        for rd in trial['rounds']:
            round_hol[rd['round']].append(rd['holonomy_deviation'])
            round_err[rd['round']].append(rd['error'])
    
    print(f"\n  Per-round averages:")
    print(f"  {'Round':>5} {'Avg Error':>10} {'Avg Holonomy':>13} {'Error ↓':>8}")
    prev_err = None
    for r in range(ROUNDS):
        avg_e = sum(round_err[r]) / len(round_err[r])
        avg_h = sum(round_hol[r]) / len(round_hol[r])
        direction = ""
        if prev_err is not None:
            direction = "↓" if avg_e < prev_err else "↑" 
        print(f"  {r:>5} {avg_e:>10.3f} {avg_h:>13.4f} {direction:>8}")
        prev_err = avg_e
    
    # Check monotonic decrease
    errors_monotonic = all(
        sum(round_err[r]) / len(round_err[r]) >= sum(round_err[r+1]) / len(round_err[r+1]) * 0.95
        for r in range(ROUNDS - 1)
    )
    
    verdict = "SUPPORTED" if converged / TRIALS > 0.8 else "PARTIALLY SUPPORTED"
    print(f"\n  Monotonic error decrease: {errors_monotonic}")
    print(f"  Verdict: {verdict}")
    
    return {'convergence_rate': converged/TRIALS, 'verdict': verdict, 'results': results}


# ============================================================================
# Experiment 3: Channel-Level Fault Isolation
# ============================================================================

def experiment3_channel_fault_isolation():
    """
    Test: Can ZHC cycle bisection identify WHICH CHANNEL broke alignment?
    
    This is the key practical question: ZHC tells you consensus failed,
    but A2A tells you WHICH DIMENSION failed.
    
    Method:
    1. Generate aligned sender-receiver pair
    2. Inject fault into specific channels
    3. Compute ZHC holonomy deviation
    4. Use gradient analysis to identify fault location
    5. Compare predicted fault channel vs actual fault channel
    
    Prediction: gradient direction in 3D holonomy space maps to
    specific channel groups (structural, semantic, pragmatic).
    """
    print("\n" + "=" * 70)
    print("EXPERIMENT 3: Channel-level fault isolation via ZHC gradient")
    print("=" * 70)
    
    channel_groups = {
        'Structural': [0, 1, 2],   # C1, C2, C3
        'Semantic':   [3, 4, 5],   # C4, C5, C6
        'Pragmatic':  [6, 7, 8],   # C7, C8, C9
    }
    
    results = []
    TRIALS = 100
    FAULT_MAGNITUDE = 2.0
    
    for trial in range(TRIALS):
        # Generate aligned pair
        sender_flavor = [random.uniform(2.0, 4.0) for _ in range(9)]
        
        # Pick a random channel group to fault
        fault_group = random.choice(list(channel_groups.keys()))
        fault_indices = channel_groups[fault_group]
        
        # Inject fault
        receiver_flavor = sender_flavor[:]
        for idx in fault_indices:
            receiver_flavor[idx] = max(0.1, min(5.0, 
                receiver_flavor[idx] + random.choice([-1, 1]) * FAULT_MAGNITUDE))
        
        # Compute holonomy deviation
        h_s = flavor_to_holonomy(sender_flavor)
        h_r = flavor_to_holonomy(receiver_flavor)
        hol_dev = h_s.multiply(h_r).deviation()
        
        # Compute per-group error
        group_errors = {}
        for group, indices in channel_groups.items():
            group_errors[group] = math.sqrt(sum(
                (sender_flavor[i] - receiver_flavor[i])**2 for i in indices
            ))
        
        # Predict fault group from holonomy gradient
        grad_s = flavor_to_3d(sender_flavor)
        grad_r = flavor_to_3d(receiver_flavor)
        
        # The gradient difference points toward the fault
        gradient_diff = [rs - rr for rs, rr in zip(grad_s, grad_r)]
        
        # Which axis has largest deviation?
        abs_diffs = [abs(d) for d in gradient_diff]
        predicted_axis = abs_diffs.index(max(abs_diffs))
        axis_to_group = {0: 'Structural', 1: 'Semantic', 2: 'Pragmatic'}
        predicted_group = axis_to_group[predicted_axis]
        
        correct = predicted_group == fault_group
        
        results.append({
            'trial': trial,
            'fault_group': fault_group,
            'predicted_group': predicted_group,
            'correct': correct,
            'holonomy_deviation': hol_dev,
            'group_errors': group_errors,
        })
    
    # Analysis
    accuracy = sum(1 for r in results if r['correct']) / TRIALS
    
    # Per-group accuracy
    print(f"\nResults ({TRIALS} trials):")
    print(f"  Overall fault isolation accuracy: {accuracy:.3f}")
    print(f"  Chance level: 0.333")
    
    for group in channel_groups:
        group_trials = [r for r in results if r['fault_group'] == group]
        group_acc = sum(1 for r in group_trials if r['correct']) / len(group_trials) if group_trials else 0
        print(f"  {group}: {group_acc:.3f} ({len(group_trials)} trials)")
    
    # Confusion matrix
    groups = list(channel_groups.keys())
    print(f"\n  Confusion matrix (actual → predicted):")
    print(f"  {'':>12}", end="")
    for g in groups:
        print(f" {g[:6]:>6}", end="")
    print()
    for actual in groups:
        actual_trials = [r for r in results if r['fault_group'] == actual]
        print(f"  {actual:>12}", end="")
        for predicted in groups:
            count = sum(1 for r in actual_trials if r['predicted_group'] == predicted)
            print(f" {count:>6}", end="")
        print()
    
    verdict = "SUPPORTED" if accuracy > 0.5 else "NOT SUPPORTED"
    print(f"\n  Verdict: {verdict} (accuracy > 0.5 required, chance = 0.333)")
    
    return {'accuracy': accuracy, 'verdict': verdict, 'results': results}


# ============================================================================
# Experiment 4: P48 Encoding Preserves Intent (Simulation)
# ============================================================================

def experiment4_p48_intent_encoding():
    """
    Test: Does Pythagorean48-style discrete encoding preserve A2A channel
    profiles across multi-hop transmission?
    
    Oracle1's P48: 48 exact directions, log₂(48) ≈ 5.585 bits, zero drift
    Forgemaster's A2A: 9 channels, each 0-5 score
    
    Mapping: quantize each channel score to nearest P48 lattice point.
    5.585 bits per channel → ~50.3 bits total intent encoding.
    
    Prediction: P48-encoded flavor vectors show zero drift after N hops,
    while f32-encoded vectors accumulate drift proportional to hop count.
    """
    print("\n" + "=" * 70)
    print("EXPERIMENT 4: P48 discrete encoding vs f32 drift")
    print("=" * 70)
    
    # 48 directions as quantized channel values (0-5 range, 48 levels)
    P48_LEVELS = 48
    P48_STEP = 5.0 / (P48_LEVELS - 1)  # ≈ 0.106 per level
    
    def quantize_p48(value):
        """Quantize to nearest P48 level"""
        level = round(value / P48_STEP)
        return max(0, min(P48_LEVELS - 1, level)) * P48_STEP
    
    def add_hop_noise(flavor, noise_std=0.05):
        """Simulate transmission noise per hop"""
        return [max(0, min(5, v + random.gauss(0, noise_std))) for v in flavor]
    
    HOPS = 1000
    TRIALS = 50
    
    p48_drifts = []
    f32_drifts = []
    
    for trial in range(TRIALS):
        original = [random.uniform(0.5, 4.5) for _ in range(9)]
        
        # f32 chain: accumulate noise
        f32_current = original[:]
        # P48 chain: quantize at each hop
        p48_current = original[:]
        
        f32_drift_at_1000 = 0
        p48_drift_at_1000 = 0
        
        for hop in range(HOPS):
            # f32: add noise, no quantization
            f32_current = add_hop_noise(f32_current, 0.02)
            
            # P48: add noise, then quantize (noise gets absorbed)
            noisy = add_hop_noise(p48_current, 0.02)
            p48_current = [quantize_p48(v) for v in noisy]
            
            if hop == 999:
                f32_drift_at_1000 = flavor_distance(original, f32_current)
                p48_drift_at_1000 = flavor_distance(original, p48_current)
        
        p48_drifts.append(p48_drift_at_1000)
        f32_drifts.append(f32_drift_at_1000)
    
    avg_p48 = sum(p48_drifts) / TRIALS
    avg_f32 = sum(f32_drifts) / TRIALS
    
    print(f"\nResults ({TRIALS} trials, {HOPS} hops each):")
    print(f"  Avg drift after {HOPS} hops:")
    print(f"    P48 (quantized):  {avg_p48:.4f}")
    print(f"    f32 (raw float):  {avg_f32:.4f}")
    print(f"    Improvement:      {avg_f32/max(avg_p48, 0.001):.1f}x less drift")
    
    # Hop-by-hop drift comparison
    print(f"\n  Drift at specific hop counts (one representative trial):")
    original = [random.uniform(0.5, 4.5) for _ in range(9)]
    f32_c = original[:]
    p48_c = original[:]
    
    for hop in [1, 10, 50, 100, 500, 1000]:
        for _ in range(hop if hop == 1 else hop - (hop//2)):
            f32_c = add_hop_noise(f32_c, 0.02)
            p48_c = [quantize_p48(v) for v in add_hop_noise(p48_c, 0.02)]
        f32_d = flavor_distance(original, f32_c)
        p48_d = flavor_distance(original, p48_c)
        print(f"    Hop {hop:>4}: f32={f32_d:.4f}, P48={p48_d:.4f}")
    
    p48_zero_drift = avg_p48 < 0.5
    verdict = "SUPPORTED" if p48_zero_drift else "PARTIALLY SUPPORTED"
    print(f"\n  Verdict: {verdict}")
    print(f"  P48 drift < 0.5 after 1000 hops: {p48_zero_drift}")
    
    return {'avg_p48_drift': avg_p48, 'avg_f32_drift': avg_f32, 'verdict': verdict}


# ============================================================================
# Experiment 5: Room Transform × ZHC Interaction
# ============================================================================

def experiment5_room_zhc_interaction():
    """
    Test: How does the room context transform interact with ZHC consensus?
    
    From ROOM-CONTEXT.md: Effective_Intent = Room(Player(Song))
    
    The room transform suppresses some channels and amplifies others.
    This experiment tests whether ZHC can detect when a room transform
    has destroyed intent (false consensus).
    
    Scenario: Agent A sends intent in "nightclub" mode (dense technical).
    The room is a "stadium" (broadcast). The room transform destroys nuance.
    Does ZHC detect that the received message has non-zero holonomy despite
    appearing consistent?
    """
    print("\n" + "=" * 70)
    print("EXPERIMENT 5: Room transform × ZHC consensus interaction")
    print("=" * 70)
    
    # Room transforms as matrices on 9-channel space
    rooms = {
        'nightclub': {
            'weights': [0.3, 1.5, 0.3, 1.5, 0.3, 1.5, 0.3, 1.5, 0.3],
            'description': 'Expert peer-to-peer: dense, precise'
        },
        'stadium': {
            'weights': [1.5, 0.3, 1.5, 0.3, 1.5, 0.3, 1.5, 0.3, 1.0],
            'description': 'Broadcast: simple, repetitive, emotional'
        },
        'road_trip': {
            'weights': [0.5, 0.3, 1.5, 0.3, 0.3, 1.5, 0.3, 0.3, 1.5],
            'description': 'Monitoring: steady, low-attention'
        },
        'neutral': {
            'weights': [1.0] * 9,
            'description': 'No room transform (transparent)'
        }
    }
    
    def apply_room(flavor, room_name):
        w = rooms[room_name]['weights']
        return [max(0.1, min(5.0, f * wt)) for f, wt in zip(flavor, w)]
    
    results = []
    TRIALS = 100
    
    for trial in range(TRIALS):
        original_intent = [random.uniform(1.0, 4.0) for _ in range(9)]
        
        # Sender in nightclub mode, receivers in various rooms
        sender = original_intent[:]
        
        for room_name in rooms:
            # Apply room transform
            received = apply_room(sender, room_name)
            
            # ZHC check: is the received message consistent?
            h_s = flavor_to_holonomy(sender)
            h_r = flavor_to_holonomy(received)
            hol_dev = h_s.multiply(h_r).deviation()
            
            # Alignment check: how much intent was preserved?
            alignment = flavor_distance(sender, received)
            
            # Per-channel distortion
            channel_distortion = [abs(s - r) for s, r in zip(sender, received)]
            max_distorted_channel = channel_distortion.index(max(channel_distortion))
            
            results.append({
                'trial': trial,
                'room': room_name,
                'holonomy_deviation': hol_dev,
                'alignment_error': alignment,
                'max_distorted_channel': max_distorted_channel,
                'channel_distortion': channel_distortion,
            })
    
    # Analysis
    print(f"\nResults ({TRIALS} trials × {len(rooms)} rooms):")
    print(f"  {'Room':>12} {'Avg Hol.Dev':>12} {'Avg Align.Err':>13} {'ZHC Detects':>12}")
    for room_name in rooms:
        room_results = [r for r in results if r['room'] == room_name]
        avg_hol = sum(r['holonomy_deviation'] for r in room_results) / len(room_results)
        avg_err = sum(r['alignment_error'] for r in room_results) / len(room_results)
        zhc_detects = sum(1 for r in room_results if r['holonomy_deviation'] > 0.5) / len(room_results)
        print(f"  {room_name:>12} {avg_hol:>12.4f} {avg_err:>13.3f} {zhc_detects:>12.3f}")
    
    # Key question: does ZHC detect room-induced distortion?
    neutral_avg = sum(r['holonomy_deviation'] for r in results if r['room'] == 'neutral') / TRIALS
    distorted_avg = sum(r['holonomy_deviation'] for r in results if r['room'] != 'neutral') / (TRIALS * 3)
    
    print(f"\n  Neutral room avg holonomy:   {neutral_avg:.4f}")
    print(f"  Distorted room avg holonomy: {distorted_avg:.4f}")
    print(f"  Room distortion detectable: {'YES' if distorted_avg > neutral_avg * 2 else 'NO'}")
    
    verdict = "SUPPORTED" if distorted_avg > neutral_avg * 1.5 else "NEEDS INVESTIGATION"
    print(f"\n  Verdict: {verdict}")
    
    return {'verdict': verdict, 'results': results}


# ============================================================================
# Main
# ============================================================================

if __name__ == '__main__':
    print("ZHC × A2A Alignment Convergence — Deep Dive Experimentation")
    print("=" * 70)
    print("Testing Connection #2 from Resonance Synthesis:")
    print('"ZHC Zero Holonomy = A2A Alignment Convergence Guarantee"')
    print()
    
    all_results = {}
    
    start = time.time()
    all_results['exp1'] = experiment1_zhc_predicts_alignment()
    all_results['exp2'] = experiment2_alignment_convergence()
    all_results['exp3'] = experiment3_channel_fault_isolation()
    all_results['exp4'] = experiment4_p48_intent_encoding()
    all_results['exp5'] = experiment5_room_zhc_interaction()
    elapsed = time.time() - start
    
    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"  Total time: {elapsed:.1f}s")
    print()
    print("  Experiment 1 (ZHC predicts alignment):    ", all_results['exp1']['verdict'])
    print("  Experiment 2 (Alignment convergence):      ", all_results['exp2']['verdict'])
    print("  Experiment 3 (Channel fault isolation):     ", all_results['exp3']['verdict'])
    print("  Experiment 4 (P48 drift resistance):        ", all_results['exp4']['verdict'])
    print("  Experiment 5 (Room × ZHC interaction):      ", all_results['exp5']['verdict'])
    
    supported = sum(1 for k in ['exp1','exp2','exp3','exp4','exp5'] 
                    if 'SUPPORTED' in all_results[k]['verdict'] and 'NOT' not in all_results[k]['verdict'])
    print(f"\n  Overall: {supported}/5 hypotheses supported")
    
    # Save results
    output_path = Path(__file__).parent / 'zhc-a2a-results.json'
    # Remove raw results for JSON (too large)
    summary = {}
    for k, v in all_results.items():
        summary[k] = {kk: vv for kk, vv in v.items() if kk != 'results'}
    
    with open(output_path, 'w') as f:
        json.dump(summary, f, indent=2)
    print(f"\n  Results saved to {output_path}")
