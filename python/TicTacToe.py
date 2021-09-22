# Predict the winner of Tictactoe given the positions of two players
class Solution:
    def createBoard(self, moves):
        board = [[None,None,None] * (1) for i in range(3)]
        a = 0
        b = 1
        while a < len(moves) and b < len(moves):
            row = moves[a][0]
            col = moves[a][1]
            board[row][col] = 'X'
            row = moves[b][0]
            col = moves[b][1]
            board[row][col] = 'O'
            a += 2
            b += 2
            if a >= len(moves) and b >= len(moves):
                break
            if a >= len(moves):
                row = moves[b][0]
                col = moves[b][1]
                board[row][col] = 'O'
            elif b >= len(moves):
                row = moves[a][0]
                col = moves[a][1]
                board[row][col] = 'X'
        return board

    def tictactoe(self, moves):
        length = len(moves)
        if length < 3:
            return 'Pending'
        board = self.createBoard(moves)

        # Check Neg Diagonals
        if board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
            return 'A'

        if board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
            return 'B'

        # Check Neg Diagonals
        if board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':
            return 'A'

        if board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O':
            return 'B'

        for i in range(3):
            # Check Row
            if board[i][0] == 'X' and board[i][1] == 'X' and board[i][2] == 'X':
                return 'A'
            if board[i][0] == 'O' and board[i][1] == 'O' and board[i][2] == 'O':
                return 'B'
            # Check Col
            if board[0][i] == 'X' and board[1][i] == 'X' and board[2][i] == 'X':
                return 'A'
            if board[0][i] == 'O' and board[1][i] == 'O' and board[2][i] == 'O':
                return 'B'

        if length < 9:
            return 'Pending'
        else:
            return 'Draw'

if __name__ == '__main__':
    s= Solution()
    print(s.tictactoe([[0,0],[2,0],[1,1],[2,1],[2,2]]))