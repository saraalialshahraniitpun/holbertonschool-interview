#!/usr/bin/python3
"""
A program that solves the N queens problem using backtracking.
"""
import sys


def print_usage_and_exit():
    """Prints usage message and exits with status 1."""
    print("Usage: nqueens N")
    sys.exit(1)


def validate_arguments():
    """Validates command-line arguments and returns N as an integer."""
    if len(sys.argv) != 2:
        print_usage_and_exit()

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    return n


def solve_n_queens(n):
    """Solves the N queens problem and prints all possible solutions."""
    def is_safe(row, col, board):
        """Checks if a queen can be placed at (row, col) safely."""
        for r in range(row):
            c = board[r]
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True

    def backtrack(row, board):
        """Recursive backtracking function to find solutions."""
        if row == n:
            # Format and print the solution as a list of coordinates
            solution = [[r, board[r]] for r in range(n)]
            print(solution)
            return

        for col in range(n):
            if is_safe(row, col, board):
                board[row] = col
                backtrack(row + 1, board)
                board[row] = -1

    board = [-1] * n
    backtrack(0, board)


if __name__ == "__main__":
    N = validate_arguments()
    solve_n_queens(N)
