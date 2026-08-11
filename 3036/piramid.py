"""Piramid"""
import math
room = int(input())
row = math.isqrt(room)
if row * row < room:
    row += 1

pos = room - ((row-1)**2)
if pos % 2:
    print(2*(row-1))
else:
    print((2*(row-1))-1)
