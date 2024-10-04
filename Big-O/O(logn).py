# A logarithm has 2 componenets a base and an exponent
# Mostly in algorithms the base of the exponent is 2

def binarySearch(arr, start, end, target):

    midIndex = start + end // 2

    if start > end:
        return False

    
    if arr[midIndex] == target:
        return True
    
    if arr[midIndex] > target:
        return binarySearch(arr, start, midIndex + 1, target)
    
    else:
        return binarySearch(arr, midIndex + 1, end, target)
    

arr = [1, 1, 2, 3, 4, 5,     5, 7, 45, 89, 56]
arr.sort()

print(binarySearch(arr, 0, len(arr), 54))

# Call 1: arr, start=0, end=10, 1
# Call 2: arr. start=0, end=4, 1
# Call 3: arr, start=0, end=2, 1

# Input Size:
    # n=10, 
# Actual Complexity
# O(3)

# Generic Complexity:
# O(logn)

# 2^3.2  = 10