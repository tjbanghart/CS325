"""Stooge Sort - sorts an array of integers in descending order.

This program reads integers from a .txt file and sorts them using the
stooge sort algorithm. The sorted array is then outputed to "stooge.out"

Thomas Banghart
Oregon State University
CS325 - Analysis of Algorithms (Fall 2020)
HW - 2
"""
import math
from utils import read_file, write_file

def stooge_sort(arr, lo, hi):
    """
    stooge sort in descending order. 
    This function was adapted from pseudocode found 
    in the prompt of HW2 Question 4.
    """
    n = hi - lo + 1
    if n == 2 and arr[lo] < arr[hi]:
        arr[lo], arr[hi] = arr[hi], arr[lo]
    elif n > 2:
        m = int(math.ceil((2 * n)/3))
        stooge_sort(arr, lo, lo+m-1)
        stooge_sort(arr, hi-m+1, hi)
        stooge_sort(arr, lo, lo+m-1)


def main():
    "Main function for stooge sort - calls I/O and sort methods"
    arr = read_file()
    for line in arr:
        stooge_sort(line, 0, len(line)-1)
    write_file('stooge', arr)


if __name__ == "__main__":
    main()
