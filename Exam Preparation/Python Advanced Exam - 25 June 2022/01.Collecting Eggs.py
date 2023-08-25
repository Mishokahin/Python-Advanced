from collections import deque


eggs = deque([int(i) for i in input().split(", ")])
papers = deque([int(i) for i in input().split(", ")])

box = 50
packed_boxes = 0

while eggs and papers:
    egg = eggs.popleft()
    paper = papers.pop()

    if egg <= 0:
        papers.append(paper)

    elif egg == 13:
        first_paper = papers.popleft()
        papers.append(first_paper)
        papers.appendleft(paper)

    else:
        if egg + paper <= box:
            packed_boxes += 1
        else:
            continue

if packed_boxes > 0:
    print(f"Great! You filled {packed_boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")
if eggs:
    print(f"Eggs left: {', '.join(map(str, eggs))}")
if papers:
    print(f"Pieces of paper left: {', '.join(map(str, papers))}")