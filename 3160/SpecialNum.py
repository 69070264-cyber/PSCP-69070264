"""UareSpicial"""
F, T = map(int, input().split())
primes = []
for i in range(F, T + 1):
    if i < 2:
        continue
    is_prime = True
    for U in range(2, int(i ** 0.5) + 1):
        if not i % U:
            is_prime = False
            break
    if is_prime:
        primes.append(str(i))

if primes:
    print(" ".join(primes))
print(f"Total primes: {len(primes)}")
