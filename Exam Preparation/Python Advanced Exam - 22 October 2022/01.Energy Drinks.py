from collections import deque

caffeine_mgs = deque(int(i) for i in input().split(", "))
energy_drinks = deque(int(j) for j in input().split(", "))
total_caffeine = 0

while caffeine_mgs and energy_drinks:
    caffeine_mg = caffeine_mgs.pop()
    energy_drink = energy_drinks.popleft()

    caffeine = caffeine_mg * energy_drink

    if total_caffeine + caffeine > 300:
         energy_drinks.append(energy_drink)
         if total_caffeine >= 30:
             total_caffeine -= 30
    else:
        total_caffeine += caffeine

if energy_drinks:
    print(f"Drinks left: {', '.join(str(drink) for drink in energy_drinks)}")

else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {total_caffeine} mg caffeine.")