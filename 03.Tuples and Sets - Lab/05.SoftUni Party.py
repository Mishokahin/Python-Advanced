N = int(input())
reservation = set()

for _ in range(N):
    reservation.add(input())

while True:
    command = input()
    if command == "END":
        break
    if command in reservation:
        reservation.remove(command)

print(len(reservation))

if reservation:
    print("\n".join(sorted(reservation)))