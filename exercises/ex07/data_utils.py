"""Dictionary related utility functions."""

__author__ = "730439223"

# Define your functions below

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []

    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8") 

    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle) 
    
    # Loop through each of the rows: where row is going to be assigned a dictionary of string to string (where the key is column name and value is the value for that particular row).
    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources.
    file_handle.close()
    
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    # TODO

    # table is the list of dictionaries. And row is a dictionary where the string is the key and the value is the row column associated with it.
    for row in table:
        item: str = row[column]
        result.append(item)

    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    # TODO: More work!

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
        
    return result


def head(table: dict[str, list[str]], x: int) -> dict[str, list[str]]:
    """Produce a column based table with only the first N rows."""    
    result: dict[str, list[str]] = {}
    # myList: dict[str, list[str]] = table[0]
    # list[dict[str, list[str]]] = table[0]

    keys = table.keys()

    for key in keys:

        myList: list[str] = []
        counter: int = 0

        for columnVal in table[key]:
            if counter >= x:
                break
            counter += 1

            myList.append(columnVal)

        result[key] = myList
            
    return result

