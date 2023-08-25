def flights(*args):
    result = {}
    last_destination = ""
    for arg in args:
        if arg == "Finish":
            break
        if type(arg) != int:
            if arg not in result:
                result[arg] = 0
            last_destination = arg
        else:
            result[last_destination] += arg

    return result


print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
