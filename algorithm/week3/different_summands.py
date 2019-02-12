# Uses python3
import sys

def optimal_summands(n):
    summands = []
    #write your code here
    remain = n
    current = 0
    #2,     1 1
    
    while current + 1 <= remain :
        current = current +1
        summands.append(current)
        remain = remain - current
    
    summands[len(summands) -1 ] = summands[len(summands) -1 ]+remain          
    
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
#     n = 120300
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
