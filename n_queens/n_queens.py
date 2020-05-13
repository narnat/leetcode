#!/usr/bin/env python3


def n_queens(res, curr, row, n):

    def is_valid(curr, row):
        print(row, curr)
        for i in range(row):
            diff = abs(curr[i] - curr[row])
            if diff == 0 or diff == row - i:
                return False
        return True

    if row == n:
        res.append([i * '.' + 'Q' + (n - i - 1) * '.' for i in curr])
        return
    for col in range(n):
        curr[row] = col
        if is_valid(curr, row):
            n_queens(res, curr, row + 1, n)


def solveNQueens(n):
    res = []
    curr = [0] * n
    n_queens(res, curr, 0, n)
    return res


if __name__ == '__main__':
    res = solveNQueens(9)
    ans = [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]
