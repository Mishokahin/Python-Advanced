count = int(input())
unique_names = set()

for _ in range(count):
    unique_names.add(input())

print("\n".join(unique_names))