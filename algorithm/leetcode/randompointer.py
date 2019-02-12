# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
        
    def __str__(self, *args, **kwargs):
        return self.label + "[" + str(self.next) + "]" + "[" + self.random.__repr__() + "]"  

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head == None:
            return None
        
        objmap = {}
        current = head
        last = None     
        head = None
        while current != None: 
            copy = RandomListNode(current.label)
            objmap[current] = copy
            if last != None:
                last.next = copy
            else:
                head = copy
            last = copy            
                        
            current = current.next
        
        
        for key,value in objmap.items():
            if key.random != None:
                value.random = objmap[key.random]
                
        return head
        
    
tmp = RandomListNode("a")
tmp.next = RandomListNode("b")
tmp.next.next = RandomListNode("c")
tmp.next.next.next = RandomListNode("d")
tmp.next.next.next.next = RandomListNode("e")
tmp.random = tmp.next.next
tmp.next.random = None
tmp.next.next.random = tmp
tmp.next.next.next.random = None
tmp.next.next.next.next.random = tmp.next
print(tmp)
tmp2 = Solution().copyRandomList(tmp)
tmp2.next.next.label = "f"
print(tmp)
print(tmp2)

