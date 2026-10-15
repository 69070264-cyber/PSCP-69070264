"""Sgodaw"""
nums = []
while True:
    n = int(input())
    if n == -1:
        break
    nums.append(n)

parts = []
if nums:
    start = prev = nums[0]
    for n in nums[1:]:
        if n == prev + 1:
            prev = n
        else:
            parts.append(f"{start}-{prev}" if start != prev else str(start))
            start = prev = n
    parts.append(f"{start}-{prev}" if start != prev else str(start))

print(", ".join(parts))
