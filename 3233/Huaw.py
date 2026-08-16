"""Huaw"""
w_l,w_n = input().split()
my_l,my_n = input().split()
if my_l == w_l and w_n == my_n:
    print("1000000")
elif w_n == my_n:
    print("100000")
elif my_l == w_l:
    if w_n[2:] == my_n[2:]:
        print("2000")
    elif w_n[3:] == my_n[3:]:
        print("1000")
    else:
        print("20")
elif my_l != w_l:
    if w_n[2:] == my_n[2:]:
        print("200")
    elif w_n[3:] == my_n[3:]:
        print("100")
    else:
        print("0")
