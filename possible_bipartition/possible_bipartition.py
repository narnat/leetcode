#!/usr/bin/env python3
from typing import List


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:

        matrix = [[0] * (N + 1) for _ in range(N + 1)]

        for bi in dislikes:
            matrix[bi[0]][bi[1]] = matrix[bi[1]][bi[0]] = 1

        color_table = [0] * (N + 1)

        def dfs(matrix, color_table, idx, color):
            color_table[idx] = color

            for i in range(1, len(matrix)):
                if matrix[idx][i] == 1:
                    if color_table[i] == color:
                        return False
                    if color_table[i] == 0 and not dfs(matrix, color_table, i, -color):
                        return False
            return True

        for i in range(1, N + 1):
            if color_table[i] == 0:
                if not dfs(matrix, color_table, i, 1):
                    return False

        return True
