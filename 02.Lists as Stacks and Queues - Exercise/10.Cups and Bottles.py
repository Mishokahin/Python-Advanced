from collections import deque

cups = deque(map(int, input().split()))
bottles = deque(map(int, input().split()))
wasted_water = 0

while cups and bottles:
    current_cup = cups.popleft()
    current_bottle = bottles.pop()

    if current_cup - current_bottle <= 0:
        wasted_water += abs(current_cup - current_bottle)

    else:
        cups.appendleft(abs(current_cup - current_bottle))

if cups:
    print(f"Cups: {' '.join(map(str, cups))}")
else:
    print(f"Bottles: {' '.join(map(str, bottles))}")

print(f"Wasted litters of water: {wasted_water}")