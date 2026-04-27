class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            filtered_row = [x for x in row if x != '.']
            if len(set(filtered_row)) != len(filtered_row):
                return False
        
        for i in range(len(board)):
            col = []
            for row in board:
                col.append(row[i])

            filtered_col = [x for x in col if x != '.']
            if len(set(filtered_col)) != len(filtered_col):
                return False
        
        for i in range(3):
            for j in range(3):
                square = []
                square.extend(board[j*3][i*3:i*3+3])
                square.extend(board[j*3+1][i*3:i*3+3])
                square.extend(board[j*3+2][i*3:i*3+3])

                filtered_square = [x for x in square if x != '.']
                if len(set(filtered_square)) != len(filtered_square):
                    return False
        
        return True