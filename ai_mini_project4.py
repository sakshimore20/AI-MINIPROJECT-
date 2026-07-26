# -*- coding: utf-8 -*-



#4. “Queen Puzzle” (N-Queens CSP)
'''🎯 Idea:

The user enters the number of queens.
The computer solves it using backtracking (Constraint Satisfaction).'''

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col or abs(board[i]-col) == abs(i-row):
            return False
    return True

def solve(board, row, n):
    if row == n:
        return True
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            if solve(board, row+1, n): return True
            board[row] = -1
    return False

def print_board(board, n):
    for r in range(n):
        line = ""
        for c in range(n):
            line += "Q " if board[r]==c else ". "
        print(line)
    print()

if __name__ == "__main__":
    n = int(input("Enter number of queens: "))
    board = [-1]*n
    if solve(board, 0, n):
        print("Solution:")
        print_board(board, n)
    else:
        print("No solution found.")
