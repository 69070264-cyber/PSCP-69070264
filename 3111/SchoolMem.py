"""Sahakon"""
from decimal import Decimal, ROUND_HALF_UP

Member = input()
N = int(input())
total = Decimal("0")
for _ in range(N):
    Price = Decimal(input())
    total += Price

if Member == "Y":
    total *= Decimal("0.95")
else:
    if total >= 500:
        total *= Decimal("0.97")

total = total.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
print(total)
