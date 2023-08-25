from collections import deque

monsters = deque(map(int, input().split(",")))
soldiers = [int(i) for i in input().split(",")]

killed_monsters = 0

while True:
    if not monsters or not soldiers:
        break

    monster = monsters.popleft()
    soldier = soldiers.pop()

    if soldier >= monster:
        soldier -= monster
        killed_monsters += 1
        if soldiers:
            soldiers[-1] += soldier
        else:
            if soldier != 0:
                soldiers.append(soldier)

    else:
        monster -= soldier
        monsters.append(monster)

if not monsters:
    print("All monsters have been killed!")

if not soldiers:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {killed_monsters}")