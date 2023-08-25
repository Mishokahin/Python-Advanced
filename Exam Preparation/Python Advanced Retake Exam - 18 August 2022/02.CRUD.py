matrix = [[i for i in input().split()] for _ in range(6)]

player_row, player_col = [int(i) for i in input() if i.isdigit()]

directions = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}

while True:
    line = input().split(", ")

    command = line[0]

    if command == "Stop":
        break

    direction = line[1]

    current_row = player_row + directions[direction][0]
    current_col = player_col + directions[direction][1]

    if command == "Create":
        value = line[2]
        if matrix[current_row][current_col] == ".":
            matrix[current_row][current_col] = value

    elif command == "Update":
        value = line[2]
        if matrix[current_row][current_col] != ".":
            matrix[current_row][current_col] = value

    elif command == "Delete":
        if matrix[current_row][current_col] != ".":
            matrix[current_row][current_col] = "."

    elif command == "Read":
        if matrix[current_row][current_col] != ".":
            print(matrix[current_row][current_col])

    player_row, player_col = current_row, current_col

for row in matrix:
    print(*row)