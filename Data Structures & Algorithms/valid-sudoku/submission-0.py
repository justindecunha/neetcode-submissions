class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        '''
            0 - 9 row - array of sets
            0 - 9 column - array of sets

        '''

        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        squares = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(len(board)):
            for j in range(len(board[0])):

                item = board[i][j]

                if item == ".":
                    continue

                if item in rows[i]:
                    return False
                else:
                    rows[i].add(item)
                
                if item in columns[j]:
                    return False
                else:
                    columns[j].add(item)
                
                if item in squares[i // 3][j // 3]:
                    return False
                else:
                    squares[i // 3][j // 3].add(item)

        return True