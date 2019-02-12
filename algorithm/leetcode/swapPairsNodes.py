# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
    def __str__(self):
        return self.val + " Child : (" + self.next.__str__() + ")"

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        firstNode = head
        secondNode = head.next
        if secondNode == None:
            return head
        newhead = secondNode
        previous = ListNode("myown")
        previous.next = head
        
        while firstNode != None:
            
            if secondNode != None: # not end
                temp = secondNode.next
                secondNode.next = firstNode#link to 1
                firstNode.next = temp#link to 3
                previous.next = secondNode
                previous = firstNode
                if temp == None:
                    firstNode = None
                    secondNode = None
                    
                elif temp !=None:
                    firstNode = temp
                    secondNode = temp.next
            
            elif secondNode == None:#the end scenario
                break#do nothing
            
        return newhead
        
node = ListNode("root")
node.next = ListNode("second")
node.next.next = ListNode("third")
# node.next.next.next = ListNode("forth")
# node.next.next.next.next = ListNode("fifth")
# node.next.next.next.next.next = ListNode("sixth")

print(Solution().swapPairs(node))