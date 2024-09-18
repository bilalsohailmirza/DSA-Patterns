
def MaximumSubarraySum(arr, K):
    
    n = len(arr)
    window_start = 0
    max_sum, window_sum = 0, 0

    for window_end in range(n):  # -----> O(n)
        window_sum += arr[window_end]

        if window_end >= K-1: # ----> O(n)
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start]
            window_start += 1

    return max_sum


print(MaximumSubarraySum([2, 1, 5, 1, 3, 2], 3)) # ---> Output: 9
