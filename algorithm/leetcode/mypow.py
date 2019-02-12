class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        
        if n < 0:
            n = -n
            x = 1/x
            
        if n == 1:
            return x
        
        left = 1
        if n % 2 == 1:
            left = x
            n = n - 1
            
        num = self.myPow(x, n//2)
        
        return num* num *left
            
print(Solution().myPow(0.00001,2147483647))