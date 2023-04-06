#!/usr/bin/python3
import sys


class NQueens:
    def __init__(self, n):
        self.n = n
        self.columns = []
        self.solutions = []

    def solve(self):
        self.place_queen(0)
        self.print_solutions()

    def place_queen(self, row):
        if row == self.n:
            self.solutions.append(list(self.columns))
        else:
            for col in range(self.n):
                if self.is_valid(row, col):
                    self.columns.append(col)
                    self.place_queen(row+1)
                    self.columns.pop()

    def is_valid(self, row, col):
        for r, c in enumerate(self.columns):
            if c == col or r-c == row-col or r+c == row+col:
                return False
        return True

    def print_solutions(self):
        for solution in self.solutions:
            print(solution)

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

    solver = NQueens(n)
    solver.solve()
