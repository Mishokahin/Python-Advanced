def matrix_search(mat, request, n):
    for row in range(n):
        for col in range(n):
            if mat[row][col] == request:
                return row, col


size = int(input())
matrix = list(input() for _ in range(size))

required_symbol = input()
position = matrix_search(matrix, required_symbol, size)

print(position if position else f"{required_symbol} does not occur in the matrix")