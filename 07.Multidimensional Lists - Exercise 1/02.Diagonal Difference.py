size = int(input())
matrix = [[int(num) for num in input().split()] for _ in range(size)]

primary_diagonal = sum([matrix[idx][idx] for idx in range(size)])
secondary_diagonal = sum([matrix[idx][size - (idx + 1)] for idx in range(size)])

print(abs(primary_diagonal - secondary_diagonal))

