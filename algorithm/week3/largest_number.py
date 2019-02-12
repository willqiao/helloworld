#Uses python3

import sys

def largest_number(a):
    #write your code here
    results = ""
    strings = [str(a[i]) for i in range(len(a))]
    
    while len(strings) != 0:
        max = strings[0]
        index = 0
        for i in range(1, len(strings)):
            if max+strings[i] < strings[i] + max:
                max =  strings[i]
                index = i
        results += max
#         print(strings, i, max, results)
        del strings[index]
            
    return results

#     res = ""
#     for x in a:
#         res += x
#     return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:] 
#     a = [925,9,91,92,98,852,859,815,83,87,86,8,1000]
    print(largest_number(a))
    
