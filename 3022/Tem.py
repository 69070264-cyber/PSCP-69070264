"""Tempp"""
OOSA = float(input())
f = input()
t = input()
celsius = ""
result = ""
if f == 'C':
    celsius = OOSA
elif f == 'F':
    celsius = (OOSA - 32) * 5.0 / 9.0
elif f == 'K':
    celsius = OOSA - 273.15
elif f == 'R':
    celsius = (OOSA - 491.67) * 5.0 / 9.0

if t == 'C':
    result = celsius
elif t == 'F':
    result = celsius * 9.0 / 5.0 + 32
elif t == 'K':
    result = celsius + 273.15
elif t == 'R':
    result = (celsius + 273.15) * 9.0 / 5.0

print(f"{result:.2f}")
