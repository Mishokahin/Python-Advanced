from collections import deque
requirements = deque([[80, "Vihren"],
                     [90, "Kutelo"],
                     [100, "Banski Suhodol"],
                     [60, "Polezhan"],
                     [70, "Kamenitza"]])

concurred = []

food_portions = deque([int(i) for i in input().split(", ")])
stamina = deque([int(i) for i in input().split(", ")])

days = 1

while True:
    if not requirements:
        print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
        break
    if days > 7 or not food_portions or not stamina:
        print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
        break

    daily_portion = food_portions.pop()
    daily_stamina = stamina.popleft()

    energy = daily_portion + daily_stamina

    peak = requirements.popleft()

    if energy >= peak[0]:
        concurred.append(peak[1])
        days += 1
    else:
        requirements.appendleft(peak)
        days += 1

if concurred:
    print("Conquered peaks:")
    print("\n".join(concurred))