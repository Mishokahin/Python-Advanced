def find_tunnels(mat):
    tunnel_locations =[]
    for r in range(len(mat)):
        if "T" in mat[r]:
            tunnel_locations.append([r, mat[r].index("T")])
    return tunnel_locations


directions = {"left": [0, -1], "right": [0, 1], "up": [-1, 0], "down": [1, 0]}

rally_size = int(input())
racing_number = input()

matrix = [input().split() for _ in range(rally_size)]

car_position = [0, 0]
kilometers_passed = 0

tunnels = find_tunnels(matrix)

while True:
    command = input()
    if command == "End":
        matrix[car_position[0]][car_position[1]] = "C"
        print(f"Racing car {racing_number} DNF.")
        break

    current_row = car_position[0] + directions[command][0]
    current_col = car_position[1] + directions[command][1]

    car_position = [current_row, current_col]

    if car_position in tunnels:
        matrix[tunnels[0][0]][tunnels[0][1]] = "."
        matrix[tunnels[1][0]][tunnels[1][1]] = "."
        if tunnels.index(car_position) == 0:
            car_position = tunnels[1]
        elif tunnels.index(car_position) == 1:
            car_position = tunnels[0]
        kilometers_passed += 30

    elif matrix[car_position[0]][car_position[1]] == "F":
        matrix[car_position[0]][car_position[1]] = "C"
        print(f"Racing car {racing_number} finished the stage!")
        kilometers_passed += 10
        break

    elif matrix[car_position[0]][car_position[1]] == ".":
        kilometers_passed += 10

print(f"Distance covered {kilometers_passed} km.")
for row in matrix:
    print("".join(row))