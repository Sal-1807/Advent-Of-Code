#!/usr/bin/env python3
import re
from collections import deque
from random import randrange, random
from time import time

INPUT = "data.txt"


def popcount(x):
    return x.bit_count()


line_re = re.compile(r'^\s*(\[[.#]+\])\s*((?:\([0-9,]*\)\s*)+)\s*(\{.*\})?\s*$')

def parse_line(line):
    m = line_re.match(line)
    if not m:
        raise ValueError("Bad line format: " + line)
    lights_descr = m.group(1)  
    buttons_part = m.group(2)  
    lights = lights_descr.strip()[1:-1]
    target = [1 if c == '#' else 0 for c in lights]
    
    buttons = []
    for b in re.finditer(r'\(([0-9,]*)\)', buttons_part):
        s = b.group(1).strip()
        if s == "":
            idxs = []
        else:
            idxs = [int(x) for x in s.split(',') if x != ""]
        buttons.append(idxs)
    return target, buttons


def solve_gf2_minweight(A_rows, b_bits, m_vars):
  
    n = len(A_rows)
    A = A_rows[:]  # copy
    b = b_bits[:]
    where = [-1] * m_vars  
    row = 0
    for col in range(m_vars):
        
        sel = None
        for r in range(row, n):
            if (A[r] >> col) & 1:
                sel = r
                break
        if sel is None:
            continue
        
        A[row], A[sel] = A[sel], A[row]
        b[row], b[sel] = b[sel], b[row]
        where[col] = row
       
        for r in range(n):
            if r != row and ((A[r] >> col) & 1):
                A[r] ^= A[row]
                b[r] ^= b[row]
        row += 1
        if row == n:
            break
   
    for r in range(row, n):
        if A[r] == 0 and b[r]:
            return None  

    
    x0 = 0
    for col in range(m_vars):
        if where[col] != -1:
            if b[where[col]]:  
                x0 |= (1 << col)

    
    basis = []
    pivot_for_row = {}
    for col, r in enumerate(where):
        if r != -1:
            pivot_for_row[r] = col

    for free_col in range(m_vars):
        if where[free_col] == -1:
            vec = 1 << free_col
            
            for r in range(row):
                pivot_col = pivot_for_row.get(r, None)
                if pivot_col is not None:
                    
                    if (A[r] >> free_col) & 1:
                        vec |= (1 << pivot_col)
            basis.append(vec)

    return x0, basis


def min_weight_from_basis(x0, basis, limit=22, time_limit=0.5):
    k = len(basis)
    if k == 0:
        return popcount(x0)
    if k <= limit:
        best = None
        
        for mask in range(1 << k):
            x = x0
            i = 0
            mm = mask
            while mm:
                lsb = mm & -mm
                idx = (lsb.bit_length() - 1)
                x ^= basis[idx]
                mm ^= lsb
            w = popcount(x)
            if best is None or w < best:
                best = w
        return best
    
    start = time()
    best = popcount(x0)
    
    B = basis
    while time() - start < time_limit:
        x = x0
        mask = 0
        for i in range(k):
            if randrange(2):
                x ^= B[i]
                mask |= (1 << i)
        w = popcount(x)
        if w < best:
            best = w
        improved = True
        attempts = 0
        while improved and (time() - start) < time_limit and attempts < 200:
            improved = False
            attempts += 1
            for i in range(k):
                x2 = x ^ B[i]
                w2 = popcount(x2)
                if w2 < w:
                    x = x2
                    w = w2
                    mask ^= (1 << i)
                    improved = True
                    if w < best:
                        best = w
            if not improved and random() < 0.05:
                i = randrange(k)
                x ^= B[i]
                mask ^= (1 << i)
                w = popcount(x)
                if w < best:
                    best = w
    return best


per_line = []
lines = [L.rstrip("\n") for L in open(INPUT, "r") if L.strip()]
t0 = time()
for idx, L in enumerate(lines):
    target, buttons = parse_line(L)
    n_lights = len(target)
    m_buttons = len(buttons)
    A_rows = [0] * n_lights
    for j, btn in enumerate(buttons):
        for i in btn:
            if 0 <= i < n_lights:
                A_rows[i] |= (1 << j)
    b_bits = target[:]  
    sol = solve_gf2_minweight(A_rows, b_bits, m_buttons)
    if sol is None:
        raise RuntimeError(f"No solution for line {idx+1}: {L}")
    x0, basis = sol
    best = min_weight_from_basis(x0, basis, limit=22, time_limit=0.3)
    total += best
    per_line.append(best)

for i, v in enumerate(per_line, 1):
    print(f"line {i}: {v}")
print("total:", total)
print(f"elapsed: {time()-t0:.3f}s")
