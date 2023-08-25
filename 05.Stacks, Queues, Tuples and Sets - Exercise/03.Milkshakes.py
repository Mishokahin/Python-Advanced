from collections import deque

chocolates = deque(map(int, input().split(", ")))
milks = deque(map(int, input().split(", ")))
milkshakes = 0

while milkshakes != 5 and chocolates and milks:
    chocolate = chocolates.pop()
    milk = milks.popleft()

    if chocolate <= 0 and milk <= 0:
        continue

    elif chocolate <= 0:
        milks.appendleft(milk)
        continue

    elif milk <= 0:
        chocolates.append(chocolate)
        continue

    if chocolate == milk:
        milkshakes += 1
    else:
        milks.append(milk)
        chocolates.append(chocolate - 5)

print("Great! You made all the chocolate milkshakes needed!" if milkshakes == 5 else "Not enough milkshakes.")
print(f"Chocolate: {', '.join(map(str, chocolates))}" if chocolates else "Chocolate: empty")
print(f"Milk: {', '.join(map(str, milks))}" if milks else "Milk: empty")