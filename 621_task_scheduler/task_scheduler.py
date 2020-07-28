#!/usr/bin/env python3
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cooldown = [0] * 26
        count = [0] * 26

        max_count = 0
        m = 0
        for task in tasks:
            idx = ord(task) - ord('A')
            count[idx] += 1
            if m < count[idx]:
                m = count[idx]
                max_count = 1
            elif m == count[idx]:
                max_count += 1

        return max(len(tasks), (m - 1) * (n + 1) + max_count)


if __name__ == '__main__':
    scheduler = Solution().leastInterval
    print(scheduler(["A", "A", "A", "B", "B", "B"], 2))
