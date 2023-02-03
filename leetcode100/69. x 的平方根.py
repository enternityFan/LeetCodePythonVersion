#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：69. x 的平方根.py
@Author ：HuntingGame
@Date ：2023-02-03 13:42 
C'est la vie!!! enjoy ur day :D
'''


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x < 3:
            return 1
        ans = 1
        L = 1
        R = x
        M = 0
        while L <=R:
            M = (L + R) //2
            if M * M <=x:
                ans = M
                L = M +1
            else:
                R = M -1
        return ans
