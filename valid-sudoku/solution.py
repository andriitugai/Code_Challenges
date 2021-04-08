class Solution:
    def validSudoku(self, board):
        '''
        :type board: list of list of int
        :rtype: bool
        '''
        for row in range(9):
            s = set()
            l = []
            for col in range(9):
                d = board[row][col]
                if d != 0:
                    s.add(d)
                    l.append(d)
            if len(s) != len(l):
                print(f"row #{row}")
                return False

        for col in range(9):
            s = set()
            l = []
            for row in range(9):
                d = board[row][col]
                if d != 0:
                    s.add(d)
                    l.append(d)
            if len(s) != len(l):
                print(f"col #{col}")
                return False

        for n in range(9):
            s = set()
            l = []
            for i in range(3):
                for j in range(3):
                    d = board[n // 3 + i][n % 3 + j]
                    if d != 0:
                        s.add(d)
                        l.append(d)
            if len(s) != len(l):
                return False

            return True































