def start_spring(**kwargs):
    sprint_objects = {}
    for name, type_of_object in kwargs.items():
        if type_of_object not in sprint_objects:
            sprint_objects[type_of_object] = []
        sprint_objects[type_of_object].append(name)

    sorted_sprint_objects = sorted(sprint_objects.items(), key=lambda x: (-len(x[1]), x[0]))

    result = ""
    for category, items in sorted_sprint_objects:
        result += f"{category}:\n"
        sorted_items = sorted(items)
        for item in sorted_items:
            result += f"-{item}\n"

    return result[:-1]


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}

print(start_spring(**example_objects))