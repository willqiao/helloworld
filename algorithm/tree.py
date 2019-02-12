
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
    def __str__(self, level=0):
        value = '\t'*level + str(self.val) + "\n" 
        if self.left != None:
            value += self.left.__str__(level=level+1)
        else:
            value += '\t'* (level+1) + "None\n"
        if self.right != None:
            value += self.right.__str__(level=level+1)
        else:
            value += '\t'* (level+1) + "None\n"
        return value
    
    def level(self):
        if self.left == None and self.right == None:
            return 1
        
        value = 0
        if self.left != None and self.right != None:
            value = max(self.left.level(), self.right.level()) + 1
        
        if self.right != None and self.left == None:
            value = self.right.level() + 1
        
        if self.left != None and self.right == None:
            value = self.left.level() + 1
        
        return value
    
    def put(self, value):
        if value <= self.val:
            if self.left != None:
                self.left.put(value)
            else:
                #found
                self.left = TreeNode(value)
        elif value > self.val:
            if self.right != None:
                self.right.put(value)
            else:
                #found
                self.right = TreeNode(value) 
        
        
        return self


root = TreeNode(30)
#10, 20, 30, 110,120,130
root.put(10).put(20).put(40).put(90).put(60).put(70)
# root.left = TreeNode(20)
# root.left.left = TreeNode(10)
# root.left.right = TreeNode(30)
# root.right = TreeNode(120)
# root.right.left = TreeNode(110)
# root.right.right = TreeNode(130)
print(root)
print("level", root.level())