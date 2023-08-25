def words_sorting(*args):
    words = {}
    for arg in args:
        words[arg] = sum(ord(c) for c in arg)

    if sum(words.values()) % 2 == 0:
        sorted_word = sorted(words.items(), key=lambda x: x[0])
    else:
        sorted_word = sorted(words.items(), key=lambda x: -x[1])

    result = ""

    for word, score in sorted_word:
        result += f"{word} - {score}\n"

    return result[:-1]


print(
    words_sorting(
        'cacophony',
        'accolade'
  ))
