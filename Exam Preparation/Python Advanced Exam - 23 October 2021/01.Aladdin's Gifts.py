from collections import deque


def mix(mat, mag):
    total = mat + mag
    if total < 100:
        if total % 2 == 0:
            total = (mat * 2) + (mag * 3)
        else:
            total *= 2
    elif total > 499:
        total /= 2

    return total


mix_materials = deque(map(int, input().split()))
magic_levels = deque(map(int, input().split()))

gifts = {"Gemstone": 0, "Porcelain Sculpture": 0, "Gold": 0, "Diamond Jewellery": 0}

while mix_materials and magic_levels:
    materials = mix_materials.pop()
    magic = magic_levels.popleft()

    mixture = mix(materials, magic)

    if 100 <= mixture <= 199:
        gifts["Gemstone"] += 1

    elif 200 <= mixture <= 299:
        gifts["Porcelain Sculpture"] += 1

    elif 300 <= mixture <= 399:
        gifts["Gold"] += 1

    elif 400 <= mixture <= 499:
        gifts["Diamond Jewellery"] += 1

if gifts["Gemstone"] > 0 and gifts["Porcelain Sculpture"] > 0 or gifts["Gold"] > 0 and gifts["Diamond Jewellery"] > 0:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")
if mix_materials:
    print(f"Materials left: {', '.join(str(i) for i in mix_materials)}")
if magic_levels:
    print(f"Magic left: {', '.join(str(i) for i in magic_levels)}")

sorted_gifts = sorted(gifts.items(), key=lambda x: x[0])

for gift, amount in sorted_gifts:
    if amount > 0:
        print(f"{gift}: {amount}")
