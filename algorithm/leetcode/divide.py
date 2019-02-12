class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend < - 2**31 or dividend > 2**31 - 1:
            return 2**31 - 1
        
        if dividend == - 2**31 and divisor == - 1:
            return 2**31 - 1
        
        if dividend == 2**31 and divisor == 1:
            return 2**31 - 1
        
        isPositive = True
        if dividend < 0:
            dividend = -dividend
            isPositive = False
            
        if divisor < 0:
            divisor = -divisor
            isPositive = not isPositive
            
        
        result = 1
        start = 1
        end = 1
        if divisor == 1:
            result = dividend
            if isPositive == False:
                return -result
            else:
                return result 
        
        while  end * divisor <= dividend :
            start = end
            end = end * 2
        
        
        result = start
        
        while end - start > 1 :
            mid = start + (end - start)//2
            if mid * divisor  > dividend:
                start = start
                end = mid
                result = start
            elif mid * divisor< dividend:
                start = mid
                end = end
                result = mid
            elif mid* divisor == dividend:
                result = mid
                break
            
        
#         result -= 1
        
        if isPositive == False:
            return -result
        else:
            return result
        
# print(Solution().divide(100,2))
print(Solution().divide(2147483647,2))