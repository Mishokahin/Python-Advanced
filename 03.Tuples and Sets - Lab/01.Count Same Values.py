tuple_of_numbers = tuple(map(float, input().split()))
unique_numbers = list()

for num in tuple_of_numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print('\n'.join(f"{number} - {tuple_of_numbers.count(number)} times" for number in unique_numbers))