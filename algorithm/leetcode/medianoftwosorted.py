class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged = []
        
        x = 0
        y = 0
        while x < len(nums1) and y < len(nums2):
            if nums1[x] <= nums2[y]:
                merged.append(nums1[x])
                x = x + 1
            elif nums1[x] > nums2[y]:
                merged.append(nums2[y])
                y = y + 1
        
        if x < len(nums1):
            merged.extend(nums1[x:])                    
        if y < len(nums2):
            merged.extend(nums2[y:])
        print(merged)
        if len(merged) % 2 == 0:
            return (merged[len(merged)//2 - 1] +merged[len(merged)//2]) /2
        else:
            return  merged[len(merged)//2]
        

print(Solution().findMedianSortedArrays([1,3,6], [2, 4,9]))