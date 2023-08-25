odd = set()
even = set()

for i in range(1, int(input()) + 1):
    name = sum([ord(ch) for ch in input()]) // i
    if name % 2 == 0:
        even.add(name)
    else:
        odd.add(name)

if sum(odd) == sum(even):
    print(", ".join(map(str, odd.union(even))))

elif sum(odd) > sum(even):
    print(", ".join(map(str, odd.difference(even))))

else:
    print(", ".join(map(str, odd.symmetric_difference(even))))