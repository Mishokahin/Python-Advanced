from collections import deque

ramens = deque(map(int, input().split(", ")))
customers = deque(map(int, input().split(", ")))

while ramens and customers:
    ramen = ramens.pop()
    customer = customers.popleft()

    if ramen > customer:
        ramens.append(ramen - customer)

    elif customer > ramen:
        customers.appendleft(customer - ramen)

if not customers:
    print("Great job! You served all the customers.")
    if ramens:
        print(f"Bowls of ramen left: {', '.join(map(str, ramens))}")

else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(map(str, customers))}")