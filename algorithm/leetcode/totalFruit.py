class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        if len(tree) <= 2:
            return len(tree)
        big = 0
        for i in range(len(tree)):
            result = self.chooseFruit(tree, i)
            if result > big:
                big = result
        return big
        
    #[1,2,3,2,2]
    def chooseFruit(self, tree, startIndex):
        type = tree[startIndex]
        type2 = None
        currentType = type
        start = startIndex
        while (currentType == type or currentType == type2) and startIndex < len(tree):
            currentType = tree[startIndex]
            
            if (currentType!= type and type2 == None):
                type2 = currentType
            if (currentType == type or currentType == type2):
                startIndex = startIndex + 1
        
        return startIndex - start 
            
        
        

print(Solution().totalFruit([3,3,3,1,2,1,1,2,3,3,4]))