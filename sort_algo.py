from util import *
import math
import copy
import random


def swap_in_place(array, i, j):
    assert i >= 0 and i < len(array) and j >= 0 and j < len(array)
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp


# worst O(n^2); best O(n); incremental approach
def insertion_sort(array, reverse=False, in_place=True):
    n = len(array)
    if in_place:
        if not reverse:
            for i in range(1, n):
                key = array[i]
                j = i - 1
                while j >= 0 and array[j] > key:
                    swap_in_place(array, j, j+1)
                    j -= 1
                array[j+1] = key
        else:
            for i in range(n-2, -1, -1):
                key = array[i]
                j = i + 1
                while j < n and key < array[j]:
                    swap_in_place(array, j, j-1)
                    j += 1
                array[j-1] = key
    else:
        arr = copy.deepcopy(array)
        insertion_sort(arr, reverse, True)
        return arr


def test_insertion_sort():
    array = create_object_array([6,8,1,4,7,2,4,5,9])
    insertion_sort(array, True)
    print(array)


# worst O(n^2); best O(n^2)
def selection_sort(array, reverse=False, in_place=True):
    n = len(array)
    if in_place:
        for i in range(0, n-1):
            key = array[i]
            tmp = None
            idx = None
            for j in range(i+1, n):
                curr = array[j]
                if not reverse:
                    if tmp == None or curr < tmp:
                        tmp = curr
                        idx = j
                    if tmp < key:
                        swap_in_place(array, i, idx)
                else:
                    if tmp == None or curr > tmp:
                        tmp = curr
                        idx = j
                    if tmp > key:
                        swap_in_place(array, i, idx)
    else:
        arr = copy.deepcopy(array)
        selection_sort(arr, reverse, True)
        return arr


def test_selection_sort():
    array = create_object_array([6,8,1,4,7,2,4,5,9])
    arr = insertion_sort(array, False, False)
    print(arr)


# O(nlogn)
def merge_sort(array, reverse=False, in_place=True):
    if in_place:
        merge_sort_helper(array, 0, len(array), reverse)
    else:
        arr = copy.deepcopy(array)
        merge_sort(arr, 0, len(arr), reverse, True)
        return arr


#  divide - conquer - combine
def merge_sort_helper(array, p, r, reverse):
    
    if r - p > 1:
        q = int(math.floor((r + p) / 2))
        merge_sort_helper(array, p, q, reverse)
        merge_sort_helper(array, q, r, reverse)
        merge(array, p, q, r, reverse)


# O(n); conquer
def merge(array, p, q, r, reverse):
    left = array[p:q]
    right = array[q:r]
    if not reverse:
        left.append(Object(math.inf))
        right.append(Object(math.inf))
    else:
        left.append(Object(-math.inf))
        right.append(Object(-math.inf))
    i = 0
    j = 0
    if not reverse:
        for k in range(p, r):
            if left[i] <= right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
    else:
        for k in range(p, r):
            if left[i] >= right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1


def test_merge_sort():
    array = create_object_array([6,8,1,4,7,2,4,5,9])
    merge_sort(array, reverse=True)
    print(array)


# O(n^2)
def bubble_sort(array, reverse=False, in_place=True):
    if in_place:
        if not reverse:
            for i in range(0, len(array)):
                for j in range(len(array)-1, i, -1):
                    if array[j-1] > array[j]:
                        swap_in_place(array, j, j-1)
        else:
            for i in range(0, len(array)):
                for j in range(len(array)-1, i, -1):
                    if array[j-1] < array[j]:
                        swap_in_place(array, j, j-1)                   
    else:
        arr = copy.deepcopy(array)
        merge_sort(arr, reverse, True)
        return arr


def test_bubble_sort():
    array = create_object_array([6,8,1,4,7,2,4,5,9])
    arr = bubble_sort(array, True, False)
    print(arr)


test_insertion_sort()
test_selection_sort()
test_merge_sort()
test_bubble_sort()