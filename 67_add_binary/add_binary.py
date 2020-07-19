#!/usr/bin/env python3


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        output = []
        a_i, b_i = len(a) - 1, len(b) - 1
        carry = 0
        while a_i > -1 or b_i > -1:
            s = carry
            if a_i > -1:
                s += ord(a[a_i]) - ord('0')
            if b_i > -1:
                s += ord(b[b_i]) - ord('0')
            val = s & 1
            output.append(chr(ord('0') + val))
            carry = bool(s & 2)
            a_i -= 1
            b_i -= 1

        if carry:
            output.append('1')
        return "".join(output[::-1])
