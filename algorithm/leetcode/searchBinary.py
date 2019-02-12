from math import floor
def search(arr, item):
    n = len(arr)
    start = 0
    end = n -1
    while end > start:
        index = floor((end - start)/2 + start)
        if arr[index] == item :
            return index
        elif arr[index] > item:
            end = index - 1
        elif arr[index] < item:
            start = index + 1
    
    return "Not Found"


print(search([1,2,3,4,5,6,7,8,9,10,11], 3))