from re import findall

input_path = "files/text.txt"
output_path = "files/output.txt"

with open(input_path, "r") as file:
    text = file.readlines()

output_file = open(output_path, "w")

letter_count = r'[^\W\s]'
punctuation_count = r'[^\w\s]'

for row in range(len(text)):
    letters, punctuation = len(findall(letter_count, text[row])), len(findall(punctuation_count, text[row]))

    output_file.write(f"Line {row + 1}: {''.join(text[row][:-1])} ({letters})({punctuation})\n")

output_file.close()