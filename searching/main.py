import math
def jump_sort(arr, searchvalue):
    """Jump sort algorithm"""
    # Find the block size to be jumped
    step = int(math.sqrt(len(arr)))
    # Find the block where element is present (if it is present)
    prev = 0
    while arr[min(step, len(arr))-1] < searchvalue:
        prev = step
        step += int(math.sqrt(len(arr)))
        if prev >= len(arr):
            return -1
    # Do a linear search for x in block beginning with prev.
    while arr[prev] < searchvalue:
        prev += 1
        # If we reached next block or end of array, element is not present.
        if prev == min(step, len(arr)):
            return -1
    # If element is found
    if arr[prev] == searchvalue:
        return prev
    return -1


jump_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)