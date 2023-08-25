from collections import deque


def accommodate_new_pets(capacity, weight_limit, *pets):
    result = ""
    housed_pets = {}
    pets_to_house = deque(pets)
    while pets_to_house:
        if sum(housed_pets.values()) == capacity:
            break
        pet_type, pet_weight = pets_to_house.popleft()
        if pet_weight <= weight_limit:
            if pet_type not in housed_pets:
                housed_pets[pet_type] = 0
            housed_pets[pet_type] += 1

    if pets_to_house:
        result += "You did not manage to accommodate all pets!\n"
    else:
        result += f"All pets are accommodated! Available capacity: {capacity - sum(housed_pets.values())}.\n"
    sorted_pets = sorted(housed_pets.items(), key=lambda x: x[0])
    result += "Accommodated pets:\n"
    for pet, count in sorted_pets:
        result += f"{pet}: {count}\n"

    return result[:-1]


print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))