#!/usr/bin/env python3


class Solution:
    def dailyTemperatures_0(self, T: List[int]) -> List[int]:
        '''
        Since we know the max size of stack, we can use array of that size
        and have a variable to track the last element of a stack
        '''
        from collections import deque
        res = [0] * len(T)
        stack = [0] * len(T)
        top = 0
        for i in range(len(T)):
            while top > 0 and T[stack[top]] < T[i]:
                idx = stack[top]
                top -= 1
                res[idx] = i - idx
            top += 1
            stack[top] = i

        return res

    def dailyTemperatures(self, T):
        ''' Version where pushing only indexes onto stack'''
        from collections import deque
        res = [0] * len(T)
        stack = deque()

        for i in range(len(T)):
            while stack and T[stack[-1]] < T[i]:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)

        return res

    def dailyTemperatures_2(self, T: List[int]) -> List[int]:
        ''' Pushing index and value onto stack, inefficient (uses more memory)'''
        from collections import deque

        res = [0] * len(T)
        stack = deque()
        hi = len(T) - 1

        for i in range(len(T) - 1, -1, -1):
            while stack and stack[-1][0] <= T[i]:
                stack.pop()
            d = stack and stack[-1][1] - i or 0
            stack.append((T[i], i))
            res[i] = d

        return res


 def dailyTemperatures_3(self, T: List[int]) -> List[int]:
        from collections import deque
        ''' Pushing only indexes, working from the end of array'''
        res = [0] * len(T)
        stack = deque()

        for i in range(len(T) - 1, -1, -1):
            while stack and T[stack[-1]] <= T[i]:
                stack.pop()
            d = stack and (stack[-1] - i) or 0
            stack.append(i)
            res[i] = d

        return res
