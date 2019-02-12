class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        isMatch = False
        if p == "":
            return not bool(s)
        elif s != "" and (s[0]==p[0] or p[0] == '.'):
            isMatch = True
            
        if len(p) >=2 and p[1] =='*':
            return self.isMatch(s, p[2:]) or (isMatch and self.isMatch(s[1:], p))
        
        return isMatch and self.isMatch(s[1:], p[1:])

# print(Solution().isMatch("acad", "a.*."))
# print(Solution().isMatch("mississippi", "mis*is*p*."))
# print(Solution().isMatch("aab", "c*a*b"))
print(Solution().isMatch("aa", "a"))