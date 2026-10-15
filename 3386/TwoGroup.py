"""2NM"""
FGall = int(input())
SGall = int(input())

FG = []
for _ in range(FGall):
    FG.append(int(input()))

SG = []
for _ in range(SGall):
    SG.append(int(input()))

common = []
for x in FG:
    if x in SG and x not in common:
        common.append(x)

if common:
    common.sort(reverse=True)
    for x in common:
        print(x)
else:
    print("Nope")
