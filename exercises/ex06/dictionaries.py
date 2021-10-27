"""Practice with dictionaries."""

__author__ = "730407005"

# Define your functions below


def invert(dict_in: dict[str, str]) -> dict[str, str]:
    """Takes dictionary as input and returns dictionary with keys and values swapped."""
    dict_out: dict[str, str] = {}
    check_1: str
    check_2: str
    for key in dict_in:
        check_1 = key
        for key in dict_in:
            check_2 = key
            if dict_in[check_1] == dict_in[check_2] and check_1 != check_2:
                print(check_1 + " " + check_2)
                raise KeyError("Cannot have duplicate keys.")
    for key in dict_in:
        dict_out[dict_in[key]] = key
    return dict_out


def favorite_color(dict_in: dict[str, str]) -> str:
    """Counts the number of times each value appears in a dictionary and returns the most common value."""
    check_1: str
    check_2: str
    favorite: str = ""
    scores: dict[str, int] = {}
    for key in dict_in:
        check_1 = key
        if dict_in[key] not in scores:
            scores[dict_in[key]] = 1
        else:
            scores[dict_in[key]] += 1
    for key in scores:
        check_1 = key
        if favorite == "":
            favorite = key
        if scores[check_1] > scores[favorite]:
            favorite = check_1
    return favorite


def count(list_in: list[str]) -> dict[str, int]:
    """Counts the number of times identical items appear in a list."""
    dict_out: dict[str, int] = {}
    for item in list_in:
        if item not in dict_out:
            dict_out[item] = 1
        else:
            dict_out[item] += 1
    return dict_out