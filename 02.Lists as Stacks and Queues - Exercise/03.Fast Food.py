from collections import deque

food = int(input())

q = deque(map(int, input().split()))

print(max(q))

for customer in list(q):
    if customer > food:
        print(f"Orders left: {' '.join(map(str, q))}")
        break
    else:
        food -= q.popleft()

if len(q) == 0:
    print("Orders complete")