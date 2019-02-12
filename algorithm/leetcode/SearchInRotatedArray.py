class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        s = 0
        e = len(nums) - 1
        m = e//2
        
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        
        
        while e-s>=1:
            if nums[s] <= nums[m] and (target >= nums[s] and target <= nums[m]):#left no pivot and inside
                if target == nums[m]:
                    return m
                elif target == nums[s]:
                    return s
                s = s
                e = m
            
            elif nums[s] > nums[m] and (target >= nums[s] or target <= nums[m]):#left has pivot and inside
                if target == nums[m]:
                    return m
                elif target == nums[s]:
                    return s
                s = s
                e = m
                
            elif nums[m+1] <= nums[e] and (target >= nums[m+1] and target <= nums[e]):#right no pivot and inside
                if target == nums[m+1]:
                    return m+1
                elif target == nums[e]:
                    return e
                s = m+1
                e = e
            elif nums[m+1] > nums[e] and (target >= nums[m+1] or target <= nums[e]):#right has pivot and inside
                if target == nums[m+1]:
                    return m+1
                elif target == nums[e]:
                    return e
                s = m+1
                e = e
            else:
                return -1
            
            m = (e - s)//2 + s
        
        return -1
        
        
print(Solution().search([1,3], 1))