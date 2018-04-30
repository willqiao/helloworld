test = [0,3,3,4,4,5,5,5,6,7]

    
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (nums.__len__() == 0):
            return 0
        
        index = 0
        
        for i in range(1, nums.__len__()):
            if (nums[index] < nums[i]):
                nums[index+1] = nums[i]
                index=index+1
        
        return index+1



print(Solution().removeDuplicates(test))
print(test)
