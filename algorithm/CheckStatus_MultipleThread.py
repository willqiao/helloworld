from bs4 import BeautifulSoup
import requests
import re
from datetime import date
import numpy
import random
import threading
import time
#http://www.freeproxylists.net/?c=US&s=rs

httpproxy = ['140.227.57.238:3128',
'140.227.60.114:3128',
'140.227.68.82:3128',
'140.227.69.27:3128',
'35.190.231.58:8080',
'108.61.186.207:8080']
from torrequest import TorRequest


  

def query(case, myresults, olddata,proxyIndex):
    global httpproxy, httpsproxy
    proxies = {
      'http': 'http://'+ httpproxy[proxyIndex]
    }
    
    url = "https://egov.uscis.gov/casestatus/mycasestatus.do"
    time.sleep(2)
    r = requests.post(url, data={'appReceiptNum':case}, proxies=proxies) # And done.
    
#     with TorRequest(proxy_port=9050, ctrl_port=9051, password='password')  as tr:
#         tr.reset_identity()
#         r = tr.post(url, data={'appReceiptNum':case})
#         print(r.text.encode(encoding='utf_8', errors='strict'))  # not your IP address
#         response = tr.get('http://ipecho.net/plain')
#         print(response.text)  # not your IP address
        
    
    content = str(r.text.encode(encoding='utf_8', errors='strict'))
    bs = BeautifulSoup(content, "html.parser")
    exform = re.compile(r'Form (.-\d*),') #form
    exdate = re.compile(r'On (\w* \d+, \d+),')
    exdate2 = re.compile(r'As of (\w* \d+, \d+),')
    
    fm = re.search(exform, str(bs.p.text.encode()))
    form, mdate = "", ""
    if fm:
        form = fm.group(1)
    dm = re.search(exdate, str(bs.p.text.encode()))
    if dm == None:
        dm = re.search(exdate2, str(bs.p.text.encode()))
    if dm : 
        mdate = dm.group(1).replace(",","")
    
    ischange = ""
#     print(olddata.get(case) == bs.h1.text, case, olddata.get(case), bs.h1.text)
    if olddata.get(case) != None and olddata.get(case)[0] == bs.h1.text:
        ischange = "No Change"
    else:
        ischange = "None"
        if olddata.get(case) != None:
            ischange = olddata.get(case)[0]
            form = olddata.get(case)[1]
        print(threading.current_thread().getName(), case, bs.h1.text, mdate, form, ischange, olddata.get(case))
    
    myresults.append([case, str(date.today()), bs.h1.text, mdate, form, ischange])

def threadRun(workqueue, results, olddata, proxyIndex):
    for case in workqueue:
        query(case, results, olddata, proxyIndex)
    
    

def checkCase(start, checknumber, numberofWorker):
    olddata = getOldData()
    prefix = start[:3]
    number = int(start[3:])
    workqueue = []
    for i in range(-checknumber//2, checknumber//2):
        workqueue.append(prefix + str(number + i))
    
    results = [[] for i in range(numberofWorker)]
    threads = []
    n = len(workqueue)
    for i in range(numberofWorker):
        step = int(n/numberofWorker)
        start = i * step
        end = (n -1 if i == numberofWorker -1 else (i+1) * step)
        
        tempqueue = workqueue[start:end]
        t = threading.Thread(target=threadRun, args=[tempqueue,results[i],olddata, i])
        threads.append(t)
        t.start()
        
    for i in threads:
        i.join()
    
    whole = []
    for data in results:
        whole.extend(data)
    
    return whole

def getOldData():
    from numpy import genfromtxt
    my_data = genfromtxt('C:\\GitHub\\helloworld\\algorithm\\my.csv', delimiter=',', names=None, dtype=None)
    dic = {}
    for dd in my_data:
        dic[dd[0].decode()] = (dd[2].decode(), dd[4].decode())
        
    return dic


results = checkCase("MSC1891003011", 800,5)
   
narray = numpy.asarray(results)
print(narray)
   
numpy.savetxt("my"+str(date.today())+".csv", narray, delimiter=',',fmt='%s')

