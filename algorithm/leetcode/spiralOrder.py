class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        results = []
        self.spiralOrder_help(matrix, results)
        return results
    
    def spiralOrder_help(self, matrix,results):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        xlen = len(matrix)
        if xlen==0:
            return
        ylen = len(matrix[0])
        if ylen==0:
            return
        #remove top
        results.extend(matrix.pop(0))
        
        #remove right
        for mylist in matrix:
            if len(mylist) > 0:
                results.append(mylist.pop())
        
        #remove bottom
        if len(matrix) > 0:
            results.extend(reversed(matrix.pop()))
        
        #remove left
        for i in reversed(range(len(matrix))):
            if len(mylist) > 0:
                results.append(matrix[i].pop(0))
        
        self.spiralOrder_help(matrix, results)
        
print(Solution().spiralOrder([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]))