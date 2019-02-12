# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        current = head
        if current == None or current.next == None:
            return False
        
        dic = {}
        dic[current] = True
        while current.next != None:
            if dic.get(current.next) == True:
                return True
            else :
                dic[current.next] = True            
            current = current.next
        return False
            
head = ListNode("1")
head.next = ListNode("2")
head.next.next = ListNode("3")
head.next.next.next = ListNode("4")
head.next.next.next.next = head.next.next
print(Solution().hasCycle(head))