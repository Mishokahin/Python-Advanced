def shopping_cart(*args):
    categories = {"Soup": [], "Pizza": [], "Dessert": []}
    for arg in args:
        if type(arg) != tuple:
            break
        else:
            category = arg[0]
            product = arg[1]
            if product not in categories[category]:
                if category == "Soup" and len(categories["Soup"]) < 3:
                    categories["Soup"].append(product)
                if category == "Pizza" and len(categories["Pizza"]) < 4:
                    categories["Pizza"].append(product)
                if category == "Dessert" and len(categories["Dessert"]) < 2:
                    categories["Dessert"].append(product)

    for value in categories.values():
        if len(value) > 0:
            break
    else:
        return 'No products in the cart!'

    sorted_cart = sorted(categories.items(), key=lambda x: (-len(x[1]), x[0]))
    result = ''
    for category, products in sorted_cart:
        result += f"{category}:\n"
        sorted_product = sorted(products)
        for product in sorted_product:
            result += f" - {product}\n"

    return result
