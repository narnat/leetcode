#!/usr/bin/env python3


def removeKdigits(num, k):
    from collections import deque
    stack = deque()
    for i in num:
        print(stack, k)
        while len(stack) and k and stack[-1] > i:
            stack.pop()
            k -= 1
        stack.append(i)
    while k:
        stack.pop()
        k -= 1
    s = "".join(stack).lstrip('0')
    return s or '0'


if __name__ == '__main__':
    print(removeKdigits("1432219", 3))
    print(removeKdigits("10200", 1))
    print(removeKdigits("10", 2))
    print(removeKdigits("321", 3))
