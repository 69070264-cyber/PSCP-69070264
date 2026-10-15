"""Whostealeat"""
Many = int(input())
allTall = []
for _ in range(Many):
    allTall.append(int(input()))

TallCount = 0
for i in range(Many):
    left_ok = (not i) or (allTall[i] > allTall[i-1])
    right_ok = (i == Many - 1) or (allTall[i] > allTall[i+1])
    if left_ok and right_ok:
        TallCount += 1

print(TallCount)
