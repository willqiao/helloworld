from audioop import reverse

class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        leng = len(matrix)
        if leng <= 1:
            return matrix
        index = 0
        for row in range(index, leng):
            for col in range(index, leng):
                temp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = temp
            
            index = index+1
        
        for row in range(leng):
            matrix[row] = matrix[row][::-1]
        
        

arr = [[7,4,1],[6,5,4],[9,3,7]]
print(Solution().rotate(arr))