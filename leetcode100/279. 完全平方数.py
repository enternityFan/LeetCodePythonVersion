#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：279. 完全平方数.py
@Author ：HuntingGame
@Date ：2023-02-08 19:24 
C'est la vie!!! enjoy ur day :D
'''
class Solution:
    def numSquares(self, n: int) -> int:
        """
        1)四平方和定理
        2）任何数消掉4的因子，结论不变。
        :param n:
        :return:
        """
        while n % 4 == 0:
            n //=4
        if n % 8 == 7:
            return 4
        a = 0
        while a * a <=n:
            b = int((n - a * a) ** 0.5)
            if a * a + b * b == n:
                return 2 if (a > 0 and b > 0 ) else 1
            a +=1
        return 3