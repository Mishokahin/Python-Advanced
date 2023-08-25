def valid_move(r, c, mat):
    if 0 <= r < len(mat) and 0 <= c < len(mat[0]):
        next_position = mat[r][c]
        if next_position == "O":
            return False
        elif next_position == "-":
            return [r, c], mat, 0
        elif next_position == "P":
            mat[r][c] = "-"
            return [r, c], mat, 1


N, M = input().split()

player_position = []
matrix = []

directions = {"up": [-1, 0],
              "down": [1, 0],
              "left": [0, -1],
              "right": [0, 1]
              }

touched_opponents = 0
moves_made = 0

for row in range(int(N)):
    line = input().split()
    matrix.append(line)

    if "B" in line:
        player_position = [row, line.index("B")]

matrix[player_position[0]][player_position[1]] = "-"

while True:
    if touched_opponents == 3:
        break

    command = input()

    if command == "Finish":
        break

    row = player_position[0] + directions[command][0]
    col = player_position[1] + directions[command][1]

    result = valid_move(row, col, matrix)

    if result:
        player_position, matrix, touched = result
        touched_opponents += touched
        moves_made += 1

print("Game over!")
print(f"Touched opponents: {touched_opponents} Moves made: {moves_made}")