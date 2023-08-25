def position(mat):
    for r in range(len(mat)):
        if "B" in mat[r]:
            return r, mat[r].index("B")


N, M = map(int, input().split())

neighborhood = [[c for c in input()] for _ in range(N)]

directions = {"up": (-1, 0), "down": (1, 0), "right": (0, 1), "left": (0, -1)}

delivery_boy = position(neighborhood)


while True:
    direction = input()

    row = delivery_boy[0] + directions[direction][0]
    col = delivery_boy[1] + directions[direction][1]

    if row not in range(N) or col not in range(M):
        print("The delivery is late. Order is canceled.")
        neighborhood[position(neighborhood)[0]][position(neighborhood)[1]] = " "
        break

    if neighborhood[row][col] == "*":
        continue

    if neighborhood[row][col] == "-":
        neighborhood[row][col] = "."

    if neighborhood[row][col] == "P":
        neighborhood[row][col] = "R"
        print("Pizza is collected. 10 minutes for delivery.")

    if neighborhood[row][col] == "A":
        neighborhood[row][col] = "P"
        print("Pizza is delivered on time! Next order...")
        break

    delivery_boy = row, col

for r in neighborhood:
    print(f"{''.join(map(str, r))}")