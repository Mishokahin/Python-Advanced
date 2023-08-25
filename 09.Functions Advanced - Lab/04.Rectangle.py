def rectangle(length, width):
    if all([isinstance(length, int), isinstance(width, int)]):
        def area():
            return length * width

        def perimeter():
            return (2 * length) + (2 * width)

        return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"

    else:
        return f"Enter valid values!"


print(rectangle(2, 10))