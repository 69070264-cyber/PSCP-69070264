"""ScoreGame"""
N = int(input())
Score = 0
for _ in range(N):
    Op = input()
    if Op == "+":
        Score += 10
    else:
        Score -= 5

print(Score)
