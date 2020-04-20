#!/usr/bin/env python3
from pandas import *

class Solution:
    def minPathSum(self, grid):

        print(DataFrame(grid))
        for i in range(1, len(grid[0])):
            grid[0][i] += grid[0][i - 1]

        print(DataFrame(grid))
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                grid[i][0] += grid[i - 1][0]
                print(DataFrame(grid))
                grid[i][j] = min(grid[i - 1][j], grid[i][j - 1])
                print(DataFrame(grid))
                print("****************************************")

        return grid[i - 1][j  - 1]

if __name__ == '__main__':
    minPathSum = Solution().minPathSum

    grid = [[1,3,1],[1,5,1],[4,2,1]]
    print(minPathSum(grid))
