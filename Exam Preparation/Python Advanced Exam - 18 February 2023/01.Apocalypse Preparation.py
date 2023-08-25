from collections import deque

resources = {30: "Patch", 40: "Bandage", 100: "MedKit"}
created = {"Patch": 0, "Bandage": 0, "MedKit": 0}

textiles = deque(int(i) for i in input().split())
medicaments = deque(int(i) for i in input().split())

while True:
    if not textiles and not medicaments:
        print("Textiles and medicaments are both empty.")
        break
    if not textiles:
        print("Textiles are empty.")
        break
    if not medicaments:
        print("Medicaments are empty.")
        break

    textile = textiles.popleft()
    medicament = medicaments.pop()

    materials = textile + medicament

    if materials in resources:
        created[resources[materials]] += 1

    elif materials > 100:
        created[resources[100]] += 1
        medicaments[-1] += materials - 100

    else:
        medicament += 10
        medicaments.append(medicament)

for item in sorted(created.items(), key=lambda x: (-x[1], x[0])):
    if int(item[1]) > 0:
        print(f"{item[0]} - {item[1]}")

if medicaments:
    medicaments.reverse()
    print(f"Medicaments left: {', '.join(str(i) for i in medicaments)}")
if textiles:
    print(f"Textiles left: {', '.join(str(i) for i in textiles)}")