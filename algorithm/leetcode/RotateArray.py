class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k > nums.__len__():
            k = k % 
            nums.__len__()  
        
        copynums = nums[:]
        
        for index in range(nums.__len__()):
            if (index - k < 0) :
                nums[index] =copynums[index - k + nums.__len__()]
            else:
                nums[index] =copynums[index - k]
                
        return nums

                         
print(Solution().rotate([1,2,3,4,5,6], 3))
                         1,2,3,4,5,6
                         6,5,4,3,2,1
                         4,5,6,1,2,3

class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        moveto = -1
        
        if k > nums.__len__():
            k = k % nums.__len__()
        
        for step in range( k ):
            for index in range(nums.__len__() - 1):
                swap = nums[index]
                nums[index] = nums[nums.__len__() -1]
                nums[nums.__len__() -1] = swap
        
        