"""Utils - helper functions for stooge sort (HW2).

This file defines helper functions that create random arrays to
be sorted by stooge sort and handle the I/O operations for stoogesort.py.

Thomas Banghart
Oregon State University
CS325 - Analysis of Algorithms (Fall 2020)
HW - 2
"""

import random

N_THRESHOLDS = [
    0,
    5,
    50, 
    100, 
    200, 
    400,
    600,
    800,
    1000,
]

def make_array(n):
    "Makes random arrays for mergeTime and insertTime"
    array = []
    for _ in range(n):
        array.append(random.randint(0, 10000))
    
    return array
    

def read_file():
    """
    Reads the contents of data.txt and returns arrays to be sorted.
    """
    array = []
    try:
        with open('data.txt', 'r') as file:
            for line in file.readlines():
                line_arr = [int(i) for i in line.strip().split()]
                array.append(line_arr[1:])
    except EnvironmentError:
        print("This program needs a \"data.txt\" file in the same directory to read from.")

    return array


def write_file(sort_type, arrays):
    "Writes sorted arrays to output file"
    file_name = "{}.out".format(sort_type)
    with open(file_name, 'w') as file:
        for array in arrays:
            for ele in array:
                file.write(str(ele))
                file.write(" ")
            file.write("\n")
