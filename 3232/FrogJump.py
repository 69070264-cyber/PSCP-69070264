"""Frogjump"""
X, Y = map(int, input().split())

jumpnow = 0
step = 0

while jumpnow < Y:
    if X <= 0:
        step = -1
        break
    jumpnow += X
    step += 1
    X -= 2

print(step)
