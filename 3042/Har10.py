"""HaHa10"""
num = int(input())
st = num - (num % 10)
result = [str(i) for i in range(st, -1, -10)]
print(" ".join(result))
