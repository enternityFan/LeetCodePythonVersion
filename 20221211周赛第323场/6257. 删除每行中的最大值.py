#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/12/11 10:32
# @Author  : HuntingGame
# @FileName: 6257. 删除每行中的最大值.py
# @Software: PyCharm
# C'est la vie. Enjoy ur day ! :D
from typing import List


class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        grid2 = []
        for each in grid:
            each.sort()
        print(grid)
grid = [[1,2,4],[3,3,1]]
print(Solution().deleteGreatestValue(grid))