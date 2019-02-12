import math
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        isNegative = False
        if x < 0 : 
            isNegative = True
            x = -x
        
        original = str(x)
        originalList = list(original)
        value = ''
        for index in reversed(range(originalList.__len__())):
            value = value + originalList[index]
            
        if isNegative : 
            value = '-' + value
        
        finalyValue = int(value)
        
        if finalyValue > (2**31-1):
            return 0
        if finalyValue < (-2**31):
            return 0
        
        return finalyValue