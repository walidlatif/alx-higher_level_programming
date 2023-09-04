#!/usr/bin/python3
"""Solve the N queens problem"""

import sys


def is_safe(board, row, col):
    """
    Check if a queen can be placed on board[row][col]

    Args:
    board -- the current state of the chessboard
    row -- the row to check
    col -- the column to check

    Returns:
    True if a queen can be placed at (row, col), False otherwise
    """

    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, col, solutions):
    """
    Solve the N queens problem recursively.

    Args:
        board: The N x N chessboard represented as a 2D list.
        col: The current column being processed.
        solutions: A list to store the valid solutions.

    Returns:
        True if a solution is found, False otherwise.
    """
    N = len(board)

    if col == N:

        solution = [[i, j] for i in range(N)
                    for j in range(N) if board[i][j] == 1]
        solutions.append(solution)
        return True

    for row in range(N):
        if is_safe(board, row, col):

            board[row][col] = 1

            solve_nqueens(board, col + 1, solutions)

            board[row][col] = 0


def print_solutions(solutions):
    """
    Print all solutions

    Args:
        solutions (list): List of solutions to be printed
    """
    for solution in solutions:
        print(solution)


if __name__ == "__main__":

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

    board = [[0] * N for _ in range(N)]
    solutions = []
    solve_nqueens(board, 0, solutions)

    print_solutions(solutions)
