from bs4 import BeautifulSoup
import requests
import re
from datetime import date
import numpy
import time
import random

httpproxy = ['104.25.114.28:80',
'213.136.77.246:80',
'104.18.54.1:80',
'104.25.177.4:80',
'104.31.84.197:80',
'109.196.127.35:8888',
'162.243.107.120:3128',
'95.171.198.206:8080',
'61.5.207.102:80',
'101.50.1.2:80']


def query(case, results, olddata):
    global httpproxy, httpsproxy
    proxies = {
      'http': 'http://'+ httpproxy[random.randint(0,9)]
    }
#     proxies = {'http':'http://104.25.114.28:80'}
    
    url = "https://egov.uscis.gov/casestatus/mycasestatus.do"
#     time.sleep(2)
    r = requests.post(url, data={'appReceiptNum':case}, proxies=proxies) # And done.
    content = str(r.text.encode(encoding='utf_8', errors='strict'))
    bs = BeautifulSoup(content, "html.parser")
    exform = re.compile(r'Form (.-\d*),') #form
    exdate = re.compile(r'On (\w* \d\d, \d\d\d\d),')
    exdate2 = re.compile(r'As of (\w* \d*, \d\d\d\d),')
    
    fm = re.search(exform, str(bs.p.text.encode()))
    form, mdate = "", ""
    if fm:
        form = fm.group(1)
    dm = re.search(exdate, str(bs.p.text.encode()))
    if dm == None:
        dm = re.search(exdate2, str(bs.p.text.encode()))
    if dm : 
        mdate = dm.group(1).replace(",", "")
    
    ischange = ""
    print(olddata.get(case) == bs.h1.text, case, olddata.get(case), bs.h1.text)
    if olddata.get(case) == bs.h1.text:
        ischange = "No Change"
    else:
        ischange = olddata.get(case)
    print(case, str(date.today()), bs.h1.text, mdate, form, ischange)
    results.append([case, str(date.today()), bs.h1.text, mdate, form, ischange])


def checkCase(start, checknumber):
    olddata = getOldData()
    prefix = start[:3]
    number = int(start[3:])
    workqueue = []
    for i in range(-checknumber//2, checknumber//2):
        workqueue.append(prefix + str(number + i))
    
    results = []
    for case in workqueue:
        query(case, results, olddata)
    
    return results

def getOldData():
    from numpy import genfromtxt
    my_data = genfromtxt('C:\\GitHub\\helloworld\\algorithm\\my.csv', delimiter=',', names=True, dtype=None)
    dic = {}
    for dd in my_data:
        dic[dd[0].decode()] = dd[2].decode()
        
    return dic
results = checkCase("MSC1891003011", 500)
  
narray = numpy.asarray(results)
print(narray)
  
numpy.savetxt("my"+str(date.today())+".csv", narray, delimiter=',',fmt='%s')

