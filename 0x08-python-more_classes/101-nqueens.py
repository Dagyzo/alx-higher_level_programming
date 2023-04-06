#!/usr/bin/env python3

import sys


def check_two_queens(new_queen_position, other_queen_position):
    """Check if two queens are attacking each other."""
    if new_queen_position[0] == other_queen_position[0] or new_queen_position[1] == other_queen_position[1]:
        return True
    elif abs(new_queen_position[0] - other_queen_position[0]) == abs(new_queen_position[1] - other_queen_position[1]):
        return True
    else:
        return False


def solve_nqueens(n):
    """Solve the N queens puzzle."""
    solutions = []

    def backtrack(queens):
        if len(queens) == n:
            solutions.append(queens)
            return
        row = len(queens)
        for col in range(n):
            if all(not check_two_queens((row, col), (r, c)) for r, c in queens):
                backtrack(queens + [(row, col)])

    backtrack([])
    return solutions


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(n)
    for s in solutions:
        print(' '.join(f"{r + 1}" for r, c in s))
