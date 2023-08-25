rows, columns = [int(el) for el in input().split()]
matrix = [[int(el) for el in input().split()] for _ in range(rows)]

sub_matrix = []
max_sum = float("-inf")

for row_idx in range(rows - 2):
    for col_idx in range(columns - 2):
        sub_matrix_row_1 = matrix[row_idx][col_idx:col_idx+3]
        sub_matrix_row_2 = matrix[row_idx + 1][col_idx:col_idx+3]
        sub_matrix_row_3 = matrix[row_idx + 2][col_idx:col_idx+3]

        current_sum = sum(sub_matrix_row_1) + sum(sub_matrix_row_2) + sum(sub_matrix_row_3)

        if current_sum > max_sum:
            max_sum = current_sum
            sub_matrix = [sub_matrix_row_1, sub_matrix_row_2, sub_matrix_row_3]

print(f"Sum = {max_sum}")
print(*sub_matrix[0])
print(*sub_matrix[1])
print(*sub_matrix[2])