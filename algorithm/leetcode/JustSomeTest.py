arr = [2] + [4,6]
print(arr[3:])
"""
from collections import deque
import time
print(time.time())



10*20
bin(20)
arr = ["good job"*2," what's the matter"]
print("{0} this my job: {1} what the heck {2}".format(23,456, "myname"))
print(2,43)
f = lambda x,y : x+2*y
print(f(40,2))

def myfunc(str,val):
    print(str, val)
    pass
v = set()
v.add((1,2,3))
v.add((1,2,-1))
t = [1,2,3]
print(list(v), "tolist")

myfunc(str="test",val="f")


print(time.time())
from functools import partial
data = [2,43,5,6,3,2,4,5,6,7,8,3,55,457]
from collections import deque
import heapq
from pprint import pprint
import logging

def mydecorator(function):
    def wrapper(*args):
        print("before")
        function(*args)
        print("after")
    return wrapper

@mydecorator
def helloworld(str):
    print(str)
    
print('sum',sum(i for i in range(100)))
    

helloworld("tttttttttt")


test = partial(heapq.nlargest, 2)
print(test(data), "secondgood")

for  d , i in enumerate(reversed(data[:])):
    print(d, i)


"""










# 
# c = deque(maxlen=7)
# for i in range(10):
#     c.appendleft(i)
#     print(c)
# c.append(11)
# print(c)
# #print(heapq.nlargest(3, c, key))
# mydict = {'t':2,'tf':3}
# print(mydict)
# pprint(mydict)
# logger = logging.getLogger("mygod")
# fh = logging.FileHandler('spam.log')
# # fh.setLevel(logging.DEBUG)
# logger.addHandler(fh)
# logger.setLevel(logging.DEBUG)
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# fh.setFormatter(formatter)
# with open("test.txt", "w") as openfile:
#     logger.info("this is my first logging msga")
#     print(type(openfile))
#     openfile.write("""
#     This is
#     some test
#     Good Job
#     
#     """
#     )