#!/usr/bin/env python3


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ''' DFS '''
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left and root.left.left is None and root.left.right is None:
            return self.sumOfLeftLeaves(root.right) + root.left.val
        return self.sumOfLeftLeaves(root.right) + self.sumOfLeftLeaves(root.left)


class Solution_2:
    ''' BFS solution '''
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        from collections import deque
        if root is None:
            return 0
        q = deque([root])
        ans = 0
        while len(q) > 0:
            node = q.popleft()
            if node.left and node.left.left is None and node.left.right is None:
                ans += node.left.val
            elif node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return ans
