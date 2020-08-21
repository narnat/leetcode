#!/usr/bin/env python3
from typing import List


class Solution:
    '''
    Using two pointer which start at opposite ends
    Time: O(n)
    Space: O(1)
    '''

    def sortArrayByParity(self, A: List[int]) -> List[int]:
        N = len(A)
        even, odd = 0, N - 1
        while even < odd:
            even_p = A[even] & 1
            odd_p = A[odd] & 1
            if (even_p == 1) and (odd_p & 1 == 0):
                A[even], A[odd] = A[odd], A[even]
                even += 1
                odd -= 1
            elif (even_p & 1 == 0) and (odd_p & 1 == 1):
                even += 1
                odd -= 1
            elif (even_p & 1 == 0):
                even += 1
            else:
                odd -= 1

        return A


class Solution_2:
    '''
    Using two pointer which start at the beginning, j will point to odds
    if not then it will be swapped with i
    Time: O(n)
    Space: O(1)
    '''

    def sortArrayByParity(self, A: List[int]) -> List[int]:
        N = len(A)
        i = 0
        for j in range(N):
            if A[j] & 1 == 0:
                A[j], A[i] = A[i], A[j]
                i += 1
        return A
