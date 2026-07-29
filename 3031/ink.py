"""inggg"""
import math

S,N = map(int, input().split())
result = []
for i in range(N):
    i += 0
    x, y = map(int, input().split())
    distance = (x**2)+(y**2)
    area = 3.1416 * distance
    time = area / S
    result.append(math.ceil(time))
for ans in result:
    print(ans)
