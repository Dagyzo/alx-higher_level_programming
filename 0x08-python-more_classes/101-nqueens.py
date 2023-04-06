#!/usr/bin/python3
def print_board(board):
    for row in board:
        print([i for i, x in enumerate(row) if x == 1])

def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_nqueens(board, col, n, solutions):
    if col == n:
        solutions.append([i for i, row in enumerate(board) if 1 in row])
        return
    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_nqueens(board, col + 1, n, solutions)
            board[row][col] = 0

def nqueens(n):
    if not isinstance(n, int):
        print("N must be a number")
        exit(1)
    if n < 4:
        print("N must be at least 4")
        exit(1)
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_nqueens(board, 0, n, solutions)
    for solution in solutions:
        print(solution)
