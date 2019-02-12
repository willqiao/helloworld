#Uses python3

import sys

def max_dot_product(a, b):
    #write your code here
    res = 0
    
    while len(a) > 0:
        va = max(a)
        vb = max(b)
        res += va*vb
        a.remove(va)
        b.remove(vb)
    
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
#     data = [3,1,3,-5,-2,4,1]
    
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    
