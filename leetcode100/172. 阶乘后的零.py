#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：172. 阶乘后的零.py
@Author ：HuntingGame
@Date ：2023-02-07 20:34 
C'est la vie!!! enjoy ur day :D
'''
class Solution:
    def trailingZeroes(self, n: int) -> int:
        """
        这个题很好说，有多少个5的因子，那么一定就有多少个2的因子，那么就能配出来多少个10
        这个题变为了n的阶乘中有多少个5
        :param n:
        :return:
        """
        ans = 0
        while n !=0:
            n //=5
            ans +=n
        return ans