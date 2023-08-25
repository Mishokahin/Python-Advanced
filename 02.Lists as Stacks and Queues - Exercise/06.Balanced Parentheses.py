from collections import deque

sequence = deque(parentheses for parentheses in input())

while sequence:
    if len(sequence) < 2:
        print("NO")
        exit()
    else:
        pairs = ["{}", "()", "[]"]
        if sequence[0] + sequence[1] in pairs:
            sequence.popleft()
            sequence.popleft()
        elif sequence[0] + sequence[-1] in pairs:
            sequence.popleft()
            sequence.pop()
        else:
            print("NO")
            exit()

print("YES")