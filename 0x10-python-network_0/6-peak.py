#!/usr/bin/python3
"""python script to peak-finder algorithm that just find a peak
on unsorted list (1D array)
it doesn't have to be the max value or greatest peak
it just could be any peak if (one at least exist)
and if there a lot of peaks, finding any one of them is okay
I will use binary serch (divide and conquer algorithm
so we don't have to go for all elements
to get o(log(n)) complixity in this binary search
which is better than the linear complixity o(n)"""


def find_peak(list_of_integers):
    """unsorted list peak finder in python
    Returns a peak exist in a list of elements"""
    left_idx = 0
    right_idx = len(list_of_integers) - 1

    while (left_idx < right_idx):
        mid_idx = (left_idx + right_idx) // 2

        if (list_of_integers[mid_idx] < list_of_integers[mid_idx + 1]):
            left_idx = mid_idx + 1
        else:
            right_idx = mid_idx  # important

    return list_of_integers[left_idx]  # important
