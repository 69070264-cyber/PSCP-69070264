"""Thunder"""
From,To = input().split()
Kg = float(input())
if From == "BKK" and To == "CNX":
    print(f"{10 + (Kg * 30):.2f}")
elif From == "CNX" and To == "UBP":
    print(f"{15 + (Kg * 40):.2f}")
elif From == "UBP" and To == "BKK":
    print(f"{20 + (Kg * 40):.2f}")
elif From == "BKK" and To == "PKT":
    print(f"{25 + (Kg * 50):.2f}")
elif From == "PKT" and To == "CNX":
    print(f"{30 + (Kg * 60):.2f}")
elif From == "UBP" and To == "PKT":
    print(f"{40 + (Kg * 70):.2f}")
else:
    print("Error")
