"""WhyWecutthisThing"""
W, H, M, N = map(int, input().split())
M += 0
N += 0
xs = [0] + list(map(int, input().split())) + [W]
ys = [0] + list(map(int, input().split())) + [H]

widths  = [xs[i+1] - xs[i] for i in range(len(xs) - 1)]
heights = [ys[i+1] - ys[i] for i in range(len(ys) - 1)]

areas = []
for w in widths:
    for h in heights:
        areas.append(w * h)

areas.sort(reverse=True)
print(areas[0], areas[1])
