"""Chainmail"""
n, s = map(int, input().split())

nxt = [0] * (n + 1)
for i in range(1, n + 1):
    nxt[i] = int(input())

visited = set()
cur = s
while cur and cur not in visited:
    visited.add(cur)
    cur = nxt[cur]

print(len(visited))
