rows_count = int(input())
matrix = [map(int, input().split(', ')) for _ in range(rows_count)]
print([num for row in matrix for num in row])