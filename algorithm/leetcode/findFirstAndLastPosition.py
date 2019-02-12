class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums)== 0:
            return [-1,-1]
        if len(nums) == 1:
            return [-1,-1] if nums[0] != target else [0,0]
        
        start = 0 
        end = len(nums) - 1
        mid = (end - start) // 2 + start
        min = -1
        max = -1
        #find min
        while end >= start:
            if target < nums[mid]: #in left side
                start = start
                end = mid -1
                mid = (end - start) // 2 + start
                pass
            elif target > nums[mid]: #in right side
                start = mid + 1
                end = end
                mid = (end - start) // 2 + start
                pass
            elif target == nums[mid]: # in both side
                if target == nums[start]:
                    min = start
                    break
                if target > nums[start]:
                    start = start + 1
                    end = mid
                    mid = (end - start) // 2 + start
                pass
        
        start = 0 
        end = len(nums) - 1
        mid = (end - start) // 2 + start        
        #find max
        while end >= start:
            if target < nums[mid]: #in left side
                start = start
                end = mid -1
                mid = (end - start) // 2 + start
                pass
            elif target > nums[mid]: #in right side
                start = mid + 1
                end = end
                mid = (end - start) // 2 + start
                pass
            elif target == nums[mid]: # in both side
                if target == nums[end]:
                    max = end
                    break
                if target < nums[end]:
                    start = mid
                    end = end - 1
                    mid = (end - start) // 2 + start
                pass
            
        return [min, max]
        

print(Solution().searchRange([1,8,8], 8))