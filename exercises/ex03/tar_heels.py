"""An exercise in remainders and boolean logic."""

__author__ = "730407005"


# Begin your solution here...
num: int = int(input("Enter an int: "))
divisible_7: bool = num % 7 == 0
divisible_2: bool = num % 2 == 0

if divisible_2 and not divisible_7:
    print("TAR")
elif divisible_7 and not divisible_2:
    print("HEELS")
elif divisible_7 and divisible_2:
    print("TAR HEELS")
else:
    print("CAROLINA")