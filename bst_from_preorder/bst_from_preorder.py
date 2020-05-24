#!/usr/bin/env python3
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        self.idx = 0
        return self.bst(preorder, float('inf'))

    def bst(self, arr, limit):
        if self.idx == len(arr) or arr[self.idx] > limit:
            return None
        root = TreeNode(arr[self.idx])
        self.idx += 1
        root.left = self.bst(arr, root.val)
        root.right = self.bst(arr, limit)

        return root


class Solution_2:
    def bst(self, pre, minv, maxv):

        if self.cur_idx >= len(pre):
            return None
        val = pre[self.cur_idx]
        if (minv > val or val > maxv):
            return None

        node = TreeNode(val)
        self.cur_idx += 1

        if self.cur_idx < len(pre):
            node.left = self.bst(pre, minv, val)
            node.right = self.bst(pre, val, maxv)

        return node

    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        self.cur_idx = 0
        return self.bst(preorder, float('-inf'), float('inf'))


class Solution_3:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        self.root = None

        for i in preorder:
            self.bst_add(i)

        return self.root

    def bst_add(self, val):
        prev = None
        cur = self.root

        while cur:
            prev = cur
            if cur.val > val:
                cur = cur.left
            else:
                cur = cur.right

        if not prev:
            self.root = TreeNode(val)
        elif prev.val > val:
            prev.left = TreeNode(val)
        else:
            prev.right = TreeNode(val)
