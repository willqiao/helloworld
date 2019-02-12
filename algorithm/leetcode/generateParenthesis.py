class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        value = set()
        
        if n == 1:
            return ["()"]
        
        for str in self.generateParenthesis(n-1):
            for i in range(len(str)):
                for j in range(i, len(str)+1):
                    if (self.validParenthesis(str[:i] + "("+str[i:j]+ ")"+ str[j:])):
                        value.add(str[:i] + "("+str[i:j]+ ")"+ str[j:])
        
        return sorted(list(value))
        
    def validParenthesis(self, str):
        stack = []
        index = 0
        for char in str:
            if char == "(":
                stack.append(char)
            elif char == ")" and len(stack) > 0:
                stack.pop()
            
            index+=1
        
        return index == len(str) and len(stack) == 0
        
print("test"[:0],"test"[0:2], "test"[2:4])
print("test"[0:1],"test"[0:0], "test"[0:4])            

print(Solution().generateParenthesis(4))
# print(Solution().validParenthesis("()()"))