#!/usr/bin/env python3
# Tested using anaconda python 3.7.3 on Manjaro Linux

"""
Goal: Create permutations of strings from a dynamic array of array,
taking a single element from each array.
Input: A CSV file, which can be loaded into an array of array.
Expected output: Comma separated strings of all permutations
Language: Any
Input CSV file:
Content of input.csv
‘a’, ‘b’, ‘c’
‘i’, ‘j’
‘x’, ‘y’
Output strings:
aix, aiy, ajx, ajy, bix, biy, bjx, bjy, cix, ciy, cjx, cjy
"""

from sys import argv
from csv import reader


def csv_to_matrix(filename):
    with open(filename, newline="") as csvfile:
        return [row for row in reader(csvfile)]


def permutations_partial(matrix):
    """Returns all permutations of elements of the first 2 rows of a matrix
    :param matrix: Array of arrays, each element a short string/character
    :returns: List of all possible permutations of elems in first 2 rows
    :rtype: A list of strings
    """
    # This is part 1; the next function implements this recursively
    for row in matrix:
        for elem in row:
            elem.strip()
    result_list = []
    for i in matrix[0]:
        for j in matrix[1]:
            result_list.append(i + j)
    return result_list


def recursive_permutations(matrix):
    """ Returns all possible permutations of a 2d array, taking 1 elem from each array.
    :param matrix: Array of arrays, each element a short string/character
    :returns: List of all permutations of elements taking 1 from each row
    :rtype: A list of strings
    """
    result = permutations_partial(matrix)
    for row in matrix[2:]:  # We already have the first two rows
        # So we take a slice of the matrix containing the remaining rows.
        result = permutations_partial([result, row])
    return result


"""
Explanatory note: This uses a recursive method.
When we add an additional row of elements, we can add each of those elements to any of the existing permutations
i.e the permutations possible with n+1 rows can be discovered by taking the possible permutations with n rows, and permuting them with the n+1th row.
"""


def main():
    if len(argv) >= 2:
        strings = sorted(recursive_permutations(csv_to_matrix(argv[1])))
        """
        Loads the csv file from arguments as a matrix
        Generates the list of possible permutations
        And sorts it in alphabetical order
        """
        print(", ".join(strings))  # Formatting for ease of reading.
    else:
        print("Please specify a CSV file to read from")


if __name__ == "__main__":
    main()
