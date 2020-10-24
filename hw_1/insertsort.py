"""Insertion Sort - sorts an array of integers in descending order.

This program reads integers from a .txt file and sorts them using the
insertion sort algorithm. The sorted array is then outputed to "insert.out"

Thomas Banghart
Oregon State University
CS325 - Analysis of Algorithms (Fall 2020)
HW - 1
"""
from utils import read_file, write_file

def insertion_sort(arr):
    """
    Insertion sort in descending order. 
    This function was adapted from pseudocode found on pg. 17 of
    Introduction to Algorithms, Third Edition 
    by Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        while i > 0 and arr[i-1] < key:
            arr[i] = arr[i-1]
            i -= 1
        arr[i] = key


def main():
    "Main function for insertion sort - calls I/O and sort methods"
    arr = read_file()
    for line in arr:
        insertion_sort(line)
    write_file('insert', arr)


if __name__ == "__main__":
    main()
