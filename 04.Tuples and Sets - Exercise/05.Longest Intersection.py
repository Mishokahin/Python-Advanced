longest_intersection = set()

for _ in range(int(input())):
    first, second = [el.split(",") for el in input().split("-")]
    first_set = set(range(int(first[0]), int(first[1])+1))
    second_set = set(range(int(second[0]), int(second[1])+1))

    intersection = first_set.intersection(second_set)

    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print(f"Longest intersection is [{', '.join(map(str, longest_intersection))}] with length {len(longest_intersection)}")