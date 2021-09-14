# a if choice < 25
# b if choice >= 25 and < 50
# c if choice > 75
# d if choice >= 50 and <= 75

"""Challenge Question #1"""

choice: int = int(input("Enter a number: "))

if choice < 25:
    print("A")
else:
    if choice < 50:
        print("B")
    else:
        if choice > 75:
            print("C")
        else:
            print("D")