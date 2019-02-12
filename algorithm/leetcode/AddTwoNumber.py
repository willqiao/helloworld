# Definition for singly-linked list.
from Scripts.unicodedata import decimal
from _ast import Num
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
    def __str__(self):
        return str(self.val) + " " + self.next.__str__()

from decimal import *

class Solution:
    def listToNumber(self, l1):
        linkList = l1
        #find size
        value = 0
        index = 0
        linkList = l1
        while linkList.next != None :
            value += linkList.val * (10**index)
            linkList =linkList.next
            index = index +1 
            
        value += linkList.val * (10**(index))
        
        return value
    
    def numberToList(self, num):
        lists = list(str(num))
        firstNode = None
        listNode = None
        for index in reversed(range(lists.__len__())):
            if firstNode == None :
                firstNode = ListNode(int(lists[index]))
                listNode = firstNode
            else:
                listNode.next = ListNode(int(lists[index]))
                listNode = listNode.next
        
        return firstNode
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        value = self.listToNumber(l1) +self.listToNumber(l2)
        print("sum" + str(value))
        return self.numberToList(value)
    

l1 = ListNode(0)
l1.next = ListNode(6)
l1.next.next = ListNode(7)

l2 = ListNode(1)
l2.next = ListNode(2)
l2.next.next = ListNode(3)
l2.next.next.next = ListNode(4)

#print(Solution().listToNumber(l1));
print(19341684684684684684684684684684684684684684684684684684684807/10) 
#19341684684684683015530916228213141159688250409872191662325760
#print(int(19341684684684684684684684684684684684684684684684684684684807 / (10)) * 10)
print(Solution().numberToList(19341684684684684684684684684684684684684684684684684684684807))