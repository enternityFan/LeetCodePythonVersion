#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/13 19:45
# @Author  : HuntingGame
# @FileName: 1637. 两点之间不包含任何点的最宽垂直面积.py
# @Software: PyCharm
# C'est la vie. Enjoy ur day ! :D
from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])

        ans = 0

        for i in range(1, len(points)):
            ans = max(ans, points[i][0] - points[i - 1][0])

        return ans


