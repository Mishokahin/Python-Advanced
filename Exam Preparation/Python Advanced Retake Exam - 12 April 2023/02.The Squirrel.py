def coordinates(mat):
    for r in range(N):
        for c in range(N):
            if mat[r][c] == "s":
                return r, c


def nut_finder(mat):
    nuts = []
    for r in range(N):
        for c in range(N):
            if mat[r][c] == "h":
                nuts.append([r, c])
    return nuts


def trap_finder(mat):
    for r in range(N):
        for c in range(N):
            if mat[r][c] == "t":
                return r, c


N = int(input())
commands = [i for i in input().split(", ")]
matrix = [input() for _ in range(N)]

row, column = coordinates(matrix)
nuts_list = [nut for nut in nut_finder(matrix)]
trap = trap_finder(matrix)
collected_nuts = 0
dead = False

for command in commands:
    if command == "left":
        column -= 1
    if command == "right":
        column += 1
    if command == "up":
        row -= 1
    if command == "down":
        row += 1
    if row not in range(N) or column not in range(N):
        print("The squirrel is out of the field.")
        dead = True
        break
    if [row, column] in nuts_list:
        nuts_list.remove([row, column])
        collected_nuts += 1
    if (row, column) == trap:
        print("Unfortunately, the squirrel stepped on a trap...")
        dead = True
        break
    if collected_nuts == 3:
        print("Good job! You have collected all hazelnuts!")
        break

if not dead and collected_nuts < 3:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {collected_nuts}")