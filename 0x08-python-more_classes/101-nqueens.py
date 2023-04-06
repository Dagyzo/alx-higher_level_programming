#!/usr/bin/python3
import sys

def nqueens(N):
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    def solve(queens, xy_sum, xy_diff):
        row = len(queens)
        if row == N:
            print(queens)
            return
        
        for col in range(N):
            if col not in queens and row+col not in xy_sum and row-col not in xy_diff:
                solve(queens + [col], xy_sum + [row+col], xy_diff + [row-col])
    
    solve([], [], [])

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    nqueens(N)
