# Uses python3
import sys

def get_change(m):
    #write your code here
    coin10 = m // 10 
    r = m % 10
    coin5 = r // 5
    r = r % 5
    coin1 = r
    
    return coin10 + coin5 + coin1

if __name__ == '__main__':
    m = int(sys.stdin.read())
#     m = 28
    print(get_change(m))
