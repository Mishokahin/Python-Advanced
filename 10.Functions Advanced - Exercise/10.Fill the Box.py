def fill_the_box(*args):
    box_size = 1
    for i in args[:3]:
        box_size *= i
    cubes = sum(args[3:args.index("Finish")])
    cubes_left = box_size - cubes

    return f"No more free space! You have {abs(cubes_left)} more cubes." if cubes_left < 0 \
        else f"There is free space in the box. You could put {cubes_left} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))

print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))

print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))