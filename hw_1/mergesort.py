"""Merge Sort - sorts an array of integers in descending order.

This program reads integers from a .txt file and sorts them using the
merge algorithm. The sorted array is then outputed to "merge.out"

Thomas Banghart
Oregon State University
CS325 - Analysis of Algorithms (Fall 2020)
HW - 1
"""

from utils import read_file, write_file


def merge(arr, left, right, mid):
    """
    Merge protion of "merge sort" in descending order. 
    This function was adapted from pseudocode found on pg. 31 of
    Introduction to Algorithms, Third Edition 
    by Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein.
    """
    # Copy main array into left and run sides
    left_sub_arr = arr[left:mid+1]
    right_sub_arr = arr[mid+1:right+1]

    # Create iterators for subarrays and for populating main array
    i = 0
    j = 0
    k = left

    # The book's pseudocode makes use of "sentinals" (null terminators) 
    # these are harder to replicate in Python than in C or C++ (no pointers)
    # rather than checking for null terminator to avoid an out of index memory access
    # we alter our loop to check when we exhaust one of the sub arrays 
    while i < len(left_sub_arr) and j < len(right_sub_arr):
        if left_sub_arr[i] >= right_sub_arr[j]:
            arr[k] = left_sub_arr[i]
            i += 1
        else:
            arr[k] = right_sub_arr[j]
            j += 1
        k += 1
    
    # Since we may have remaining elements in either array
    # we need to check both subarray
    while i < len(left_sub_arr):
        arr[k] = left_sub_arr[i]
        i += 1
        k += 1

    while j < len(right_sub_arr):
        arr[k] = right_sub_arr[j]
        j += 1
        k += 1

    return arr


def merge_sort(arr, left, right):
    """
    Merge sort in descending order. 
    This function was adapted from pseudocode found on pg. 34 of
    Introduction to Algorithms, Third Edition 
    by Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein.
    """
    # Checks if there are elements to sort, otherwise just return
    if left < right:
        # Get midpoint for array
        mid = (int((left + right)/2))
        # Merge sort left side of array
        merge_sort(arr, left, mid)
        # Merge sort right side of array
        merge_sort(arr, mid+1, right)
        # Call merge to start creating sorted array
        merge(arr, left, right, mid)

    return 


def main():
    "Main function for insertion sort - calls I/O and sort methods"
    arr = read_file()
    for line in arr:
        merge_sort(line, 0, len(line))
    write_file('merge', arr)


if __name__ == "__main__":
    main()
