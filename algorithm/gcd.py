# Uses python3
import sys

def gcd_naive(a, b):
    small = min(a,b)
    large = max(a,b)
    if large % small == 0:
        return small
    
    while True:
        r = large % small
        large = small
        small = r
        if r == 0:
            return large   
    
    return 1
#     current_gcd = 1
#     for d in range(2, min(a, b) + 1):
#         if a % d == 0 and b % d == 0:
#             if d > current_gcd:
#                 current_gcd = d
# 
#     return current_gcd

#100 /2 , 50, 25, 10, 5, 20

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
#     a,b = 28851538, 1183019
    print(gcd_naive(a, b))
