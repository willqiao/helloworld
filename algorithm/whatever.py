import re

my = """
On August 13, 2018, we ordered your new card for Receipt Number MSC1891003002, and will mail it to the address you gave us. If you move, go to www.uscis.gov/addresschange to give us your new mailing address
"""

exdate = re.compile(r'On (\w* \d+, \d+),')
exdate2 = re.compile(r'As of (\w* \d+, \d+),')

form, mdate = "a", "a"
dm = re.search(exdate, my)
if dm == None:
    dm = re.search(exdate2, my)
if dm != None: 
    mdate = dm.group(1).replace(",","")
    
print(mdate)