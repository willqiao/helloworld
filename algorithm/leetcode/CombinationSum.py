class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(candidates)<=0:
            return [[]]
        
        result = []
        for num in candidates:
            newTarget = target - num
            
            if newTarget <0:
                continue
            elif newTarget ==0:
                temp = [num]
                result.append(temp) 
            else:
                mylist = self.combinationSum(candidates, newTarget)
                for eachList in mylist:
                    temp = [num]
                    temp.extend(eachList)
                    result.append(temp)
        
        
        myset = set()
        for mylist in result:
            myset.add(tuple(sorted(mylist)))
            
        result = []
        for myt in myset:
            result.append(list(myt))
        
        return result
        
print(Solution().combinationSum([2,3,6,7], 7))