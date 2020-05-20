#!/usr/bin/env python3


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        ''' Iterative solution (Inorder traversal)'''
        from collections import deque
        stack = deque()
        prev = TreeNode(float('-inf'))
        while root or len(stack) > 0:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()

            if prev.val >= root.val:
                return False
            prev = root
            root = root.right

        return True

    def isValidBST_2(self, root: TreeNode) -> bool:
        ''' Recursive solution, with INT_MAX and INT_MIN'''
        def validate(node, min_val, max_val):
            if not node:
                return True
            return min_val < node.val < max_val and validate(node.left, min_val, node.val) and validate(node.right, node.val, max_val)

        return validate(root, float('-inf'), float('inf'))

    def isValidBST(self, root: TreeNode) -> bool:
        ''' Using prev node'''
        def validate(node):
            if not node:
                return True

            if not validate(node.left):
                return False
            if self.prev.val >= node.val:
                return False
            self.prev = node
            return validate(node.right)

        self.prev = TreeNode(float('-inf'))
        return validate(root)
