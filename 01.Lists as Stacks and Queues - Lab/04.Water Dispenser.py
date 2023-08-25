from collections import deque
people = deque()

liters_of_water = int(input())

while True:
    line = input()
    if line == "Start":
        break
    people.append(line)

while True:
    line = input()
    if line == "End":
        print(f"{liters_of_water} liters left")
        break
    line_args = line.split()
    if len(line_args) == 2:
        liters_of_water += int(line_args[1])
    else:
        liters = int(line_args[0])
        person = people.popleft()
        if liters > liters_of_water:
            print(f"{person} must wait")
        else:
            print(f"{person} got water")
            liters_of_water -= liters