# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here
    total = 0
    if sum(w) <= W:
        return sum(w)
    dic = [[0 for i in range(len(w)+1)] for i in range(W+1) ]
#     print(dic)
    
    for i in range(len(w)+1):
        dic[0][i] = 0
    for i in range(W+1):
        dic[i][0] = 0
    
    for i in range(1, len(w)+1):
        for WC in range(1, W+1):
#             print((WC, i-1), (WC - w[i-1], i-1))
#             print(dic.get((WC, i-1)), dic.get((WC - w[i-1], i-1)) + w[i-1] if (WC - w[i-1] >= 0) else 0)
            dic[WC][ i] = max  (
                
                dic[WC][ i-1],
                
                dic[WC - w[i-1]][ i-1] + w[i-1] if (WC - w[i-1] >= 0) else 0
                
                )
    
    return dic[W][len(w)]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
#     print(optimal_weight(1020, [1,4,8,10,20,12,123,342,123,234]))
