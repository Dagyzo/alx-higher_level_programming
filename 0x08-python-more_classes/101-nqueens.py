#!/usr/bin/python3

import sys

def nqueens(N):
    # Initialize the board with all zeros
    board = [[0 for x in range(N)] for y in range(N)]

    # Helper function to check if a queen can be placed on the board
    def can_place(board, row, col):
        # Check if there is a queen in the same column
        for i in range(row):
            if board[i][col] == 1:
                return False

        # Check if there is a queen in the same diagonal (upper left)
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        # Check if there is a queen in the same diagonal (upper right)
        for i, j in zip(range(row, -1, -1), range(col, N, 1)):
            if board[i][j] == 1:
                return False

        # If all checks pass, it is safe to place a queen
        return True

    # Helper function to solve the N queens problem recursively
    def solve(board, row):
        # Base case: all queens have been placed
        if row == N:
            # Print the solution
            print('\n'.join([''.join(['Q' if x == 1 else '.' for x in row]) for row in board]))
            print()
            return

        # Try placing a queen in each column of the current row
        for col in range(N):
            if can_place(board, row, col):
                board[row][col] = 1
                solve(board, row+1)
                board[row][col] = 0

    # Start the recursion from the first row
    solve(board, 0)

# Parse the command line argument
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

# Call the nqueens function to solve the problem
nqueens(N)
