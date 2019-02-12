# Uses python3
import sys

def get_change(m):
    #write your code here
    #1, 3, 4
    dic = {0:0, 1:1, 2:2, 3:1, 4:1}
    if m < 5:
        return dic[m]
    current = 5
    while current <= m:
        dic[current] = min ([dic[current - 1] + 1, dic[current - 3] + 1, dic[current - 4] + 1])        
        current +=1
    
    return dic[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
#     m = 34
    print(get_change(m))
