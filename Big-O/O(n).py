# O(n) simple means linear time complexity


def search_and_add(arr, value_to_search, value_to_add):
    result = 0
    for i in range(len(arr)): # 0 -> n - 1
        if arr[i] == value_to_search: # O(n)
            print("value Found!!!") # O(n)
            result = value_to_add + arr[i] # O(n)
            
    print("Found value after additoin: ", result)

    # T(n) = O(1) + O(n) + O(n) + O(n) + O(n) = O(3n + 1) = O(n)



arr = []
value_to_search = 864
value_to_add = 36

for i in range(10000):
    arr.append(i)

print("Initialization Complete")
search_and_add(arr, value_to_search=value_to_search, value_to_add=value_to_add)