#!/usr/bin/python3
"""NQueens problem module."""


def n_queens(rows, columns):
    solutions = [[]]
    for row in range(rows):
        solutions = add_queen(row, columns, solutions)
    for i in range(len(solutions)):
        answer = []
        for j in range(len(solutions[0])):
            answer.append([j, solutions[i][j]])
        print(answer)
    return


def add_queen(new_row, columns, prev_sol):
    return [solution + [new_col]
            for solution in prev_sol
            for new_col in range(columns)
            if no_conflict(new_row, new_col, solution)]


def no_conflict(new_row, new_col, solution):
    return all(solution[row] != new_col and
               solution[row] + row != new_col + new_row and
               solution[row] - row != new_col - new_row
               for row in range(new_row))


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    n = 0
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)
    if n < 4:
        print("N must be at least 4")
        exit(1)
    n_queens(n, n)
