count = int(input())
cars = set()

for _ in range(count):
    command, car = input().split(", ")
    if command == "IN":
        cars.add(car)
    if command == "OUT":
        if car in cars:
            cars.remove(car)

if cars:
    print("\n".join(cars))
else:
    print("Parking Lot is Empty")