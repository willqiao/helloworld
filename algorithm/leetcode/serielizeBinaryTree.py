# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
    def __str__(self, *args, **kwargs):
        return str(self.val)  + "["+ str(self.left) + "," + str(self.right) +"]" 
    
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        myresult = []
        current = root
        
        self.travelNode(root, myresult)
        print(myresult)
        
        return str(myresult)
    
    def travelNode(self, node, arr):
        arr.append(node.val)
        if node.left != None:
            self.travelNode(node.left, arr)
        else:
            arr.append("null")
        
        if node.right != None:
            self.travelNode(node.right, arr)
        else:
            arr.append("null")
    
    
    def retravelNode(self, arr):
        if len(arr) ==0 :
            return None
        elif arr[0] == 'null':
            arr.pop(0)
            return None
        else:
            root = TreeNode(arr[0])
            arr.pop(0)
            root.left = self.retravelNode(arr)
            root.right = self.retravelNode(arr)
            return root
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        arr = (data[2:len(data)-2]).split("', '")
        print(len(arr))
        return self.retravelNode(arr)
#         return pickle.loads(data)

# Your Codec object will be instantiated and called as such:
root = TreeNode("0")
root.left = TreeNode("1")
root.right = TreeNode("2")
root.right.left = TreeNode("3")
root.right.right = TreeNode("4")
root.right.right.left = TreeNode("5")
codec = Codec()
print(codec.deserialize(codec.serialize(root)))