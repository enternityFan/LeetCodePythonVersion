#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：202. 快乐数.py
@Author ：HuntingGame
@Date ：2023-02-07 21:26 
C'est la vie!!! enjoy ur day :D
'''
class Solution:
    def isHappy(self, n: int) -> bool:
        """
        这是一个数学结论的解。。看不看都行。
        :param n:
        :return:
        """



        while n !=1 and n !=4:
            ans = 0
            while n!=0:
                ans +=(n % 10) * (n % 10)
                n //=10

            n =ans


        return n == 1