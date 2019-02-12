class Solution:
    def findDuplicates(self, nums):
        
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) < 2 :
            return []
        
        value = []
        
        for i in range(len(nums)):
            currentNum = nums[i]
            if currentNum < 0:
                currentNum = currentNum*-1
            
            if nums[currentNum-1] == currentNum and i != currentNum-1:
                value.append(currentNum)
            elif  nums[currentNum-1] < 0:
                value.append(currentNum)
            else :
                nums[currentNum-1] = nums[currentNum-1] * -1
#         return value
        
        return value
        
        
print(Solution().findDuplicates([13,8,5,3,20,12,3,20,5,16,9,19,12,11,13,19,11,1,10,2]))
# print(Solution().findDuplicates([1,1]))
print(Solution().findDuplicates([10,2,5,10,9,1,1,4,3,7]))
