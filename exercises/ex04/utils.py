"""List utility functions."""

__author__ = "730407005"
# TODO: Implement your functions here.


def all(int_list: list[int], check_int: int) -> bool:
    """Checks whether every item in a list of ints is equal to another int."""
    i: int = 0
    result: bool = False
    while i < len(int_list):
        if int_list[i] == check_int:
            result = True
        else:
            return False
        i += 1
    return result


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Checks for deep equality of int lists by running through each item individually."""
    i: int = 0
    j: int = 0
    result: bool = False
    if len(list_1) == len(list_2):
        if len(list_1) == 0 and len(list_2) == 0:
            return True
        else:
            while i < len(list_1) and j < len(list_2):
                if list_1[i] == list_2[j]:
                    result = True
                else:
                    return False
                i += 1
                j += 1
    else:
        return False
    return result


def max(int_list: list[int]) -> int:
    """Returns the maximum integer from a list."""
    i: int = 0
    current_max: int = int_list[0]
    if len(int_list) == 0:
        raise ValueError("max() arg is an empty list")
    else:
        while i < len(int_list):
            if current_max < int_list[i]:
                current_max = int_list[i]
            i += 1
    return current_max