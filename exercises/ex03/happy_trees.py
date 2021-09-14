"""Drawing forests in a loop."""

__author__ = "730407005"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

depth: int = int(input("Depth: "))
row: int = 1
output: str
while row <= depth:
    output = row * TREE
    print(output)
    row = row + 1