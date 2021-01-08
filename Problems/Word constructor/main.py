word1 = input()
word2 = input()

for letter1, letter2 in zip(word1, word2):
    print(f"{letter1}{letter2}", end="")
