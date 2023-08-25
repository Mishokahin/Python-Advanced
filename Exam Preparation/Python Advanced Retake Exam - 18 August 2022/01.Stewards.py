from collections import deque


def matches(f_seat, s_seat, l_seats):
    if f_seat in l_seats:
        return True, f_seat
    elif s_seat in l_seats:
        return True, s_seat


seats = list(i for i in input().split(", "))
top_sequence = deque(int(j) for j in input().split(", "))
bottom_sequence = deque(int(k) for k in input().split(", "))

matched_seats = []

rotations = 0

while True:
    if len(matched_seats) == 3:
        break
    if rotations == 10:
        break

    rotations += 1

    first_number = top_sequence.popleft()
    second_number = bottom_sequence.pop()

    character = chr(first_number + second_number)

    first_seat = str(first_number) + character
    second_seat = str(second_number) + character

    if matches(first_seat, second_seat, seats):
        if matches(first_seat, second_seat, seats)[1] not in matched_seats:
            matched_seats.append(matches(first_seat, second_seat, seats)[1])
            seats.pop(seats.index(matches(first_seat, second_seat, seats)[1]))

    else:
        top_sequence.append(first_number)
        bottom_sequence.appendleft(second_number)

print(f"Seat matches: {', '.join(matched_seats)}")
print(f"Rotations count: {rotations}")