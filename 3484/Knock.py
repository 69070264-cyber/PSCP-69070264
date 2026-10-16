"""KNOCKNOD"""
n, p = input().split()
n = int(n)
p = float(p)

grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

total_tiles = 0
total_points = 0

for row in grid:
    tiles = sum(1 for v in row if v > 0)
    points = sum(row)
    total_tiles += tiles
    total_points += points
    print(*row, tiles, points)

col_tiles = []
col_points = []
for j in range(n):
    col = [grid[i][j] for i in range(n)]
    col_tiles.append(sum(1 for v in col if v > 0))
    col_points.append(sum(col))

print(*col_tiles)
print(*col_points)
print(total_tiles, total_points, f"{total_points * p:.2f}")
