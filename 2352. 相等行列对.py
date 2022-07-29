# @Time : 2022-07-29 11:41
# @Author : Phalange
# @File : 2352. 相等行列对.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0
        for i in range(m):
            Ri = grid[i]
            for j in range(n):
                Cj = [a[j] for a in grid]

                if Ri == Cj:
                    res +=1

        return res
