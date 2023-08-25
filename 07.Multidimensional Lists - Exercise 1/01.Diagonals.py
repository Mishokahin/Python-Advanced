size = int(input())
matrix = [[int(num) for num in input().split(", ")] for _ in range(size)]

primary_diagonal = [matrix[idx][idx] for idx in range(size)]
secondary_diagonal = [matrix[idx][size - (idx + 1)] for idx in range(size)]

print(f"Primary diagonal: {', '.join(str(el) for el in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(el) for el in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")