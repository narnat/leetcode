#!/usr/bin/env python3


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        def symmetric(n1, n2):
            if not n1 and not n2:
                return True
            if not n1 or not n2:
                return False
            return n1.val == n2.val and symmetric(n1.left, n2.right) and symmetric(n1.right, n2.left)
        return symmetric(root, root)


class Solution_2:
    def isSymmetric(self, root: TreeNode) -> bool:
        from collections import deque
        queue = deque([root, root])

        while len(queue) > 0:
            node1 = queue.popleft()
            node2 = queue.popleft()

            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False

            if node1.val != node2.val:
                return False

            queue.append(node1.left)
            queue.append(node2.right)
            queue.append(node1.right)
            queue.append(node2.left)

        return True
