"""Utility functions."""

__author__ = "123456789"

from csv import DictReader

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
        column.append(row[field])
    
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