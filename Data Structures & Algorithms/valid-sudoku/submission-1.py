class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        squares = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(len(board)):
            for j in range(len(board[0])):

                item = board[i][j]

                if item == ".": continue

                if item in rows[i] or item in columns[j] or item in squares[i // 3][j // 3]:
                    return False

                rows[i].add(item)
                columns[j].add(item)
                squares[i // 3][j // 3].add(item)      

        return True