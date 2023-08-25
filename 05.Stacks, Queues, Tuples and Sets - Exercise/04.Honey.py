from collections import deque


def calculation(bee, symbol, nectar):
    produced_honey = 0
    if symbol == "+":
        produced_honey = bee + nectar
    elif symbol == "-":
        produced_honey = bee - nectar
    elif symbol == "*":
        produced_honey = bee * nectar
    elif symbol == "/":
        if bee == 0 or nectar == 0:
            produced_honey = 0
        else:
            produced_honey = bee / nectar
    return produced_honey


bees = deque(map(int, input().split()))
nectars = deque(map(int, input().split()))
symbols = deque(input().split())

honey = 0

while bees and nectars:
    bee = bees.popleft()
    nectar = nectars.pop()

    if bee > nectar:
        bees.appendleft(bee)

    else:
        symbol = symbols.popleft()
        honey += abs(calculation(bee, symbol, nectar))

print(f"Total honey made: {honey}")
if bees:
    print(f"Bees left: {', '.join(map(str, bees))}")
if nectars:
    print(f"Nectar left: {', '.join(map(str, nectars)) }")