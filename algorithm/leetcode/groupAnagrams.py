class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        mydict = {}
        for mystr in strs:
            key = str(sorted(mystr))
            if mydict.get(key) == None:
                mydict[key] = []
            
            mydict[key].append(mystr)
                
        
        return list(mydict.values())
        
        
print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))