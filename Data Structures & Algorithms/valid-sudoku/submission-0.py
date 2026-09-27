class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check rows
        for row in board:
            found = set()
            for num in row:
                if num in found:
                    return False
                else:
                    found.add(num)
        #check columns
        for index in range(len(board)):
            board[index]
        #check 3x3 boxes