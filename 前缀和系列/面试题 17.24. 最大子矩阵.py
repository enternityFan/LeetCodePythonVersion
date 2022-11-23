#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/23 13:02
# @Author  : HuntingGame
# @FileName: 面试题 17.24. 最大子矩阵.py
# @Software: PyCharm
# C'est la vie. Enjoy ur day ! :D
from typing import List


class Solution:
    def getMaxMatrix(self, matrix: List[List[int]]) -> List[int]:
        ans = [0] * 4
        m = len(matrix)
        n = len(matrix[0])
        maxval = -1000000000
        if m == 1 and n == 1:
            return ans

        for i in range(m):
            s = [0] * n

            for j in range(i,m):
                #j是结束的行号
                cur = 0
                tmp = 0
                for k in range(n):
                    s[k] +=matrix[j][k]
                    cur +=s[k]
                    if cur > maxval:
                        maxval = cur
                        print(maxval)
                        ans[0] = i
                        ans[2] = j
                        ans[3] = k
                        ans[1] = tmp
                    if cur <0:
                        cur = 0
                        tmp = k+1

        return ans

print(Solution().getMaxMatrix([[-1, -2, -9, 6], [8, -9, -3, -6], [2, 9, -7, -6]]))