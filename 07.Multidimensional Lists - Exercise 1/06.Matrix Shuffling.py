rows, columns = [int(el) for el in input().split()]
matrix = [input().split() for _ in range(rows)]

while True:
    command = input()
    if command == "END":
        break

    command_args = command.split()

    if len(command_args) == 5:
        row1, col1, row2, col2 = [int(el) for el in command_args[1:5]]
        if row1 and row2 not in range(rows) and col1 and col2 not in range(columns):
            print("Invalid input!")
        else:
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
            [print(" ".join(el for el in matrix[r][0:columns])) for r in range(rows)]

    else:
        print("Invalid input!")