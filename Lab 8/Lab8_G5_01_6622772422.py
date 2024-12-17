s = input("Input: ").lower()
words = s.split()
word_set = {}

for word_key in words:
    if word_key in word_set:
        word_set[word_key] += 1
    else:
        word_set[word_key] = 1

max_word = max(word_set.values())

print("Output:")

for word, count in word_set.items():
    if count == max_word:
        print(word, "=", count)