def func_executor(*functions):
    result = []

    for function, args in functions:
        result.append(f"{function.__name__} - {function(*args)}")

    return "\n".join(result)


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
    )
)
