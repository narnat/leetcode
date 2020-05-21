#!/usr/bin/env python3


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        ''' Efficient approach, traversing parts of the tree'''
        if root.left is None:
            return -1
        if root.left.val != root.val:
            candidate1 = root.left.val
            candidate2 = self.findSecondMinimumValue(root.right)
        elif root.right.val != root.val:
            candidate1 = root.right.val
            candidate2 = self.findSecondMinimumValue(root.left)
        else:
            candidate1 = self.findSecondMinimumValue(root.left)
            candidate2 = self.findSecondMinimumValue(root.right)
        if candidate1 >= 0 and candidate2 >= 0:
            return min(candidate1, candidate2)
        return max(candidate1, candidate2)


class Solution_2:
    ''' Similar to Solution1 but with global variables, self.min'''

    def findSecondMinimumValue(self, root: TreeNode) -> int:
        self.min = float('inf')
        self.helper(root)
        return self.min if self.min != float('inf') else -1

    def helper(self, root):
        if root.left is None:
            return
        if root.left.val != root.val:
            self.min = min(self.min, root.left.val)
            self.helper(root.right)
        elif root.right.val != root.val:
            self.min = min(self.min, root.right.val)
            self.helper(root.left)
        else:
            self.helper(root.left)
            self.helper(root.right)


class Solution_3:
    ''' Traversing the whole tree '''

    def findSecondMinimumValue(self, root: TreeNode) -> int:
        self.min = float('inf')
        self.helper(root)
        return self.min if self.min != float('inf') else -1

    def helper(self, root):
        if root.left is None:
            # There is also no right child
            return
        if root.left.val != root.val:
            self.min = min(self.min, root.left.val)
        elif root.right.val != root.val:
            self.min = min(self.min, root.right.val)
        self.helper(root.left)
        self.helper(root.right)
