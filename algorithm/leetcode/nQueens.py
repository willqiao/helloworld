class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        results = []
        queens = []
        
        self.solveNQueens_help(queens, 0, n, results)
        
        total = []
        for myqueens in results:
            myresult = []
            for queen in myqueens:
                str = '....'
                str = str[:queen[1]] + 'Q' + str[queen[1]+1:]
                myresult.append(str)
            total.append(myresult)
        return total
        
    def solveNQueens_help(self, queens, index, n, results):
        if len(queens) == n:
            results.append(queens[:])
            return
        
        #init sq
        sq = [0 for i in range(n)] 
        for queen in queens:
            for y in range(n):
                
                sq[queen[1]] = 1
                
                space = index - queen[0]
                
                if 0 <=  queen[1] + space < n:
                    sq[queen[1] + space] = 1
                    
                if 0 <=  queen[1] - space < n:
                    sq[queen[1] - space] = 1
        
        
        for i in range(n):
            if sq[i] == 0:
                queens.append((index, i))
                
                self.solveNQueens_help(queens, index+1, n, results)
                
                queens.pop()
        
        

print(Solution().solveNQueens(4))