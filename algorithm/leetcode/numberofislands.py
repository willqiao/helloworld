class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        l1 = len(grid)
        if l1 == 0:
            return 0
        l2 = len(grid[0])
        if l2 == 0:
            return 0
        count = 0
        for x in range(l1):
            for y in range(l2):
                if grid[x][y] == "1":
                    count = count + 1
                    self.flip(x, y, grid)
                    print(grid)
        return count
    
    def flip(self, x, y, grid):
        #3 ways:
        grid[x][y] = 0
        if y+1 < len(grid[0]) and grid[x][y+1] == "1":
            self.flip(x, y+1, grid)
        
        if x+1 < len(grid) and grid[x+1][y] == "1":
            self.flip(x+1, y, grid)
        
        if x-1 >= 0 and grid[x-1][y] == "1":
            self.flip(x-1, y, grid)
            
        if y-1 >= 0 and grid[x][y-1] == "1":
            self.flip(x, y-1, grid)
        
        return
        

print(Solution().numIslands([["1","1","1"],["0","1","0"],["1","1","1"]]))

