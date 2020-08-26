#!/usr/bin/env python3
from typing import List


class Solution:
    '''
    Using DP
    Time: O(35 * n), n is num of travel days
    Space: O(30) -> O(1)
    '''
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [0] * 30

        def get_idx(idx, diff, days):
            if idx == 0:
                return 0
            cur_diff = 0
            i = idx
            while i > 0:
                tmp = days[i] - days[i - 1]
                if diff < cur_diff + tmp:
                    break
                cur_diff += tmp
                i -= 1
            return i

        for i in range(n):
            week = get_idx(i, 6, days)
            month = get_idx(i, 29, days)
            dp[(i + 1) % 30] = min(dp[i% 30] + costs[0], dp[week % 30] +
                                   costs[1], dp[month % 30] + costs[2])

        return dp[(i+1) % 30]


class Solution_2:
    '''
    DP solution, starting from first travel day till last travel day
    Time: O(dp[-1] - dp[0])
    Space: O(30)
    '''
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [0] * 30
        days_set = set(days)

        for i in range(days[0], days[-1] + 1):
            if i not in days_set:
                dp[i % 30] = dp[(i - 1) % 30]
            else:
                dp[i % 30] = min(dp[(i - 1) % 30] + costs[0],
                           dp[max(0, i - 7) % 30] + costs[1],
                           dp[max(0, i - 30) % 30] + costs[2])
        return dp[i % 30]
