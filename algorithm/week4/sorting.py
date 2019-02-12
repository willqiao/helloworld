# Uses python3
import sys
import random


def partition3(a, l, r):
    #write your code here
    p = a[l]
    pl = l
    pr = l
    l=l+1
    while l <= r and r >=0 and l< len(a):
        while l< len(a) and a[l] <= p:
            if a[l] == p:
                pr+=1
                l+=1
            else:
                #swap pl and l
                temp = a[pl]
                a[pl] = a[l]
                a[l] = temp
                #pl++, pr++
                pl+=1
                pr+=1
                l+=1
            
        while a[r] > p and r >= 0:
            r-=1
        
        if l < r and a[l]!=a[r]:
            #swap pl to l
            templ = a[l]
            a[l] = a[pl]
            #swap l to r
            tempr = a[r]
            a[r] = templ
            #swap r to pl
            a[pl] = tempr
            #pl++, pr++
            if tempr != p:
                pl+=1
            pr+=1
            l+=1
            r-=1
    
        
    return pl, pr  
    



def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    pl,pr = partition3(a, l, r)
#     print(a,pl,pr, l, r)
    if pl - 1 > l:
        randomized_quick_sort(a, l, pl - 1);
    if pr+1 < r:
        randomized_quick_sort(a, pr + 1, r);


if __name__ == '__main__':
#     input = sys.stdin.read()
#     n, *a = list(map(int, input.split()))
    a = [2]
    n = len(a)
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
