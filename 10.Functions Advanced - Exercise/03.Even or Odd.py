def even_odd(*args):
    if args[-1] == "even":
        return [int(i) for i in args[:-1] if int(i) % 2 == 0]
    if args[-1] == "odd":
        return [int(i) for i in args[:-1] if int(i) % 2 != 0]


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))