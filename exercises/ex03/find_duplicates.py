"""Finding duplicate letters in a word."""

<<<<<<< HEAD
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
=======
__author__ = "123456789"

word: str = input("Enter a word: ")

i: int = 0
duplicate: bool = False
while (i < len(word)):
    j: int = i + 1
    while(j < len(word)):
        if (word[i] == word[j]):
            duplicate = True
        j += 1
    i += 1

print("Found duplicate: " + str(duplicate))
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1
