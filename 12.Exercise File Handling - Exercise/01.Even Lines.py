from re import sub

file_path = "files/text.txt"

with open(file_path, "r") as file:
    text = file.readlines()

punctuation = r'[^\w\s]'

for row in range(0, len(text), 2):
    text[row] = sub(punctuation, "@", text[row])
    print(*text[row].split()[::-1], sep=" ")