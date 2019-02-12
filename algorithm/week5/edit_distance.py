# Uses python3
def edit_distance(s, t):
    #write your code here
    dic = {}
    for i in range(len(s)+1):
        dic[(i, 0)]=i
        
    for j in range(len(t)+1):
        dic[(0, j)]=j
    
    
    i, j = 1,1
    
    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            total = dic[(i-1, j-1)] + 1
            previous = (i-1, j-1)
            if s[i-1] == t[j-1]:
                if dic[(i-1, j-1)] < total:
                    total = dic[(i-1, j-1)]
                    previous = (i-1, j-1)
            else:
                if total > dic[(i-1, j)] + 1:
                    total = dic[(i-1, j)] + 1
                    previous = (i-1, j)
                if total > dic[(i, j-1)] + 1:
                    total = dic[(i, j-1)] + 1
                    previous = (i, j-1)
            
            dic[(i, j)] = total
        
    
    return dic[(len(s), len(t))]
    

if __name__ == "__main__":
    
    print(edit_distance(input(), input()))
#     print(edit_distance("editing", "distance"))
