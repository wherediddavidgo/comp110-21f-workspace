"""An exercise in remainders and boolean logic."""

<<<<<<< HEAD
__author__ = "730407005"
=======
__author__ = "730243388"
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1


# Begin your solution here...
num: int = int(input("Enter an int: "))
<<<<<<< HEAD
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
=======

if (num % 14 == 0):
    print("TAR HEELS")
elif (num % 7 == 0):
    print("HEELS")
elif (num % 2 == 0):
    print("TAR")
else:
    print("CAROLINA")
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1
