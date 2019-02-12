class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 1
        
        hasOne = False
        mymin = 0
        mymax = 0
        for num in nums:
            if num <= 0:
                continue
            else:
                if num == 1:
                    hasOne = True
                if num < mymin:
                    mymin = num
                if num > mymax:
                    mymax = num
        
        if hasOne == False:
            return 1
        
        if hasOne == True:
            myresult = [ 0 for i in range(mymax)]
            for num in nums:
                if num > 0:
                    myresult[num-1] = 1
            
            for index, result in enumerate(myresult):
                if result == 0:
                    return index + 1
                 
            return len(myresult) + 1 
        

print(Solution().firstMissingPositive([7,8,9,11,12]))