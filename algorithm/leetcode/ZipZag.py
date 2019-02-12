class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        leng = len(s)
        if leng <= 1:
            return s
        
        interval = numRows*2 -2
        smallInterval = (numRows-2)*2
        next = 0
        value = ""
        while next < leng:
            value += s[next]
            next = next + interval
        
        for index in range(1, numRows - 1):
            next = index
            currentRow = index
            while next < leng:
                value += s[next]
                next = next + (numRows - (currentRow + 1)) * 2
                if next < leng:
                    value += s[next]
                    next = next + 2*(currentRow+1)-2
            
        next = numRows - 1
        while next < leng:
            value += s[next]
            next += interval
        
        
        return value
    
print(Solution().convert("abcdefghijkl", 3))