#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：2240. 买钢笔和铅笔的方案数.py
@Author ：HuntingGame
@Date ：2022-10-20 9:32 
C'est la vie!!! enjoy ur day :D
'''


class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:

        ans = 0
        for i in range(total//cost1+1):

            ans +=(total - i * cost1)//cost2+1
        return ans

print(Solution().waysToBuyPensPencils(10000,1,1))
