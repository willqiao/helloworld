from math import floor
from copy import deepcopy
import pprint

class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        fullset = set(["1","2","3","4","5","6","7","8","9"])
        self.solveSudoku_help(board, [])        
        
    def valid(self, board):
        pass
    
    def findOptions(self, board, position):
        fullset = set(["1","2","3","4","5","6","7","8","9"])
        x = position[0]
        y = position[1]
        
        subxset = set()
        subyset = set()
        subcubeset = set()
        
        for i in range(9):
            if board[x][i] != '.':
                subxset.add(board[x][i])
            if board[i][y] != '.':
                subyset.add(board[i][y])
        
        for cubx in range(x//3*3, x//3*3+3):
            for cuby in range(y//3*3, y//3*3+3):
                if board[cubx][cuby] != '.':
                    subcubeset.add(board[cubx][cuby])
#         print('a1', position, (fullset - subxset - subyset - subcubeset))
#         print('a2',position, subxset, subyset, subcubeset)
        return (fullset - subxset - subyset - subcubeset)

    def solveSudoku_help(self, board, positionList):
        for x in range(9):
            for y in range(9):
                if board[x][y] == '.':
                    
                    options = self.findOptions(board, (x,y))
                    
                    if len(options) == 0:
                        return False
                    
                    found = False
                    for num in options:
                        board[x][y] = num
                        positionList.append((x,y))
                        
#                         print(board, positionList)
                        found = self.solveSudoku_help(board, positionList)
                        if found == True:
                            break
                                                                        
                        if found == False:
                            #reset
                            while True:
                                last = positionList.pop()
                                board[last[0]][last[1]] = '.'
                                if (last[0] == x and last[1] == y):
                                    break
                        
                    if found == False:
                        return False

        return True

board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

# board[0][5] = var
# print(Solution().findOptions(board, (8,8)))
print(Solution().solveSudoku(board))
pprint.pprint(board)
# pprint(rows)
# pprint(columns)
# pprint(blocks)
# pprint(mymap)







