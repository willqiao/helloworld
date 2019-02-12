class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l=len(nums)
        s=0
        for i in range(l):
            s=max(s,i+nums[i])
            if s>=(l-1):
                return True
            if i==s:
                break
        return False

# class Solution:
#     def canJump(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         maxindex = self.canJump_help(nums, 0)
#         if maxindex == len(nums)-1:
#             return True
#         else:
#             return False
#         
#         
#     def canJump_help(self, nums, start):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         if nums[start] == 0 or start == len(nums) -1:
#             return start
#         
#         maxv = start +nums[start]
#         maxIndex = start
#         for i in range(start, start+nums[start]+1):
#             if i >= len(nums):
#                 return len(nums) - 1
#             else:
#                 if i + nums[i] >= maxv and i > maxIndex:
#                     maxv = i+nums[i]
#                     maxIndex = i
#             
#             print(maxIndex, i)
#         
#         return self.canJump_help(nums, maxIndex)
                
        

print(Solution().canJump([1,5,1,1,1,0,1,1,3,1,0,0]))