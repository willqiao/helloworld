class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        self.permuteUnique_help(sorted(nums), 0, results)
        
        return results
    def shouldSwap(self, nums, start, end):
        for i in range(start, end):
            if nums[i] == nums[end]:
                return False
        
        return True
    def permuteUnique_help(self, nums, start, results):
        if len(nums) == start+1:
            results.append(nums[:])
            return
        
        for i in range(start, len(nums)):
            #choose
            
            print(start, i, self.shouldSwap(nums, start, i), nums)
            if self.shouldSwap(nums, start, i):                                
                nums[start], nums[i] = nums[i], nums[start]
                
                self.permuteUnique_help(nums, start+1, results)
                
                #backtracking
                nums[start], nums[i] = nums[i], nums[start]
            
            
        
        
print(Solution().permuteUnique([2,2,1,1]))