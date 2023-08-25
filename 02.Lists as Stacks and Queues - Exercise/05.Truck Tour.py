from collections import deque

n = int(input().strip())
res = 0
tank = 0
q = deque()

for ind in range(n):
    petr, dist = [int(arg) for arg in input().strip().split()]
    tank += petr

    if dist <= tank:
        tank -= dist
    else:
        tank = 0
        res = ind + 1

    q.append((petr, dist))

print(res)