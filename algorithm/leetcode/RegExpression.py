import re
from datetime import datetime, date
import time

print("test1")
time.sleep(2)

print("test2")

# def getOldData():
#     from numpy import genfromtxt
#     my_data = genfromtxt('C:\\GitHub\\helloworld\\algorithm\\my.csv', delimiter=',', names=True, dtype=None)
#     dic = {}
#     print(my_data)
#     for dd in my_data:
#         dic[dd[0]] = dd[2]
#         
#     return dic
# 
str = "On July 30, 2018, we ordered your new card for Receipt Number "
 
# ex = re.compile(r'Form (.-\d*),')#form
ex = re.compile(r'On (\w* \d\d, \d\d\d\d),')
ex2 = re.compile(r'As of (\w* \d*, \d\d\d\d),')
m = re.search(ex, str)
print(m.start(), m.end(), m.group(1))
# 
# 
# print( date.today())
# 
# getOldData()
