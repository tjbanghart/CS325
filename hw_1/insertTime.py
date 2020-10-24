"""Insertion Sort - sorts an array of integers in descending order.

This program tracks the run time for the 
insertion sort algorithm. It takes arrays of size n 
containing random integer values from 0 to 10000 to sort.  
It prints n and the running time of the algorithim. This output 
will be charted in a viz to track 

Thomas Banghart
Oregon State University
CS325 - Analysis of Algorithms (Fall 2020)
HW - 1
"""

from utils import make_array, N_THRESHOLDS
from time import process_time

def insertion_sort(arr):
    """
    Insertion sort in descending order. 
    This function was adapted from pseudocode found on pg. 17 of
    Introduction to Algorithms, Third Edition 
    by Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein.
    """
    start = process_time()

    for i in range(1, len(arr)):
        key = arr[i]
        while i > 0 and arr[i-1] < key:
            arr[i] = arr[i-1]
            i -= 1
        arr[i] = key
    
    stop = process_time()
    return stop - start


def main():
    print("N,TIME")
    for n in N_THRESHOLDS:
        arr = make_array(n)
        print("{0},{1}".format(n, insertion_sort(arr)))


if __name__ == "__main__":
    main()
