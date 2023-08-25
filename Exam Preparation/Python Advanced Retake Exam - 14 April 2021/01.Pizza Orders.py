from collections import deque

pizza_orders = deque(map(int, input().split(", ")))
employees = deque(map(int, input().split(", ")))

total_count = 0

while pizza_orders and employees:
    order = pizza_orders.popleft()
    employee = employees.pop()

    if order <= 0 or order > 10:
        employees.append(employee)
        continue

    if order > employee:
        pizza_orders.appendleft(order - employee)
        total_count += employee

    if order <= employee:
        total_count += order

if employees:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_count}")
    print(f"Employees: {', '.join(str(i) for i in employees)}")

if pizza_orders:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(str(i) for i in pizza_orders)}")