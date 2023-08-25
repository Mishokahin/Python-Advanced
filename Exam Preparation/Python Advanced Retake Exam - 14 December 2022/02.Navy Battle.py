def find_player_position(mat):
    for r in range(len(mat)):
        if "S" in mat[r]:
            return [r, mat[r].index("S")]


directions = {"up": [-1, 0],
              "down": [1, 0],
              "left": [0, -1],
              "right": [0, 1]
              }

n = int(input())
matrix = [[i for i in input()] for _ in range(n)]

submarine = find_player_position(matrix)

mines_hit = 0
cruisers = 3

matrix[submarine[0]][submarine[1]] = "-"

while True:
    if cruisers == 0:
        print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
        matrix[submarine[0]][submarine[1]] = "S"
        break
    if mines_hit == 3:
        print(f"Mission failed, U-9 disappeared! Last known coordinates [{submarine[0]}, {submarine[1]}]!")
        matrix[submarine[0]][submarine[1]] = "S"
        break

    command = input()

    row = submarine[0] + directions[command][0]
    col = submarine[1] + directions[command][1]

    submarine = [row, col]

    if matrix[row][col] == "*":
        mines_hit += 1
        matrix[row][col] = "-"

    if matrix[row][col] == "C":
        cruisers -= 1
        matrix[row][col] = "-"

for rows in matrix:
    print("".join(rows))