rows, columns = [int(el) for el in input().split(", ")]
matrix = list([int(num) for num in input().split(", ")] for _ in range(rows))

max_sum = float("-inf")
sub_matrix = []

for row_idx in range(rows - 1):
    for col_idx in range(columns - 1):
        current_el = matrix[row_idx][col_idx]
        el_below = matrix[row_idx + 1][col_idx]
        next_el = matrix[row_idx][col_idx + 1]
        el_diagonal = matrix[row_idx + 1][col_idx + 1]

        current_sum = current_el + el_below + next_el + el_diagonal

        if max_sum < current_sum:
            max_sum = current_sum
            sub_matrix = [[current_el, next_el], [el_below, el_diagonal]]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)