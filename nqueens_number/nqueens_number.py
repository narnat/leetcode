#!/usr/bin/env python3


class Solution:
    def totalNQueens(self, n):
        cols = [False] * n
        dg1 = [False] * (2 * n)
        dg2 = [False] * (2 * n)
        self.count = 0

        def solve_queens(cols, dg1, dg2, row):
            if row == n:
                self.count += 1
            else:
                for col in range(n):
                    d1 = col + row
                    d2 = col - row + n

                    if cols[col] or dg1[d1] or dg2[d2]:
                        continue
                    cols[col], dg1[d1], dg2[d2] = 3 * [True]
                    solve_queens(cols, dg1, dg2, row + 1)
                    cols[col], dg1[d1], dg2[d2] = 3 * [False]

        solve_queens(cols, dg1, dg2, 0)
        return self.count


if __name__ == '__main__':
    totalNQueeens = Solution().totalNQueens
    assert totalNQueeens(8) == 92
    assert totalNQueeens(4) == 2
    assert totalNQueeens(5) == 10
    print(totalNQueeens(15))
