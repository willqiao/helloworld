class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <=2:
            return 0
        
        
        dictleft = {}
        dictright = {}
        #finding left max
        for i in range(len(height)):
            if i==0:
                dictleft[0] = height[0]
            else:
                dictleft[i] = max(dictleft[i-1], height[i])
                
        for i in reversed(range(len(height))):
            if i==len(height)-1:
                dictright[i] = height[i]
            else:
                dictright[i] = max(dictright[i+1], height[i])
                
        allUnit = 0
#         print(dictright, dictleft)
        for i in range(len(height)):
            left = dictleft[i]
            right =  dictright[i]
            if height[i] < left and height[i] < right:
                allUnit += min(left, right) - height[i] 
        #find leftmax
        
        #find rightmax
        
        return allUnit
        


print(Solution().trap([5,2,1,2,1,5]))
# print(Solution().trap([9,6,8,8,5,6,3]))