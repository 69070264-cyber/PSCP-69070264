"""Brickback"""
a = int(input())
b = int(input())
goal = int(input())
Bink = goal // (b*5)
Breal = min(b,Bink)
goal -= Breal * 5
if goal <= a:
    print(goal)
else:
    print(-1)
