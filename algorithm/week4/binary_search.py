# Uses python3
import sys

def binary_search(a, x):
    left, right = 0, len(a)-1
    
    while left <= right:
        middle = (right - left)//2 + left
        if x == a[middle]:
            return middle
        elif x < a[middle]:
            left = left
            right = middle - 1
        elif x > a[middle]:
            left = middle + 1
            right = right
            
    return -1

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
#     data = [5, 1, 2, 3, 4, 5,5, 1, 2,3, 4, 5]
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
#     print(a)
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')
