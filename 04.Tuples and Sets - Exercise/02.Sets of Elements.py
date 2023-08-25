n, m = input().split()
set_n = set(int(input()) for _ in range(int(n)))
set_m = set(int(input()) for _ in range(int(m)))

print("\n".join(map(str, set_n.intersection(set_m))))