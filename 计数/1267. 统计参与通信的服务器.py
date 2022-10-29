#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/10/29 15:48
# @Author  : HuntingGame
# @FileName: 1267. 统计参与通信的服务器.py
# @Software: PyCharm
# C'est la vie. Enjoy ur day ! :D
from typing import List


class Solution:

    def countServers(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0
        onecomputer = []
        for i in range(m):
            if sum(grid[i]) >1:
                ans +=sum(grid[i])
            else:
                onecomputer.append(i)

        for j in range(n):

            # 这个时候值需要统计一行只有一个的情况，因为其他的已经统计过了
            sumtmp = sum([each[j] for each in grid])
            sumrow = sum([grid[i][j] for i in onecomputer])
            if sumtmp >1:
                ans +=sumrow


        return ans
