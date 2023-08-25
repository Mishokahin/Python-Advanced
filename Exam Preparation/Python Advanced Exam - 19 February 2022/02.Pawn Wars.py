def player_position(mat, color):
    for r in range(len(mat)):
        for c in mat[r]:
            if c == color:
                return r, mat[r].index(color)


matrix = [input().split() for _ in range(8)]

white = player_position(matrix, "w")
black = player_position(matrix, "b")
white_player = ""
black_player = ""

turns = 0

while True:
    current_player = white if turns % 2 == 0 else black
    row1, col1 = white
    white_player = f"{chr(97 + col1)}{str((7 - row1) + 1)}"

    row2, col2 = black
    black_player = f"{chr(97 + col2)}{str(7 - row2 + 1)}"

    if current_player == white:
        if row1 - 1 == row2 and col1 - 1 == col2 or row1 - 1 == row2 and col1 + 1 == col2:
            print(f"Game over! White win, capture on {black_player}.")
            break
        row1 -= 1
        if row1 == 0:
            print(f"Game over! White pawn is promoted to a queen at {chr(97 + col1)}8.")
            break
        white = row1, col1

    else:
        if row2 + 1 == row1 and col2 - 1 == col1 or row2 + 1 == row1 and col2 + 1 == col1:
            print(f"Game over! Black win, capture on {white_player}.")
            break
        row2 += 1
        if row2 == 7:
            print(f"Game over! Black pawn is promoted to a queen at {chr(97 + col2)}1.")
            break
        black = row2, col2

    turns += 1