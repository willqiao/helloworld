class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        
        value = self.countAndSay(n-1)
        
        current = value[0]
        count = 0
        result = ""
        for num in value:
            if num == current:
                count+=1
            else:
                result += str(count) + current
                current = num
                count = 1
        result += str(count) + current
        
        return result
    
print(Solution().countAndSay(6))