# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def __str__(self):
        return self.val + " Child : (" + self.next.__str__() + ")"

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        size = 1
        node = head
        previous = None
        delete = None
        while (node.next != None):
            size +=1
            node = node.next
        
        if size == 1 and n == 1:
            return None
        if size == n and size > 1:
            return head.next
        
        i = 0
        node = head
        while (node != None):
            i +=1
            
            if i == size - n:
                previous = node
            if i == size - n +1 :
                delete = node
                
            node = node.next
                
        
        previous.next = delete.next
        
        return head
    
node = ListNode("root")
node.next = ListNode("second")
# node.next.next = ListNode("third")
# node.next.next.next = ListNode("forth")
# node.next.next.next.next = ListNode("fifth")
# node.next.next.next.next.next = ListNode("sixth")

print(node)
print(Solution().removeNthFromEnd(node, 2))
