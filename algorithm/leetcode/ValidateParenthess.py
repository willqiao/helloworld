class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) %2 != 0:
            return False
        if s == "":
            return True
        
        left = set(["{","(","["])
        right = {"}":"{" ,")":"(", "]":"["}
        stack = []
        current = 0
        for i in range(len(s)):
            if s[i] in left:
                stack.append(s[i])
            elif len(stack) > 0:
                char = stack.pop()
                if char == right[s[i]]:
                    current = i
                    continue
                else:
                    return False
            
            current = i
                
        
        return len(stack) == 0 and current == len(s)-1
        
print(Solution().isValid(s="()"))