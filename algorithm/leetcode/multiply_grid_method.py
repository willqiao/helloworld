class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        total = 0
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                temp1 = int(num1[i1]) * (10**(len(num1) - i1 - 1))
                temp2 = int(num2[i2]) * (10**(len(num2) - i2 - 1))
                total += temp1*temp2
        return total
        
        

#     20, 3
#    
# 400   18 120
# 00  0  0
# 6  1200 8000


print(Solution().multiply("25", "50"))        