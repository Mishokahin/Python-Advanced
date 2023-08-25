rows, columns = [int(el) for el in input().split()]
matrix = [[el for el in input().split()] for _ in range(rows)]

count = 0

for row_idx in range(rows - 1):
    for col_idx in range(columns - 1):
        current_el = matrix[row_idx][col_idx]
        el_below = matrix[row_idx + 1][col_idx]
        next_el = matrix[row_idx][col_idx + 1]
        el_diagonal = matrix[row_idx + 1][col_idx + 1]

        if current_el == next_el == el_below == el_diagonal:
            count += 1

print(count)