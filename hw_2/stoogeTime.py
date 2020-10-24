"""Stooge Sort - sorts an array of integers in descending order.

This program tracks the run time for the 
stooge sort algorithm. It takes arrays of size n 
containing random integer values from 0 to 10000 to sort.  
It prints n and the running time of the algorithim. This output 
will be charted in a viz to track 

Thomas Banghart
Oregon State University
CS325 - Analysis of Algorithms (Fall 2020)
HW - 2
"""
import math
from utils import make_array, N_THRESHOLDS
from time import process_time

def stooge_sort(arr, lo, hi):
    """
    stooge sort in descending order. 
    This function was adapted from pseudocode found 
    in the prompt of HW2 Question 4.
    """
    start = process_time()
    n = hi - lo + 1
    #swap if two elements left and lo is less than hi (descending)
    if n == 2 and arr[lo] < arr[hi]:
        arr[lo], arr[hi] = arr[hi], arr[lo]
    # if more than two elements we need some recursive calls 
    elif n > 2:
        #get mid point
        m = int(math.ceil((2 * n)/3))
        # sort first 2/3 
        stooge_sort(arr, lo, lo+m-1)
        # sort second 2/3
        stooge_sort(arr, hi-m+1, hi)
        # go back to resort the first 2/3 if the above call changed order
        stooge_sort(arr, lo, lo+m-1)
    stop = process_time()
    return stop - start


def main():
    "Main function for stooge sort - calls I/O and sort methods"
    print("N,TIME")
    for n in N_THRESHOLDS:
        arr = make_array(n)
        print("{0},{1}".format(n, stooge_sort(arr, 0, len(arr)-1)))


if __name__ == "__main__":
    main()
