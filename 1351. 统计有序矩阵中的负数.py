# @Time : 2022-07-29 8:48
# @Author : Phalange
# @File : 1351. 统计有序矩阵中的负数.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            if grid[i][n-1] >=0:
                continue
            l = 0
            r = n

            pos =-1 # 记录位置，该位置表示第i行从此往后的第一个负数
            while l <=r:
                mid = l + (r - l) // 2
                if grid[i][mid] >=0:
                    l = mid+1
                elif grid[i][mid] <0:
                    r = mid-1
                    pos = mid

            count +=(n - pos)

        return count






grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
grid2 = [[5,1,0],[-5,-5,-5]]
s = Solution()
print(s.countNegatives(grid2))