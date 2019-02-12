# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return a[left]
    
    middle = (right - left)//2 + left
    
    leftMajor = get_majority_element(a, left, middle)
    rightMajor = get_majority_element(a, middle+1, right)
    
#     print(leftMajor, rightMajor, a[left:right+1])
    
    if leftMajor == -1 and rightMajor == -1:
        return -1
    elif leftMajor == rightMajor:
        return leftMajor
    else:
        countleft = 0
        countright = 0
        for i in range(left, right+1):
            if a[i] == leftMajor:
                countleft+=1
            if a[i] == rightMajor:
                countright+=1
        if countleft > (right+1-left)//2:
            return leftMajor
        elif countright > (right+1-left)//2:
            return rightMajor
        else:
            return -1    
    
    #write your code here
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
#     n = 5
#     a = [1,2,2]
#     print(get_majority_element(a, 0, len(a)-1))
    if get_majority_element(a, 0, n-1) != -1:
        print(1)
    else:
        print(0)
