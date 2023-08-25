n = int(input())
matrix = list(list(num for num in map(int, input().split(", ")) if num % 2 == 0) for _ in range(n))

print(matrix)