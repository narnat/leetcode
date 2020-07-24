#!/usr/bin/env python3
from typing import List


class Solution:
    '''
    DFS solution
    Time: O(2 ^ (n - 2))
    '''

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph) - 1

        def dfs(arr, v):
            if v == n:
                output.append(arr[:])
                return
            for edge in graph[v]:
                arr.append(edge)
                dfs(arr, edge)
                arr.pop()

        output = []
        dfs([0], 0)
        return output
