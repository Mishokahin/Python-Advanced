size = int(input())
matrices = list([int(num) for num in input().split()] for _ in range(size))

result = [matrices[idx][idx] for idx in range(size)]

print(sum(result)),