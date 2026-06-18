class Solution:
    def isValid(self, nums: List[str]) -> bool:
        unique = set()
        for i in nums:
            if i in unique:
                return False
            if i == ".":
                continue
            unique.add(i)
        return True

    def getColumn(self, board: List[List[str]], column_num: int) -> List[str]:
        column = []
        for row in board:
            column.append(row[column_num])
        return column
    
    def getBox(self, board: List[List[str]], box_num: int) -> List[str]:
        box = []
        initial_col = (box_num * 3) % 9
        final_col = initial_col + 3
        initial_row = (box_num // 3) * 3
        final_row = initial_row + 3 
        for i in range(initial_row, final_row):
            for j in range(initial_col, final_col):
                box.append(board[i][j])
        return box

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            row = board[i]
            if not self.isValid(row):
                return False
            
            column = self.getColumn(board, i)
            if not self.isValid(column):
                return False
             
            box = self.getBox(board, i)
            if not self.isValid(box):
                return False
        
        return True
        