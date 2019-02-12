# Uses python3
import sys

def lcm_naive(a, b):
    small = min(a,b)
    large = max(a,b)
    gcd = 0
    while True:
        r = large % small 
        large = small
        small = r 
        if r == 0:
            gcd = large  
            break
    return int(a//gcd * b//gcd * gcd)


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
#     a, b = 226553150, 1023473145
    print(lcm_naive(a, b))

