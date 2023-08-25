list_of_list = [numbers.split() for numbers in input().split("|")]
print(*[" ".join(sub_list) for sub_list in list_of_list[::-1] if sub_list])
