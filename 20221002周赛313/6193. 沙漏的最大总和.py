# @Time : 2022-10-02 10:53
# @Author : Phalange
# @File : 6193. 沙漏的最大总和.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        ans = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(0,m-2):
            for j in range(0,n-2):
                tmp = sum(sum(rows[j:j+3]) for rows in grid[i:i+3]) - grid[i+1][j] - grid[i+1][j+2]
                ans = max(tmp,ans)

        return ans


grid = [[6,2,1,3],[4,2,1,5],[9,2,8,7],[4,1,2,9]]
print(Solution().maxSum(grid))

