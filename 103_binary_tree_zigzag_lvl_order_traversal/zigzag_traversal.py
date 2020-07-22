#!/usr/bin/env python3
from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ''' Using BFS and stack and queues'''

    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        q.append(root)
        output = []
        lvl = 0
        while len(q) > 0:
            lvl_size = len(q)
            arr = []
            while lvl_size:
                lvl_size -= 1
                if lvl % 2 == 0:
                    node = q.popleft()
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                else:
                    node = q.pop()
                    if node.right:
                        q.appendleft(node.right)
                    if node.left:
                        q.appendleft(node.left)

                arr.append(node.val)
            lvl += 1
            output.append(arr)
        return output
