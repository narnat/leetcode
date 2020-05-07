#!/usr/bin/env python3


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root, x, y):
        from queue import Queue

        q = Queue(root)
        q.put(root)

        is_x = is_y = False
        while not q.empty():
            size = q.qsize()

            while size:
                node = q.get()
                size -= 1
                is_x = True if node.val == x else is_x
                is_y = True if node.val == y else is_y

                if node.left and node.right:
                    if node.left.val == x and node.right.val == y:
                        return False
                    if node.right.val == x and node.left.val == y:
                        return False

                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
            if is_x and is_y:
                return True
            if is_x or is_y:
                return False

        return False

    def isCousins_2(self, root, x, y):
        """ My first solution"""
        from queue import Queue

        q = Queue()
        q.put(root)
        parent = None

        while not q.empty():
            size = q.qsize()

            while size:
                node = q.get()
                size -= 1

                if node.val == x or node.val == y:
                    val = x if node.val == y else y

                    while size:
                        cousin = q.get()
                        size -= 1
                        if cousin.val == val:
                            if parent and parent.left != node:
                                return True
                            return False
                    return False

                if node.left:
                    if node.left.val == x or node.left.val == y:
                        parent = node
                    q.put(node.left)
                if node.right:
                    if node.right.val == x or node.right.val == y:
                        parent = node
                    q.put(node.right)

        return False

    def isCousins_rec(self, root, x, y):
        """ Recursive solution, not that efficient"""
        def dfs(tree, depth, parent, val):
            if tree:
                if tree.val == val:
                    return depth, parent
                return dfs(tree.left, depth + 1, tree, val) or dfs(tree.right, depth + 1, tree, val)

        d1, p1 = dfs(root, 0, None, x)
        d2, p2 = dfs(root, 0, None, y)
        return d1 == d2 and p1 != p2

    def isCousins_rec_2(self, root, x, y):
        """ Optimized recursive solution"""
        def dfs(tree, depth, parent):
            if tree:
                if tree.val == x:
                    store[0] = (depth, parent)
                if tree.val == y:
                    store[1] = (depth, parent)
                dfs(tree.left, depth + 1, tree)
                dfs(tree.right, depth + 1, tree)

        store = [(0, 0), (-1, -1)]
        dfs(root, 0, None)
        d1, p1 = store[0]
        d2, p2 = store[1]
        return d1 == d2 and p1 != p2
