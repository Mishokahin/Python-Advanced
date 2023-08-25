from collections import deque

materials = deque(map(int, input().split()))
magic_levels = deque(map(int, input().split()))

crafted = []
toy_table = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}

while materials and magic_levels:
    material = materials.pop() if magic_levels[0] or not materials[0] else 0
    magic = magic_levels.popleft() if material or not magic_levels[0] else 0

    if not magic:
        continue

    toy = material * magic

    if toy_table.get(toy):
        crafted.append(toy_table[toy])

    elif toy < 0:
        materials.append(material + magic)

    elif toy > 0:
        materials.append(material + 15)

if {"Doll", "Wooden train"}.issubset(crafted) or {"Teddy bear", "Bicycle"}.issubset(crafted):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(map(str, reversed(materials)))}")
if magic_levels:
    print(f"Magic left: {', '.join(map(str, magic_levels))}")

[print(f"{toy}: {crafted.count(toy)}") for toy in sorted(set(crafted))]