# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    

    previous = 0
    current  = 1
    data = []
    
    data.append(0)
    data.append(1)
    result = 0
    for _ in range(to - 1):
        previous, current = current, (previous + current) % 10
        if len(data) > 2 and data[len(data)-1] == 0 and current == 1:
            del data[len(data)-1]
            break
        else:
            data.append(current)

#     print(data)
    mysize = len(data)
    
    times = (to - from_) // mysize
    remain = (to - from_) % mysize
    result = times * sum(data)
    for i in range(remain+1):
        result += data[(from_+i) % mysize]
        
    return result % 10


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
#     from_, to = 1, 2
    print(fibonacci_partial_sum_naive(from_, to))