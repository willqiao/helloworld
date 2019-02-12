
class Solution:
    def fabonacci(self, n):
        
        if n <=2:
            return 1
         
        last1 = 1
        last2 = 1
        sum = 0  
        for i in range(2, n):
            sum = last1+last2
            last2 = last1
            last1 = sum
        
        return sum
    

    
print(Solution().fabonacci(12))