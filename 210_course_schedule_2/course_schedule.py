#!/usr/bin/env python3
from typing import List


class Solution:
    '''
    DFS solution to get topological sort of a graph
    Time: O(|V| ^ 2) as adjacency matrix is used
    Memory: O(|V|)
    '''

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_mat = [[0] * numCourses for _ in range(numCourses)]
        for pre in prerequisites:
            adj_mat[pre[0]][pre[1]] = 1

        visited = [0] * numCourses
        top_sort = []

        def dfs(course, visited, top_sort):
            visited[course] = 1  # Gray vertex

            for i in range(numCourses):
                if adj_mat[course][i] == 1:
                    if visited[i] == 1:
                        return False
                    if visited[i] == 0:
                        if dfs(i, visited, top_sort) is False:
                            return False

            visited[course] = 2
            top_sort.append(course)
            return True

        for i in range(numCourses):
            if visited[i] == 0:
                if not dfs(i, visited, top_sort):
                    return []
        return top_sort


class Solution_2:
    '''
    Stack Based, Kahn's Algorithm, Adjacency matrix
    '''

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import deque
        adj_mat = [[0] * numCourses for _ in range(numCourses)]
        indegree = [0] * numCourses
        top_sort = []
        for pre in prerequisites:
            adj_mat[pre[1]][pre[0]] = 1
            indegree[pre[0]] += 1
        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        while len(q) > 0:
            v = q.popleft()
            top_sort.append(v)
            for i in range(numCourses):
                if adj_mat[v][i]:
                    indegree[i] -= 1
                    if indegree[i] == 0:
                        q.append(i)
        return top_sort if len(top_sort) == numCourses else []


class Solution_3:
    ''' Kahn's Algorithm, using adjacency list'''

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import deque, defaultdict
        adj_list = defaultdict(list)
        indegree = {}

        for course, req in prerequisites:
            adj_list[req].append(course)
            indegree[course] = indegree.get(course, 0) + 1

        queue = deque([course for course in range(
            numCourses) if course not in indegree])
        order = []

        while len(queue) > 0:
            v = queue.popleft()
            order.append(v)
            for neighbor in adj_list[v]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return order if len(order) == numCourses else []
