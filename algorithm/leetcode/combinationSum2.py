class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        if len(candidates) == 0:
            return []
        
        results = []
        for index in range(len(candidates)):
            num = candidates[index]
            if num > target:
                continue
            subcandidate = candidates[:index] + candidates[index+1:]
            newtarget = target - num
            if newtarget == 0:
                temp = [num]
                results.append(temp)
            elif newtarget < 0:
                continue
            elif newtarget > 0:
                mylist = self.combinationSum2(subcandidate, newtarget)
                if len(mylist) == 0:
                    continue
                else:
                    for mlist in mylist:
                        temp = [num]
                        temp.extend(mlist)
                        results.append(temp)
        
        uniqueset = set()
        for mylist in results:
            uniqueset.add(tuple(sorted(mylist)))
         
        results = []
        for mytuple in uniqueset:
            results.append(list(mytuple))
        
        return results
    
   
        


print(Solution().combinationSum2([20,34,8,30,26,19,21,20,34,8,30,26,33,28,19,21,20,34,8,30,26,33,28,19,21,20,34,8,30,26,33,28,19,21,20,34,8,30,26,33,28,19,21,20,34,8,30,26,33,28,19,21,20,34,8,30,26,33,28,19,21,20,34,8,30,26,33,28,19,21,20,34,8,30,26,33,28,19,21,20,34,8,30,26,33,28,19,21,20,34,8,30,26,33,28,19,21,20,34,8,30,26,33,28,19,21,20,34,8,30,26,33,28,19,21,20,34,8,30,26,33,28,19,21,20,34,8,30,26,33,28,19,21,20,34,8,30,26,33,28,19,21,20,34,8,30,26,33,28,19,21,20,34,8,30,26,33,28,19,21,20,34,8,30,26,33,28,19,21,20,34,8,30,26,33,28,19,21,20,34,8,30,26,33,28,19,21,20,34,8,30,26,33,28,19,21,20,34,8,30,26,33,28,19,21,20,34,8,30,26,33,28,19,21,20,34,8,30,26,33,28,19,21,20,34,8,30,26,33,28,19,21,20,34,8,30,26,33,28,19,21,20,34,8,30,26,33,28,19,21,20,34,8,30,26,33,28,19,21,20,34,8,30,26,33,28,19,21,20,34,8,30,26,33,28,19,21,28,22,15,33,19,12,9,17,9,11,7,5,14,31,14,12,6,29,20,27,24,23,34,23,18,29,6,8,23,20,25,8,30,27,7,6,34,11,10,8,9,34,30,10],26))