"""Finding duplicate letters in a word."""

__author__ = "730407005"

i: int = 0
j: int = 0
dups: bool = False
word: str = input("Enter a word: ")

while i < len(word):
    j = 0
    while j < len(word):
        if j == i:
            j = j + 1
        else:
            if word[i] == word[j]:
                dups = True
        j = j + 1
    i = i + 1


print("Found duplicate: " + str(dups))