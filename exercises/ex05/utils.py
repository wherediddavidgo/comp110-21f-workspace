"""List utility functions part 2."""

__author__ = "730407005"

# Define your functions below


def only_evens(int_list: list[int]) -> list[int]:
    """Takes list of ints as input and returns new list of just the evens."""
    i: int = 0
    output_list: list[int] = []
    while i < len(int_list):
        if int_list[i] % 2 == 0:
            output_list.append(int_list[i])
        i += 1
    return output_list


def sub(int_list: list[int], lower: int, upper: int) -> list[int]:
    """Takes list of ints and 2 indices as inputs, returns new list of items from old list between lower index inclusive and outer index exclusive."""
    i: int = lower
    output_list: list[int] = []
    if lower >= len(int_list) or lower < 0 or upper <= 0 or upper >= len(int_list) or len(int_list) == 0 or lower >= upper:
        return []
    else:
        while i < upper:
            output_list.append(int_list[i])
            i += 1
        return output_list


def concat(list_1: list[int], list_2: list[int]) -> list[int]:
    """Takes 2 lists of ints as inputs and returns new list of all items."""
    i: int = 0
    output_list: list[int] = []
    while i < len(list_1):
        output_list.append(list_1[i])
        i += 1
    i = 0
    while i < len(list_2):
        output_list.append(list_2[i])
        i += 1
    return output_list