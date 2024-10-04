
# Let's say we have 1 customer that is attended in 1 minutes
# 10 customers its gonna take 10^2 = 100 minutes
import random

arr = []
for i in range(20000):
    arr.append(random.randint(1, 500))
    # print(arr[i], end=" ")

n = len(arr)

for i in range(n): # O(n)
    for j in range(0, n - i - 1, ): # O(n)
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp

# n + n + n + n + n = n*n = n^2

print()
# print(arr)