# Given an array of positive numbers and a positive number ‘S’, find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0, if no such subarray exists.

# Brainstorming:
# S = 9
# [3, 1, 4, 6, 1, 5, 2, 10]

# window_start: 7
# window_end: 7
# window_sum: 10
# min_length: 1
import math

def SmallestSubArrayWithGivenSum(arr, S):

    n = len(arr)
    window_start = 0
    window_sum = 0
    min_length = math.inf

    for window_end in range(n):
        window_sum += arr[window_end]

        while window_sum >= S:
            min_length = min(min_length, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1
        
    if min_length == math.inf:
        return 0
    else:
        return min_length