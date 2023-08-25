from collections import deque

tools = deque(map(int, input().split()))
substances = deque(map(int, input().split()))
challenges = list(map(int, input().split()))

while tools and substances and challenges:
    tool = tools.popleft()
    substance = substances.pop()

    total = tool * substance

    if total in challenges:
        challenges.remove(total)

    else:
        tools.append(tool + 1)
        if substance - 1 > 0:
            substances.append(substance - 1)

print("Harry is lost in the temple. Oblivion awaits him." if challenges
      else "Harry found an ostracon, which is dated to the 6th century BCE.")

if tools:
    print(f"Tools: {', '.join(map(str, tools))}")

if substances:
    print(f"Substances: {', '.join(map(str, substances))}")

if challenges:
    print(f"Challenges: {', '.join(map(str, challenges))}")