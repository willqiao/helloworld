from pprint import pprint
def getAll(arrs):
    result = []
    
    n = len(arrs)
    if n == 1:
        return arrs[0]
    
    subs = getAll(arrs[1:])
    for char in arrs[0]:
        for postfix in subs:
            result.append(char + postfix)
    
    return result
    

pprint(len(getAll([["1",'2','3'], ['4','5'],['6','7','8','9']])))