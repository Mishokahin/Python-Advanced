import math
from collections import deque

expression = deque(input().split())

numbers = deque()
result = 0

while expression:
    item = expression.popleft()

    if item.strip("-").isdigit():
        numbers.append(int(item))
    elif item == "-":
        result = numbers.popleft()
        while numbers:
            result -= numbers.popleft()
        expression.appendleft(str(math.floor(result)))
        result = math.floor(result)
    elif item == "*":
        result = numbers.popleft()
        while numbers:
            result *= numbers.popleft()
        expression.appendleft(str(math.floor(result)))
        result = math.floor(result)
    elif item == "/":
        result = numbers.popleft()
        while numbers:
            result /= numbers.popleft()
        expression.appendleft(str(int(result)))
        result = math.floor(result)
    elif item == "+":
        result = numbers.popleft()
        while numbers:
            result += numbers.popleft()
        expression.appendleft(str(math.floor(result)))
        result = math.floor(result)

print(result)