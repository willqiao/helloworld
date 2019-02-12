class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        
        data = {"2":["a","b","c"], "3":["d","e","f"], "4":["g","h","i"],"5":["j","k","l"], "6":["m","n","o"], "7":["p","q","r","s"], "8":["t","u","v"], "9":["w","x","y","z"]}
        totalStr = 1
        for char in digits:
            totalStr = totalStr*len(data[char])
        
        currentFactor = totalStr
        results = [["" for i in range(len(digits))] for j in range(totalStr)]
        for i in range(len(digits)):#239
            currentFactor = int(currentFactor/len(data[digits[i]])) #4
            currentIndex = 0
            for z in range(int(totalStr/currentFactor/len(data[digits[i]]))):#9
                for x in data[digits[i]]:#a,b,c4
                    for y in range(currentFactor):#repeating 1
                        results[currentIndex][i] = x
                        currentIndex += 1
            
                
        value = []
        for arr in results:
            value.append("".join(arr))
            
        return value
            
print(Solution().letterCombinations("23"))
                