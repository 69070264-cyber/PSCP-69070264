"""seasonchagee"""
mouth = int(input())
day = int(input())

if mouth in (1,2,3):
    if not mouth % 3 and day >= 21:
        print("spring")
    else:
        print("winter")
elif mouth in (4,5,6):
    if not mouth % 3 and day >= 21:
        print("summer")
    else:
        print("spring")
elif mouth in (7,8,9):
    if not mouth % 3 and day >= 21:
        print("fall")
    else:
        print("summer")
elif mouth in (10,11,12):
    if not mouth % 3 and day >= 21:
        print("winter")
    else:
        print("fall")
