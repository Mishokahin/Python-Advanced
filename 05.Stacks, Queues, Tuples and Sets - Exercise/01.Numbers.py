first = set(map(int, input().split()))
second = set(map(int, input().split()))

for _ in range(int(input())):
    command = input().split()
    if command[0] + " " + command[1] == "Add First":
        [first.add(num) for num in map(int, command[2:len(command)+1])]
    elif command[0] + " " + command[1] == "Add Second":
        [second.add(num) for num in map(int, command[2:len(command)+1])]
    elif command[0] + " " + command[1] == "Remove First":
        [first.discard(num) for num in map(int, command[2:len(command)+1])]
    elif command[0] + " " + command[1] == "Remove Second":
        [second.discard(num) for num in map(int, command[2:len(command)+1])]
    elif command[0] + " " + command[1] == "Check Subset":
        print(second.issubset(first) or first.issubset(second))

print(", ".join(map(str, sorted(first))))
print(", ".join(map(str, sorted(second))))