# Uses python3
import sys
import itertools
from pprint import pprint

def partition3(A):
    if sum(A) % 3 != 0 or len(A) < 3:
        return 0
    
    subsum = sum(A)//3
    
    dp = [[[0 for _ in range(subsum+1) ] for _ in range(subsum+1)] for _ in range(len(A))]
    
    
    for k in range(len(A)):
        dp[k][A[k]][0] = 1
        dp[k][0][A[k]] = 1 
        dp[k][0][0] = 1
        
    for k in range(1, len(A)):
        for mysum1 in range(1, subsum+1):
            for mysum2 in range(1, subsum+1):
                
                dp[k][mysum1][mysum2] = (dp[k-1][mysum1 - A[k]][mysum2] if mysum1 - A[k] >= 0 else 0) | (dp[k-1][mysum1][mysum2 - A[k]] if mysum2 - A[k] >= 0 else 0) | (dp[k-1][mysum1][mysum2]) 
#                 print(k,mysum1, mysum2, subsum, dp[k][mysum1][mysum2], (dp[k-1][mysum1 - A[k]][mysum2] if mysum1 - A[k] >= 0 else 0), (dp[k-1][mysum1][mysum2 - A[k]] if mysum2 - A[k] >= 0 else 0), (dp[k-1][mysum1][mysum2]) )
#     
#     pprint(dp)
    return dp[len(A)-1][subsum][subsum]

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))
#     print(partition3([1,2,3,4,5,5,7,7,8,10,12,19,25]))

