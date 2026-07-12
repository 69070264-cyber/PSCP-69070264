"""666"""


def main():
    """color"""
    color1 = input()
    color2 = input()

    primary_colors = ["Red", "Yellow", "Blue"]

    if color1 not in primary_colors or color2 not in primary_colors:
        print("Error")

    elif color1 == color2:
        print(color1)

    elif (color1 == "Red" and color2 == "Yellow") or (color1 == "Yellow" and color2 == "Red"):
        print("Orange")
    elif (color1 == "Red" and color2 == "Blue") or (color1 == "Blue" and color2 == "Red"):
        print("Violet")
    elif (color1 == "Yellow" and color2 == "Blue") or (color1 == "Blue" and color2 == "Yellow"):
        print("Green")
    else:
        print("Error")

main()
