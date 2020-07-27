#!/usr/bin/env python3
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:

        def build(end):
            if self.postord < 0:
                return
            root = TreeNode(postorder[self.postord])
            self.postord -= 1
            if inorder[self.inord] != root.val:
                root.right = build(root)
            self.inord -= 1
            if end is None or inorder[self.inord] != end.val:
                root.left = build(end)
            return root

        self.postord = self.inord = len(inorder) - 1
        return build(None)


class Solution_2:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:

        def build(i_i, i_j, p_i, p_j):
            if i_i > i_j:
                return

            root = TreeNode(postorder[p_j])
            i = inorder_map[root.val]
            width = i - i_i - 1
            root.left = build(i_i, i - 1, p_i, p_i + width)
            root.right = build(i + 1, i_j, p_i + width + 1, p_j - 1)

            return root

        inorder_map = {inorder[i]: i for i in range(len(inorder))}

        n = len(inorder) - 1
        return build(0, n, 0, n)


class Solution_3:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:

        def build(i_i, i_j, p_i, p_j):
            if i_i > i_j:
                return

            if i_i == i_j:
                return TreeNode(inorder[i_i])

            root = TreeNode(postorder[p_j])
            i = 0
            for i in range(i_i, i_j + 1):
                if inorder[i] == root.val:
                    break
            width = i - i_i - 1
            root.left = build(i_i, i - 1, p_i, p_i + width)
            root.right = build(i + 1, i_j, p_i + width + 1, p_j - 1)

            return root

        n = len(inorder) - 1
        return build(0, n, 0, n)
