def player_position(mat):
    for r in range(len(mat)):
        for c in mat[r]:
            if c == "E":
                return r, mat[r].index("E")


def current_pos(p_pos, d_pos):
    if p_pos + d_pos < 0:
        return 5
    elif p_pos + d_pos > 5:
        return 0
    else:
        return p_pos + d_pos


matrix = [input().split() for _ in range(6)]

directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

player = player_position(matrix)

commands = input().split(", ")
deposits = {"W": ["Water", 0], "M": ["Metal", 0], "C": ["Concrete", 0]}

for command in commands:
    row = current_pos(player[0], directions[command][0])
    col = current_pos(player[1], directions[command][1])

    if matrix[row][col] == "R":
        print(f"Rover got broken at ({row}, {col})")
        break

    if matrix[row][col] in deposits:
        deposits[matrix[row][col]][1] += 1
        print(f"{deposits[matrix[row][col]][0]} deposit found at ({row}, {col})")

    player = row, col

if deposits["W"][1] > 0 and deposits["M"][1] > 0 and deposits["C"][1] > 0:
    print("Area suitable to start the colony.")

else:
    print("Area not suitable to start the colony.")