"""Sirpiece"""
S = float(input())
M = float(input())

cmin = max(0.0, S - (2 * M))

if cmin < M - 2:
    print("Surprising")
else:
    print("Not surprising")
