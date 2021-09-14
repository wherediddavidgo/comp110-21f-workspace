"""Finding duplicate letters in a word."""

__author__ = "730407005"

i: int = 1
c: int = 0
dups: bool = False
word: str = input("Enter a word: ")
ichar: str
cchar: str

while i < len(word):
    ichar = word[i]
    cchar = word[c]
    while c < len(word):
        if ichar == cchar:
            dups = True
            c = c + 1
        else:
            c = c + 1
    c = 0
    i = i + 1
print("Found duplicates: " + str(dups))