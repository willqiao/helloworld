class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]        
        """
        
        if len(nums) < 3:
            return []
        
        returnList = []
        result = set()
        negtive = {}
        positive = {}
        for num in nums:
            if num < 0 :
                if (negtive.get(num) == None) :
                    negtive[num] = 1
                else:
                    negtive[num] = negtive[num] + 1
            else:
                if (positive.get(num) == None) :
                    positive[num] = 1
                else:
                    positive[num] = positive[num] + 1
                    
        if (len(negtive)  == 0 or  len(positive) == 0) and positive.get(0) != None and positive.get(0) > 2:
            return [[0,0,0]]  
        
        for key1 in positive:
            for key2 in positive:
                if (key1 == key2 and positive[key1] == 1):
                    continue
                if negtive.get(-key1 - key2) != None:
                    result.add((-key1-key2, min(key1,key2), max(key1,key2)))
                    
        for key1 in negtive:
            for key2 in negtive:
                if (key1 == key2 and negtive[key1] == 1):
                    continue
                if positive.get(-key1 - key2) != None:
                    result.add((min(key1,key2), max(key1,key2), -key1-key2))
        
        if positive.get(0) != None and positive.get(0) > 2:
             result.add((0,0,0))
             
        
        for item in result:
            returnList.append(list(item))
            
        return returnList
        
        
print(Solution().threeSum([0,0,0]))