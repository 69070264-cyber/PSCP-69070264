"""CatFox"""
import json

animals = {}

n = int(input())
for _ in range(n):
    d = json.loads(input())
    for name, code in d.items():
        animals[code] = name

if "Cat01" not in animals and "Garfield" not in animals.values():
    animals["Cat01"] = "Garfield"
if "Fox01" not in animals and "Fubuki" not in animals.values():
    animals["Fox01"] = "Fubuki"

codes = sorted(animals, key=lambda k: (k[:3], int(k[3:])))

cats = sum(1 for k in codes if k.startswith("Cat"))
foxes = sum(1 for k in codes if k.startswith("Fox"))

print("Cat :", cats)
print("Fox :", foxes)
for cd in codes:
    print(animals[cd], ":", cd)
