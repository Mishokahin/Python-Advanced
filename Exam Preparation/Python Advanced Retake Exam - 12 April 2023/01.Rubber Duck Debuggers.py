from collections import deque

ducky_table = {"Darth Vader Ducky": 0,
               "Thor Ducky": 0,
               "Big Blue Rubber Ducky": 0,
               "Small Yellow Rubber Ducky": 0
               }

programmers_time = deque(int(p) for p in input().split())
number_of_tasks = deque(int(n) for n in input().split())

while programmers_time and number_of_tasks:
    programmer = programmers_time.popleft()
    tasks = number_of_tasks.pop()

    tasks_done = programmer * tasks

    if tasks_done in range(0, 61):
        ducky_table["Darth Vader Ducky"] += 1
    elif tasks_done in range(61, 121):
        ducky_table["Thor Ducky"] += 1
    elif tasks_done in range(121, 181):
        ducky_table["Big Blue Rubber Ducky"] += 1
    elif tasks_done in range(181, 241):
        ducky_table["Small Yellow Rubber Ducky"] += 1
    else:
        programmers_time.append(programmer)
        number_of_tasks.append(tasks - 2)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
for ducky, count in ducky_table.items():
    print(f"{ducky}: {count}")