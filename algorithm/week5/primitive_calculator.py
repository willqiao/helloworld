# Uses python3
import sys

def optimal_sequence(n):
    #A + 1, 2A, or 3A
    dic = {1:[1], 2:[1,2], 3:[1,3]}
    if n < 4:
        return dic[n]
    current = 4    
    while current <=n :
        ops = len(dic[current - 1])
        previou = current -1
        
        if current % 3 == 0:
            ops = len(dic[current / 3])
            previou = current / 3
            
        elif current % 2 == 0:
            if ops > len(dic[current / 2]):
                ops = len(dic[current / 2])
                previou = current / 2
            
        
        arr = dic[previou][:]
        arr.append(current)
        dic[current] = arr
        
        current +=1
    
    sequence = dic[current-1]
#     print(dic)
    return sequence

input = sys.stdin.read()
n = int(input)
# n = 3
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
