"""Counting letters in a string."""

__author__ = "730407005"


# Begin your solution here...

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