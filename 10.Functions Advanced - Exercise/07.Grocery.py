def grocery_store(**groceries):
    return "\n".join(f"{i}: {q}" for i, q in sorted(groceries.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))


print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))

