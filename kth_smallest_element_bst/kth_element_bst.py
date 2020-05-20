#!/usr/bin/env python3


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        ''' Morris traversal, O(1) space'''
        cur = root
        while cur:
            if cur.left is None:
                # There is no left subtree, do not create any links
                # just print or decrement k
                k -= 1
                if k == 0:
                    return cur.val
                cur = cur.right
            else:
                pre = cur.left
                while pre.right and pre.right is not cur:
                    # Find predecessor of cur
                    pre = pre.right
                if pre.right is None:
                    # Create a temporary link from predecessor to cur, 1 pass
                    pre.right = cur
                    cur = cur.left
                else:
                    # Remove the link from predecessor to cur from 1 pass
                    # and print or decrement k
                    pre.right = None
                    k -= 1
                    if k == 0:
                        return cur.val
                    cur = cur.right

    def kthSmallest_2(self, root: TreeNode, k: int) -> int:
        ''' Iterative inorder'''
        from collections import deque
        stack = deque()
        while root or len(stack) > 0:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right

        return None

    def kthSmallest_3(self, root: TreeNode, k: int) -> int:
        ''' Recursive inorder '''
        self.k = k
        self.ans = None
        self.found = False
        self.inorder(root)
        return self.ans

    def inorder(self, root):
        if self.found:
            return
        if not root:
            return None
        self.inorder(root.left)
        self.k -= 1
        if self.k == 0:
            self.ans = root.val
            self.found = True
            return
        self.inorder(root.right)
