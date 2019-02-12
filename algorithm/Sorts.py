import timeit
count = 0

from random import shuffle

## O(n2)
def sortInsertion(arr):
    global count
    for i in range(1, len(arr)):
        for j in reversed(range(1, i+1)):
            if arr[j] < arr[j-1]:
                
                count+=1
                temp = arr[j-1]
                arr[j-1]= arr[j]
                arr[j] = temp
            else:
                break
    
    return arr


def gapInsertionSort(arr, startPosition, gap):
    global count
    for i in range(startPosition + gap, len(arr), gap):
        for j in reversed(range(startPosition + gap, i +1, gap)):
            if arr[j] < arr[j-gap]:
                count+=1
                temp = arr[j]
                arr[j] = arr[j-gap]
                arr[j-gap] = temp
            else:
                break
        
    


def sortShell(arr):
    global count
    gap = len(arr)//2
    startPosition = 0
    while gap > 0:
        gapInsertionSort(arr, startPosition, gap)
        startPosition += 1
        if startPosition == gap:
            startPosition = 0
            gap = gap//2
            
    return arr



def sortMerge(arr):
    
    n = len(arr)
    if n ==1 :
        return arr
    leftList = sortMerge(arr[:n//2])
    rightList = sortMerge(arr[n//2:])
    
    global count
    l = 0
    r= 0
    k = 0
    
    while k < len(arr):
        if l >= len(leftList):
            arr[k] = rightList[r]
            r+=1
        elif r >= len(rightList):
            arr[k] = leftList[l]
            l+=1
        elif leftList[l] < rightList[r]:
            arr[k] = leftList[l]
            l += 1
        elif rightList[r] < leftList[l]:
            arr[k] = rightList[r]
            r+=1
        elif rightList[r] == leftList[l]:
            arr[k] = rightList[r]
            r+=1
            arr[k] = leftList[l]
            l+=1
        count+=1
        k +=1
    return arr



def sortQuick(arr, start, end):
    global count
    if start >= end:
        return arr
    
    p = start
    l = start + 1
    r = end
    while r > l:
        if arr[l] <= arr[p]:
            l+=1
        
        if arr[r] > arr[p]:
            r-=1
        
        if arr[l] > arr[p] and arr[r] < arr[p]:
            temp = arr[l]
            arr[l] = arr[r]
            arr[r] = temp
            r-=1
            l+=1
    
    if arr[r] < arr[p]:
        #swap pivot and r    
        temp = arr[p]
        arr[p] = arr[r]
        arr[r] = temp
        p = r
        
    count+=1
    
    
    sortQuick(arr, start, p-1)
    sortQuick(arr, p+1, end)    
    
    return arr


arr = list(range(10))
arr.append(1)
arr.append(1)
shuffle(arr)
arr = [6, 1, 4, 8, 5, 2, 9, 7, 3, 1, 0, 1]
# print(arr)

# start = timeit.default_timer()
# count = 0 
# sortInsertion(arr[:])
# print(count, "insertion used time:", timeit.default_timer() - start)#25114908 insertion used time: 10.354270775169725
#  
# start = timeit.default_timer()
# count = 0
# sortShell(arr[:])
# print(count, "shell used time:", timeit.default_timer() - start)#145120 shell used time: 0.16158501240464673
# 
# start = timeit.default_timer()
# count = 0
# sortMerge(arr[:])
# print(count, "merge used time:", timeit.default_timer() - start)#133616 merge used time: 0.0954855600944029 


start = timeit.default_timer()
count = 0 
print(sortQuick(arr[:], 0, len(arr) - 1))
print(count, "quick used time:", timeit.default_timer() - start)