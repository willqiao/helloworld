class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.jump_help(nums, 0)
        
        
    def jump_help(self,nums,start):
        first = nums[start]
        max = 0
        next = start
        if nums[start] >= len(nums)-1-start:
            if nums[start] == 0 or len(nums)-start == 1:
                return 0
            else:
                return 1
        
        for i in range(1,first+1):
            if max < i+nums[start + i]:
                max =  i+nums[start+i]
                next = start+i
        
        return 1 + self.jump_help(nums, next)
    
         

print(Solution().jump([2,4,3,1,1,1,3,1]))