"""Counting letters in a string."""

<<<<<<< HEAD
__author__ = "730407005"
=======
__author__ = "730243388"
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1


# Begin your solution here...

<<<<<<< HEAD
search_character: str = input("What letter do you want to search for?: ")
input_string: str = input("Enter a word: ")
i: int = 0
character_counter: int = 0

while i < len(input_string) - 1:
    if search_character == input_string[i]:
        character_counter += 1
        i += 1
    else:
        i += 1
    """
    print(word[i] + " " + str(i))
    i = i + 1
    """
print("Count: " + str(character_counter))
=======
letter: str = input("What letter do you want to seach for? ")
word: str = input("Enter a word ")
count: int = 0
i: int = 0
while (i < len(word)):
    if word[i] == letter:
        count += 1
    i += 1
print("Count: " + str(count))
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1
