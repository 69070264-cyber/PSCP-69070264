"""Thief"""
N,K,T = map(int,input().split())
count = 0
check = 1
if T == 1:
    print("1")
else:
    while True:
        check += K
        while check > N:
            check %= N
        if not check:
            check = N
        if check == 1:
            break
        if check == T:
            count += 1
            break
        count += 1
    print(count+1)
