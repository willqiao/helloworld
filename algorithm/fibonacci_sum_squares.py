# Uses python3
from sys import stdin

def fibonacci_sum_squares_naive(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    previous = 0
    current  = 1
    data = []
    
    data.append(0)
    data.append(1)
    result = 0
    for _ in range(n - 1):
        previous, current = current, (previous + current) % 10
        if len(data) > 2 and data[len(data)-1] == 0 and current == 1:
            del data[len(data)-1]
            break
        else:
            data.append(current)

    
    mysize = len(data)
#     print(data,mysize)
    times = n // mysize
    height = 0
    width = 0
    for index, num  in  enumerate(data):
        if index % 2 == 0:
            height += num
        else:
            width += num

    
    
    height = times* height
    width = times * width 
    
#     print(height, width)
    for i in range(2, n % mysize+1, 2):
        height += data[i]
    
    height += data[1]
    
#     print(height, width)    
    for i in range(1, n % mysize+1, 2):
        width += data[i]
    
#     print(height, width)
    return width * height % 10

if __name__ == '__main__':
    n = int(stdin.read())
#     n = 1234567890
    print(fibonacci_sum_squares_naive(n))
