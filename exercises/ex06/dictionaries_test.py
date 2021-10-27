"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730407005"


def test_invert_single_item() -> None:
    """Tests invert with a dictionary containing a single item."""
    dict_in: dict[str, str] = {"Key": "Value"}
    print("functioning")
    assert invert(dict_in) == {"Value": "Key"}


def test_invert_multiple_items() -> None:
    """Tests invert with a dictionary containing several items."""
    dict_in: dict[str, str] = {
        "Key 1": "Value 1", 
        "Key 2": "Value 2", 
        "Key 3": "Value 3", 
        "Key 4": "Value 4"}
    assert invert(dict_in) == {
        "Value 1": "Key 1",
        "Value 2": "Key 2",
        "Value 3": "Key 3",
        "Value 4": "Key 4"
    }


def test_invert_empty() -> None:
    """Tests whether invert returns empty dictionary when given empty dictionary."""
    dict_in: dict[str, str] = {}
    assert invert(dict_in) == {}


def test_favorite_color_equal_faves() -> None:
    """Checks that when there are two colors mentioned the same number of times, the favorite is the one that comes first."""
    dict_in: dict[str, str] = {
    "Vicki": "Blue", 
    "Norman": "Green", 
    "David": "Green",
    "Cecilia": "Blue"
    }
    assert favorite_color == "Blue"


def test_favorite_color_empty() -> None:
    """Checks that function returns nothing when given empty dictionary."""
    dict_in: dict[str, str] = {}
    assert favorite_color == ""


def test_favorite_color_more_than_two() -> None:
    """Tests function with more than two values."""
    dict_in: dict[str, str] = {
    "Vicki": "Blue", 
    "Norman": "Green", 
    "David": "Green",
    "Cecilia": "Blue",
    "Bella": "Orange",
    "Adin": "Green"
    }
    assert favorite_color == "Green"


def test_count_single_item() -> None:
    """Tests count with a list containing 1 item."""
    list_in: list[str] = ["a"]
    assert count(list_in) == {"a": 1}


def test_count_items_grouped() -> None:
    """Tests count when identical items are grouped together in list."""
    list_in: list[str] = ["a", "a", "a", "b", "d", "d", "d", "s", "s"]
    assert count(list_in) == {
        "a": 3,
        "b": 1,
        "d": 3,
        "s": 2
    }


def test_count_items_scattered() -> None:
    """Tests count when identical items are not necessarily together in list."""
    list_in: list[str] = ["s", "a", "d", "b", "d", "a", "d", "s", "a"]
    assert count(list_in) == {
        "a": 3,
        "b": 1,
        "d": 3,
        "s": 2
    }

