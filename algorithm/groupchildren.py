import random

def groupChildren(children):
    
    groups = []
    
    for child in children:
        join = False
        for group in groups:
            group.append(child)
            if max(group) - min(group) > 12:
                del group[len(group)-1]
            else:
                join = True
        
        if join == False:
            groups.append([child])
    
    print(len(groups))
    return groups


def groupChildren2(children):
    children = sorted(children)
    
    groups = []
    
    start = 0
    startNewGroup = True
    for i in range(len(children)):
        if i + 1 < len(children) and children[i] - children[start] <= 12 and children[i+1] - children[start] > 12:
            groups.append(children[start:i+1]) 
            start = i+1
        elif i + 1 == len(children) and children[i] - children[start] <= 12:
            groups.append(children[start:i+1]) 
            break
        elif i + 1 == len(children) and children[i] - children[start] > 12:
            groups.append(children[i:i+1]) 
            break    
             
    
    print(len(groups))
    return groups




# print(random.sample(range(1,12*6), 150))


print(groupChildren2([20, 52, 37, 7, 11, 26, 60, 34, 38, 4, 22, 17, 55, 21, 42, 48, 25, 15, 65, 66, 27, 57, 58, 30, 32, 6, 13, 40, 56, 50]))
# print(groupChildren([random.randint(1,12*6) for _ in range(250)]))