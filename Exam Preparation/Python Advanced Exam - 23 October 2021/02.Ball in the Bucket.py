def points_earned(mat, r, c):
    points = 0
    if mat[r][c] == "B":
        mat[r][c] = 0
        for i in range(0, 6):
            points += int(mat[i][c])

    return points


def result(points_scored):
    prize = ""
    if 100 <= points_scored <= 199:
        prize = "Football"
    elif 200 <= points_scored <= 299:
        prize = "Teddy Bear"
    elif 300 <= points_scored:
        prize = "Lego Construction Set"

    if prize != "":
        return f"Good job! You scored {points_scored} points, and you've won {prize}."

    else:
        return f"Sorry! You need {100 - points_scored} points more to win a prize."


matrix = [input().split() for _ in range(6)]

total_points = 0

for _ in range(3):
    row, col = map(int, input().strip("(").strip(")").split(", "))
    if row in range(0, 6) and col in range(0, 6):
        total_points += points_earned(matrix, row, col)

print(result(total_points))