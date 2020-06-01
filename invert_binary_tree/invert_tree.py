#!/usr/bin/env python3


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        from collections import deque
        queue = deque()
        if root is None:
            return root
        queue.append(root)
        while len(queue) > 0:
            level_size = len(queue)
            while level_size:
                level_size -= 1
                node = queue.popleft()
                node.left, node.right = node.right, node.left
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root


class Solution_2:
    def invertTree(self, root: TreeNode) -> TreeNode:
        from collections import deque
        queue = deque()
        queue.append(root)

        while len(queue) > 0:
            node = queue.popleft()
            if node:
                node.left, node.right = node.right, node.left
                queue.append(node.left)
                queue.append(node.right)
        return root


class Solution_3:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            left = self.invertTree(root.right)
            right = self.invertTree(root.left)
            root.left, root.right = left, right
        return root
