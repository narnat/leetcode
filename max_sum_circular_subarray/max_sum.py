#!/usr/bin/env python3


class Solution:
    def maxSubarraySumCircular(self, A):
        '''
        Get kadane(A), minKadane(A), sum(A), return max(kadane(A), sum(A) - minKadane(A))
        '''
        local_max, max_sum = A[0], A[0]
        local_min, min_sum = A[0], A[0]
        total = A[0]
        for i in range(1, len(A)):
            local_max = max(local_max + A[i], A[i])
            max_sum = max(max_sum, local_max)
            local_min = min(local_min + A[i], A[i])
            min_sum = min(min_sum, local_min)
            total += A[i]

        return total != min_sum and max(max_sum, total - min_sum) or max_sum
