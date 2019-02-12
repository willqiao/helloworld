from math import ceil, floor

def shellSort(arr):
    gap = len(arr)//2
    while gap > 0:
        i = 0
        while i < gap:
            gap_insertionSort(arr, i, gap)
            i += 1
        gap = gap//2
        print(gap)
    return arr

def gap_insertionSort(arr, start, gap):
    for i in range(start, len(arr), gap):
        for j in range(i+gap, len(arr), gap):
            if arr[j] < arr[i]:
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp
    

def mergeSort(arr):
    if len(arr) == 1:
        return arr
    middle = len(arr)//2
    left = mergeSort(arr[:middle])
    right = mergeSort(arr[middle:])
    i = 0
    l = 0
    r = 0
    for i in range(len(arr)):
        if l < len(left) and r < len(right):
            if left[l] < right[r]:
                arr[i] = left[l]
                l+=1
            else :
                arr[i] = right[r]
                r+=1
        
        elif l >= len(left) and r < len(right):
            arr[i] = right[r]
            r+=1

        elif r >= len(right) and l < len(left):
            arr[i] = left[l]
            l+=1
        
    return arr

def quickSort(arr):
    pass

def insertionSort(arr):
    pass

def bubbleSort(arr):
    pass









arr = [23,4,56,33,45,21,0,4,2,1]
# print(mergeSort(arr))
print(shellSort(arr))