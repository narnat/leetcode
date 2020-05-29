#!/usr/bin/env python3
from typing import List


class Solution:
    ''' Topological sort, DFS. Using coloring nodes'''

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        matrix = [[0] * numCourses for _ in range(numCourses)]
        UNVISITED, VISITING, VISITED = range(3)
        for i in prerequisites:
            matrix[i[0]][i[1]] = 1
        color = [UNVISITED] * numCourses

        def dfs(matrix, color, idx):
            color[idx] = 1

            for i in range(numCourses):
                if matrix[idx][i] == 1:
                    if color[i] == VISITING:
                        return False
                    if color[i] == UNVISITED:
                        if not dfs(matrix, color, i):
                            return False
            color[idx] = VISITED
            return True

        for i in range(numCourses):
            if color[i] == UNVISITED:
                if not dfs(matrix, color, i):
                    return False

        return True


class Solution_2:
    ''' Topological sort logic, Kahn's Algorithm, BFS'''

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import deque
        matrix = [[0] * numCourses for _ in range(numCourses)]
        indegree = [0] * numCourses
        for i in prerequisites:
            matrix[i[0]][i[1]] = 1
            indegree[i[1]] += 1
        queue = deque()

        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        count = 0
        while len(queue) > 0:
            v = queue.popleft()
            count += 1
            for i in range(numCourses):
                if matrix[v][i] == 1:
                    indegree[i] -= 1
                    if indegree[i] == 0:
                        queue.append(i)

        return count == numCourses
