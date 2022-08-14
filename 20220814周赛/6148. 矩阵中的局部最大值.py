# @Time : 2022-08-14 10:30
# @Author : Phalange
# @File : 6148. 矩阵中的局部最大值.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        ans = [[0] * (n-2) for i in range(n-2)]

        for i in range(n-2):
            for j in range(n-2):
                ans[i][j] = max([max(grid[i][j:j+3]),max(grid[i+1][j:j+3]),max(grid[i+2][j:j+3])])
        return ans


grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
print(Solution().largestLocal(grid))