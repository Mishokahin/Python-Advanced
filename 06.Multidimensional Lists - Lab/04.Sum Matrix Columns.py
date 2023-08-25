rows, columns = map(int, input().split(", "))
matrices = list([int(num) for num in input().split()] for _ in range(rows))

for c in range(columns):
    current_sum = 0
    for r in range(rows):
        current_sum += matrices[r][c]
    print(current_sum)