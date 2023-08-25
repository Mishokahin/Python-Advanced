def operate(*args):
    if args[0] == "+":
        return sum(args[1:])
    if args[0] == "-":
        result = args[1]
        for n in args[2:]:
            result -= n
        return result
    if args[0] == "*":
        result = args[1]
        for n in args[2:]:
            result *= n
        return result
    if args[0] == "/":
        if any([bool(i == 0) for i in args[1:]]):
            return 0
        else:
            result = args[1]
            for n in args[2:]:
                result /= n
            return result


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))