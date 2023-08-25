def shop_from_grocery_list(budget, products, *prices):
    bud = budget
    purchased = [product for product in products]
    for item, price in prices:
        if item in purchased:
            if price <= bud:
                bud -= price
                purchased.remove(item)
            else:
                break

    if purchased:
        return f"You did not buy all the products. Missing products: {', '.join(purchased)}."
    else:
        return f"Shopping is successful. Remaining budget: {bud:.2f}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))