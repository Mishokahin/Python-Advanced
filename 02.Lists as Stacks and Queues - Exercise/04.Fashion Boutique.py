box = list(map(int, input().split()))
capacity = int(input())
temp = 0
racks = 1

while box:
    if temp + box[-1] <= capacity:
        temp += box.pop()
    else:
        racks += 1
        temp = 0

print(racks)