class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        length = s.__len__()
        for index in range(length):
            subStr = s[index]
            for second in range(index+1, length):
                if subStr.find(s[second] ) < 0 :
                    subStr += s[second]
                else:
                    break
            temp = subStr.__len__()
            if temp > longest :
                longest = temp
        return longest


a = 'test'.find("s")
#print(Solution().lengthOfLongestSubstring("pwwkew"))
