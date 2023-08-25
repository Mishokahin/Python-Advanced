from collections import deque

sub_strings = deque(map(str, input().split()))
colors = ["red", "yellow", "blue", "orange", "purple", "green"]
secondary_colors = {"orange": {"red", "yellow"},
                    "purple": {"red", "blue"},
                    "green": {"yellow", "blue"}
                    }

found_colors = []

while sub_strings:
    color_1 = sub_strings.popleft()
    color_2 = sub_strings.pop() if sub_strings else ""

    if color_1 + color_2 in colors:
        found_colors.append(color_1 + color_2)

    elif color_2 + color_1 in colors:
        found_colors.append(color_2 + color_1)

    else:
        if len(color_1[:-1]) > 0:
            sub_strings.insert(len(sub_strings) // 2, color_1[:-1])
        if len(color_2[:-1]) > 0:
            sub_strings.insert(len(sub_strings) // 2, color_2[:-1])

final_colors = []
for color in found_colors:
    if color in colors[:3] or color in secondary_colors.keys() and set(secondary_colors[color]).issubset(found_colors):
        final_colors.append(color)

print(final_colors)