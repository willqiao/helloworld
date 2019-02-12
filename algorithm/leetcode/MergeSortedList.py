# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def __str__(self):
        return str(self.val)+"->" + str(self.next)

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        if len(lists) ==0:
            return None
        
        if len(lists) ==1:
            return lists[0]
        
        if len(lists) == 2:
            return self.mergeTwoLists(lists[0], lists[1])
        
        return self.mergeTwoLists(self.mergeKLists(lists[:len(lists)//2]), self.mergeKLists(lists[len(lists)//2:]))
        
        
    def mergeTwoLists(self, list1, list2):
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        small = list1 if list1.val <= list2.val else list2
        root = small
        large = list1 if list1.val > list2.val else list2
        
        while small != None:
            if small.next == None:
                small.next = large
                return root
            if small.next != None:
                if large == None:
                    return root
                else:
                    if large.val >= small.val and large.val <= small.next.val:#link this val
                        temp = small.next
                        temp2 = large.next 
                        small.next = large
                        small.next.next = temp
                        
                        small = small.next
                        large = temp2
                         
                    else: #move small forward
                        small = small.next
        
        return root
        


root = ListNode(1)
root.next = ListNode(5)
root.next.next = ListNode(6)
root.next.next.next = ListNode(9)

root2 = ListNode(3)
root2.next = ListNode(4)
root2.next.next = ListNode(4)
root2.next.next.next = ListNode(6)
root2.next.next.next.next = ListNode(8)

root4 = ListNode(1)
root4.next = ListNode(3)
root4.next.next = ListNode(4)
root4.next.next.next = ListNode(4)
root4.next.next.next.next = ListNode(5)
root4.next.next.next.next.next = ListNode(6)
root4.next.next.next.next.next.next = ListNode(6)
root4.next.next.next.next.next.next.next = ListNode(8)
root4.next.next.next.next.next.next.next.next = ListNode(9)

root3 = ListNode(2)
root3.next = ListNode(3)
root3.next.next = ListNode(5)
root3.next.next.next = ListNode(10)
root3.next.next.next.next = ListNode(15)

# print(Solution().mergeTwoLists(root4, root3))
print(Solution().mergeKLists([root, root2, root3]))
