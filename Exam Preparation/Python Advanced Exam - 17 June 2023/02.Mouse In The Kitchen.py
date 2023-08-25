def find_mouse_cheese(mat):
    position = 0, 0
    found_cheese = 0
    for r in range(len(mat)):
        if "M" in mat[r]:
            position = r, mat[r].index("M")
            mat[r][mat[r].index("M")] = "*"
        if "C" in mat[r]:
            found_cheese += mat[r].count("C")

    return position, found_cheese


N, M = map(int, input().split(","))

cupboard = [[c for c in input()] for _ in range(N)]

directions = {"up": (-1, 0), "down": (1, 0), "right": (0, 1), "left": (0, -1)}

mouse = find_mouse_cheese(cupboard)[0]
cheese = find_mouse_cheese(cupboard)[1]


while True:
    command = input()
    if command == "danger":
        cupboard[mouse[0]][mouse[1]] = "M"
        print("Mouse will come back later!")
        break

    row, col = mouse[0] + directions[command][0], mouse[1] + directions[command][1]

    if row not in range(N) or col not in range(M):
        cupboard[mouse[0]][mouse[1]] = "M"
        print("No more cheese for tonight!")
        break

    if cupboard[row][col] == "@":
        continue

    if cupboard[row][col] == "T":
        cupboard[row][col] = "M"
        print("Mouse is trapped!")
        break

    if cupboard[row][col] == "C":
        cheese -= 1
        cupboard[row][col] = "*"
        if cheese == 0:
            cupboard[row][col] = "M"
            print("Happy mouse! All the cheese is eaten, good night!")
            break

    mouse = row, col

for rows in cupboard:
    print(f"{''.join(rows)}")