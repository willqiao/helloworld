class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        found = False
        ii = -1
        jj = -1
        for i in reversed(range(1, len(nums))):
            for j in reversed(range(i)):
                if nums[i] > nums[j] : #found, switch
                    if j > jj :
                        found = True
                        ii = i
                        jj = j
                    break
                
#             if found:
#                 break
            
        if found :
            #swap i 0 and j 
            temp = nums[ii]
            nums[ii] = nums[jj]
            nums[jj] = temp
            
            if jj < len(nums)-1:
                #sort from i    
                for i in range(jj+1, len(nums)):
                    for j in range(i+1, len(nums)):
                        if nums[i]> nums[j]:
                            temp = nums[i]
                            nums[i] = nums[j]
                            nums[j] = temp
                
        else :
            #sort from i    
            for i in range(len(nums)):
                for j in range(i+1, len(nums)):
                    if nums[i]> nums[j]:
                        temp = nums[i]
                        nums[i] = nums[j]
                        nums[j] = temp

        return nums
        
print(Solution().nextPermutation([4,2,0,2,3,2,0]))