rows, columns = map(int, input().split(", "))
matrices = list(map(int, input().split(", ")) for row in range(rows))

print(sum(list(sum(matrix) for matrix in matrices)))
print(matrices)