class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index in range(nums.__len__()):
            for second in range(index+1, nums.__len__()):
                if nums[index] + nums[second] == target:
                    return [index, second]
        
        
    

print(Solution().twoSum([7,9,10,2,4,5,6,8], 10))