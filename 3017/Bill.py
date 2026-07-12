"""Bill"""
def bined():
    """billdef"""
    fooddrink = float(input())
    service = fooddrink*0.1
    if service < 50:
        service = 50
    elif service > 1000:
        service = 1000

    vat = (fooddrink+service)*0.07
    print(f"{fooddrink+service+vat:.2f}")

bined()
