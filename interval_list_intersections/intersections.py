#!/usr/bin/env python3
from typing import List


def intervalIntersection(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    m = len(A)
    n = len(B)

    i = j = 0
    res = []

    while i < m and j < n:
        print(i, j)
        if A[i][0] <= B[j][1] and B[j][0] <= A[i][1]:
            res.append([max(A[i][0], B[j][0]), min(A[i][1], B[j][1])])
        if A[i][1] < B[j][1]:
            i += 1
        else:
            j += 1

    return res


if __name__ == '__main__':
    A = [[0, 2], [5, 10], [13, 23], [24, 25]]
    B = [[1, 5], [8, 12], [15, 24], [25, 26]]

    print(intervalIntersection(A, B))
