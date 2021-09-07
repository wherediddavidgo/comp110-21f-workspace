"""Repeating a beat in a loop."""

__author__ = "730407005"


# Begin your solution here...

beat: str = input("What beat would you like to repeat? ")
beat_count: int = int(input("How many times do you want to repeat it? "))
current_count: int = 0

output: str = beat

if beat_count <= 0:
    print("No beat...")
else:
    while current_count < beat_count - 1:
        output = output + " " + beat
        current_count += 1
    print(output)