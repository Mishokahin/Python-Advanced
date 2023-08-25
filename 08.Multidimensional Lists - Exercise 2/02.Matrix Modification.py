N = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(N)]

while True:
    command, *info = input().split()
    if command == "END":
        break

    row, col, value = info[0], info[1], info[2]

    if not(0 <= int(row) < N and 0 <= int(col) < N):
        print("Invalid coordinates")

    elif command == "Add":
        matrix[int(row)][int(col)] += int(value)

    elif command == "Subtract":
        matrix[int(row)][int(col)] -= int(value)

[print(*row) for row in matrix]