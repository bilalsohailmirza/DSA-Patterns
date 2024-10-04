# O(nlog(n))

# Merge Sort is an Example of nlogn algorithms

def MergeSort(arr):

    if len(arr) < 2:
        return arr
    
    middleIndex = len(arr) // 2

    leftArr = arr[:middleIndex]
    rightArr = arr[middleIndex:]

    return merge(MergeSort(leftArr), MergeSort(rightArr)) # 


def merge(leftArr, rightArr):

    resultArr = []
    leftIndex = 0
    rightIndex = 0

    while leftIndex < len(leftArr) and rightIndex < len(rightArr):

        if leftArr[leftIndex] < rightArr[rightIndex]:
            resultArr.append(leftArr[leftArr])

        else:
            resultArr.append(rightArr[rightIndex])


    return resultArr + leftArr[leftIndex:] + rightArr[rightIndex:]
    