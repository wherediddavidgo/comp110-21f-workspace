"""Utility functions."""

__author__ = "123456789"

from csv import DictReader
from typing import ItemsView

def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Reads csv file as list of dictionaries."""
    result: list[dict[str, str]] = []

    file_handle = open(filename, "r", encoding="utf8")

    csv_reader = DictReader(file_handle)

    for row in csv_reader:
        result.append(row)
    
    file_handle.close()
    return result


def column_values(rows: list[dict[str, str]], field: str) -> list[str]:
    """Returns all values in a single column."""
    column: list[str] = []

    for row in rows:
        column.append(row["difficulty"])
    
    return column


def columnar(rows: list[dict[str, str]]) -> dict[str, list[str]]:
    """Turns row-based table into column-based table."""
    columns: dict[str, list[str]] = {}
    items: list[str] = []

    for key in rows[0]:
        for row in rows:
            items.append(row[key])
            columns[key] = items
        items = []

    return columns


def head(columns_in: dict[str, list[str]], head_len: int) -> dict[str, list[str]]:
    """Returns the first N rows of a table."""
    columns_out: dict[str, list[str]] = {}

    if head_len > len(columns_in):
        return columns_in

    for key in columns_in:
        vals: list[str] = []
        for item in range(head_len):
            vals.append(columns_in[key][item])
        columns_out[key] = vals

    return columns_out


def select(columns_in: dict[str, list[str]], fields: list[str]) -> dict[str, list[str]]:
    """Returns a column-based table with a subset of fields from the original."""
    columns_out: dict[str, list[str]] = {}

    for field in fields:
        columns_out[field] = columns_in[field]
    
    return columns_out


def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combines 2 column-based tables."""
    columns_out: dict[str, list[str]] = {}

    for key in table_1:
        columns_out[key] = table_1[key]
    
    for key in table_2:
        columns_out[key] = table_2[key]

    return columns_out


def count(list_in: list[str]) -> dict[str, int]:
    """Counts each unique item in list."""
    dict_out: dict[str, int] = {}

    for item in list_in:
        if item not in dict_out:
            dict_out[item] = 1
        else:
            dict_out[item] += 1

    return dict_out


def create_filter(column_in: list[str], sel: str) -> list[int]:
    """Returns list indices of every item of a certain type."""
    indices: list[int] = []
    i: int = 0

    for item in column_in:
        if item == sel:
            indices.append(i)
        i += 1

    return indices


def filtered(column_in: list[str], filter_list: list[int]) -> list[str]:
    """Uses list of indices from create_filter and returns all items in a list with those indices."""
    column_out: list[str] = []
    i: int = 0

    while i < len(filter_list):
        column_out.append(column_in[filter_list[i]])
        i += 1

    return column_out


def averages(columns_in: dict[str, list[str]], key_type: str, value_type: str) -> dict[str, float]:
    """Takes columnar data, converts columns to integers, and returns dictionary of keys and average values."""
    averages: dict[str, float] = {}
    scores: dict[str, list[str]] = {}
    scores_int: dict[str, list[int]] = {}
    total: int = 0
    int_column: list[int] = []


    for row in columns_in[key_type]:
        if row not in scores:
            filter_list: list[int] = create_filter(columns_in[key_type], row)
            scores[row] = filtered(columns_in[value_type], filter_list)
    
    for column in scores:
        for i in scores[column]:
            if len(scores[column]) > 5:
                int_column.append(int(i))
                scores_int[column] = int_column
        int_column = []
        # print(scores[column])


    for column in scores_int:
        for i in scores_int[column]:
            total += i
        averages[column] = total / len(scores_int[column])
        total = 0

    return averages