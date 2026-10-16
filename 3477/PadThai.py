"""ThaiPad"""
recipe = {
    "Pad Thai Sauce", "Tofu", "Pickle Turnip", "Shrimp",
    "Bean Sprouts", "Noodle", "Chives", "Lime",
    "Egg", "Oil", "Peanuts",
}

used = set()
while True:
    line = input().strip()
    if line == "Cook":
        break
    used.add(line)

tastes = set()
while True:
    line = input().strip()
    if line == "End":
        break
    tastes.add(line)

if used - recipe:
    print("This is not Pad Thai!!!")
elif recipe - used:
    print("This is bad!")
elif tastes != {"Sweet", "Sour", "Salty"}:
    print("Not Bad...")
else:
    print("Delicious!")
