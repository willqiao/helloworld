# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

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
    print(data,mysize)
    times = n // mysize
    remain = n % mysize
    result = times * sum(data)
    for i in range(remain+1):
        result += data[i]
        
    return result % 10

if __name__ == '__main__':
#     input = sys.stdin.read()
#     n = int(input)
    n = 100
    print(fibonacci_sum_naive(n))
