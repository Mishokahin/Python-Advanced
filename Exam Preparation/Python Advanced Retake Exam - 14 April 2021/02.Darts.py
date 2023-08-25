def score(mat, r, c):
    if mat[r][c] == "D":
        points = sum(map(int, [mat[0][c], mat[6][c], mat[r][0], mat[r][6]])) * 2
    elif mat[r][c] == "T":
        points = sum(map(int, [mat[0][c], mat[6][c], mat[r][0], mat[r][6]])) * 3
    else:
        points = int(mat[r][c])

    return points


player_1, player_2 = input().split(", ")

dart_board = [input().split() for _ in range(7)]

player_1_data = {"name": player_1, "score": 501, "turns": 0}
player_2_data = {"name": player_2, "score": 501, "turns": 0}

turns = 0

while True:
    turns += 1
    current_player = player_1_data if turns % 2 != 0 else player_2_data
    row, col = map(int, input().strip("(").strip(")").split(", "))
    current_player["turns"] += 1
    if row in range(7) and col in range(7):
        if dart_board[row][col] == "B":
            print(f"{current_player['name']} won the game with {current_player['turns']} throws!")
            break
        else:
            current_player['score'] -= score(dart_board, row, col)

        if current_player['score'] <= 0:
            print(f"{current_player['name']} won the game with {current_player['turns']} throws!")
            break



