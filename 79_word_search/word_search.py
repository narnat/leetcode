#!/usr/bin/env python3
from typing import List


class Solution:
    '''
    Using DFS, use board as a seen matrix
    Time: O(mn4^L) where L is len of a word
    Memory: O(L)
    '''

    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(x, y, idx):
            if idx >= l:
                return True
            if x not in range(0, n) or y not in range(0, m) or board[y][x] == '#' or board[y][x] != word[idx]:
                return False
            char, board[y][x] = board[y][x], '#'
            for x_i, y_i in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                if dfs(x + x_i, y + y_i, idx + 1):
                    return True
            board[y][x] = char
            return False

        m, n, l = len(board), len(board[0]), len(word)
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(j, i, 0):
                        return True
        return False
