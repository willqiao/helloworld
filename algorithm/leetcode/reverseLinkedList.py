class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
    def __str__(self):
        return "[" + self.val + "\n[" + str(self.next)+  "]\n]"

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        
        oldhead = head
        current1 = head
        current2 = current1.next
        while current2 != None:
            oldnext = current2.next
            current2.next = current1            
            
            current1 = current2
            current2 = oldnext
        
        oldhead.next = None
        return current1
    
#         myhead = head
#         if myhead == None or myhead.next == None:
#             return myhead
#         
#         mynext = self.reverseList(head.next)
#         newhead = mynext
#         while mynext.next != None:
#             mynext = mynext.next
#         
#         mynext.next = myhead
#         myhead.next = None
#         return newhead

head = ListNode("1")
head.next = ListNode("2")
head.next.next = ListNode("3")
head.next.next.next = ListNode("4")

print(Solution().reverseList(head)) 