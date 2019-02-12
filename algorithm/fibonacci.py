# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n
    if n == 2:
        return 1
    
    last1 = 1
    last2 = 1
    #1, 1, 2, 3 
    
    sum = 0
    for _ in range(2, n):
        sum = last1+last2
        last2 = last1
        last1 = sum
    
    return sum

n = int(input())
print(calc_fib(n))
