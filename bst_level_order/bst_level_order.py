#!/usr/bin/env python3
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        from collections import deque
        queue = deque()
        res = []
        if not root:
            return res

        queue.append(root)

        while len(queue) > 0:
            size = len(queue)
            level = []
            while size:
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                size -= 1
            res.append(level)

        return res
