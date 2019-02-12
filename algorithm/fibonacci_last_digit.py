# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    data = []
    data.append(0)
    data.append(1)
#     print(0, 0)
#     print(1, len(data))
    for _ in range(n - 1):
        previous, current = current, (previous + current) % 10
        
        if len(data) > 2 and data[len(data)-1] == 0 and current == 1:
            del data[len(data)-1]
            break
        else:
            data.append(current)
    
    mysize = len(data)
    return data[n % mysize]

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
#     n = 32730513
    print(get_fibonacci_last_digit_naive(n))
