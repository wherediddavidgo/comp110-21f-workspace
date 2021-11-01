"""Demonstrates python numeric operators for two input numbers."""

__author__ = "730243388"

string_one = input("Left-hand side: ")
string_two = input("Right-hand side: ")

number_one = int(string_one)
number_two = int(string_two)

print(string_one + " ** " + string_two + " is " + str(number_one ** number_two))
print(string_one + " / " + string_two + " is " + str(number_one / number_two))
print(string_one + " // " + string_two + " is " + str(number_one // number_two))
print(string_one + " % " + string_two + " is " + str(number_one % number_two))
