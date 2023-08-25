from collections import deque
people = deque()

while True:
    line = input()
    if line == "End":
        count = len(people)
        print(f"{count} people remaining.")
        break
    if line == "Paid":
        print("\n".join(people))
        people.clear()
    else:
        people.append(line)