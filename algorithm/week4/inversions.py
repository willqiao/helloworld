# Uses python3
import sys

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        b[left] = a[left]
        return number_of_inversions
    ave = (left + right) // 2
    
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    #write your code here
    lsa = b[left:ave]
    rsa = b[ave:right]
    temp = []

    while len(lsa) > 0 and len(rsa)>0:
        if lsa[0] <= rsa[0]:
            temp.append(lsa[0])
            del lsa[0]
        elif rsa[0] <= lsa[0]:
            if lsa[0]>rsa[0]:
                number_of_inversions+=len(lsa)
            temp.append(rsa[0])
            del rsa[0]
    
    if len(rsa) > 0:
        temp.extend(rsa)
    elif len(lsa) > 0:
        temp.extend(lsa)
    
    for num in temp:
        b[left] = num
        left+=1
#     return b
    return number_of_inversions

if __name__ == '__main__':
#     input = sys.stdin.read()
#     n, *a = list(map(int, input.split()))
#2,3, 9,2,9
#2,3, 2,9,9
    a = [4, 80, 70, 23, 9, 60, 68, 27, 66, 78, 12, 40, 52, 53, 44, 8, 49, 28, 18, 46, 21, 39, 51, 7, 87, 99, 69, 62, 84, 6, 79, 67, 14, 98, 83, 0, 96, 5, 82, 10, 26, 48, 3, 2, 15, 92, 11, 55, 63, 97, 43, 45, 81, 42, 95, 20, 25, 74, 24, 72, 91, 35, 86, 19, 75, 58, 71, 47, 76, 59, 64, 93, 17, 50, 56, 94, 90, 89, 32, 37, 34, 65, 1, 73, 41, 36, 57, 77, 30, 22, 13, 29, 38, 16, 88, 61, 31, 85, 33, 54]
    n = len(a)
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))
#     print(b)
